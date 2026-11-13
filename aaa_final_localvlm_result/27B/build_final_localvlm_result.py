"""Model-comparison evidence: common samples, ranks, source-cluster bootstrap, costs."""
import argparse
import csv
import datetime
import itertools
import json
import math
from pathlib import Path
import statistics

import numpy as np
from compare_local_judges_gemini import values
from audit_qwen_gemini_agreement import continuous

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/"metric/qwen3_8-27b/20261112_subset100_H_7gpu_v1"
METHODS=["JoyAI-edit","LiveEdit","Lucy-Edit","SANA-Streaming-edit","StreamDiffusionV2-edit","StreamEdit","Wan2.1-VACE"]
METRICS=["EFA","IS_g","SOL","SCL","SEO","DSR_Contrast","PSR","CF_g","CA_HDF"]
PRIMARY=["Attribute","Camera","Composition","Motion","Spatial","Style","Temporal"]


def dumpcsv(p,rs):
    with p.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rs for k in r)));w.writeheader();w.writerows(rs)


def ranks(xs,high):
    order=sorted(range(len(xs)),key=lambda i:xs[i],reverse=high);rs=[0.]*len(xs);i=0
    while i<len(order):
        j=i+1
        while j<len(order) and abs(xs[order[i]]-xs[order[j]])<1e-12:j+=1
        for k in range(i,j):rs[order[k]]=(i+j+1)/2
        i=j
    return rs


def relation(a,b):
    return 0 if abs(a-b)<1e-12 else (1 if a>b else -1)


def compare(a,b,high):
    ra,rb=ranks(a,high),ranks(b,high)
    rho=statistics.correlation(ra,rb) if len(set(ra))>1 and len(set(rb))>1 else None
    c=d=tx=ty=both=0
    for i,j in itertools.combinations(range(7),2):
        x,y=relation(a[i],a[j]),relation(b[i],b[j])
        if not x and not y:both+=1
        elif not x:tx+=1
        elif not y:ty+=1
        elif x==y:c+=1
        else:d+=1
    den=math.sqrt((c+d+tx)*(c+d+ty))
    topa={i for i,x in enumerate(ra) if x==min(ra)}
    topb={i for i,x in enumerate(rb) if x==min(rb)}
    return {"spearman":rho,"kendall_tau_b":(c-d)/den if den else None,
            "pair_exact_agreement":(c+both)/21,"concordant":c,"discordant":d,
            "tie_local_only":tx,"tie_gemini_only":ty,"tie_both":both,
            "top1_same_set":topa==topb,
            "top3_overlap":len({i for i,x in enumerate(ra) if x<=3}&{i for i,x in enumerate(rb) if x<=3}),
            "max_rank_change":max(abs(x-y) for x,y in zip(ra,rb))}


def table(headers,rs):
    return "\n".join(["| "+" | ".join(headers)+" |","|"+"|".join("---" for _ in headers)+"|"]+
        ["| "+" | ".join(str(v) for v in r)+" |" for r in rs])


def fmt(x,d=3):return "N/A" if x is None else f"{float(x):.{d}f}"


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--bootstrap",type=int,default=1000);args=ap.parse_args()
    out=args.output
    if out.exists() and any(out.iterdir()):raise ValueError("Nonempty output; refuse overwrite")
    out.mkdir(parents=True,exist_ok=True)
    meta={r["sample_id"]:r for r in json.loads((RUN/"records.json").read_text())}
    local={};old={};cost=[];sourcefiles=[]
    for m in METHODS:
        local[m]={r["edit_id"]:r for r in map(lambda p:json.loads(p.read_text()),(RUN/"methods"/m/"records").glob("*.json"))}
        for t,folder in [("consistency","gemini_full_7models_v2"),("preservation","gemini_preserve/full_7models")]:
            p=ROOT/"metric"/folder/m/"results.jsonl";sourcefiles.append(str(p))
            with p.open() as f:old[t,m]={r["edit_id"]:r for r in map(json.loads,f) if r.get("record_status")=="valid"}
        states=[json.loads(p.read_text()) for p in (RUN/"methods"/m/"attempts").glob("*/*/status.json")]
        valid=[s for s in states if s["status"]=="valid"]
        secs=[s["elapsed_sec"] for s in valid]
        ends=[s["started"]+s["elapsed_sec"] for s in valid]
        cost.append({"method":m,"valid_interactions":len(local[m]),"planned":300,
            "mean_request_sec":statistics.mean(secs),"median_request_sec":float(np.median(secs)),
            "P90_request_sec":float(np.quantile(secs,.9)),
            "valid_request_hours":sum(secs)/3600,"all_recorded_attempt_hours":sum(s.get("elapsed_sec",0) for s in states)/3600,
            "attempts_missing_elapsed":sum("elapsed_sec" not in s for s in states),
            "peak_allocated_mib":max(s.get("peak_allocated_mib",0) for s in valid),
            "mean_prompt_tokens":statistics.mean(s["prompt_tokens"] for s in valid),
            "mean_output_tokens":statistics.mean(s["completion_tokens"] for s in valid),
            "request_only_interactions_per_hour":3600/statistics.mean(secs),
            "failed_attempts":sum(s["status"]!="valid" for s in states),
            "first_recorded_request":datetime.datetime.fromtimestamp(min(s["started"] for s in states)).isoformat(),
            "last_recorded_valid_end":datetime.datetime.fromtimestamp(max(ends)).isoformat()})
    edits=sorted(set.intersection(*(set(local[m]) for m in METHODS)))
    assert len(edits)==299
    sourceids=sorted({meta[local[METHODS[0]][e]["sample_id"]]["video_id"] for e in edits})
    sourceindex={v:i for i,v in enumerate(sourceids)}
    types=np.array([PRIMARY.index(meta[local[METHODS[0]][e]["sample_id"]]["taxonomy"]["primary_type"]) for e in edits])
    src=np.array([sourceindex[meta[local[METHODS[0]][e]["sample_id"]]["video_id"]] for e in edits])
    vals=np.full((2,9,7,len(edits)),np.nan)
    gemtoken={"prompt":0,"output":0,"thinking":0,"total":0}
    for j,m in enumerate(METHODS):
        for i,e in enumerate(edits):
            r=local[m][e];c=old["consistency",m][e];p=old["preservation",m][e]
            for t,g in [("consistency",c),("preservation",p)]:
                for role in ["reference","edited"]:
                    k=role+"_video_sha256";assert r[t+"_result"]["inputs"][k]==g["inputs"][k]
                usage=g["api"]["usage_metadata"]
                for dest,key in [("prompt","promptTokenCount"),("output","candidatesTokenCount"),
                                 ("thinking","thoughtsTokenCount"),("total","totalTokenCount")]:
                    gemtoken[dest]+=usage.get(key,0)
            a=r["metrics"];b={**values(c,"consistency"),**values(p,"preservation")}
            for k,metric in enumerate(METRICS):
                if a[metric] is not None:vals[0,k,j,i]=a[metric]
                if b[metric] is not None:vals[1,k,j,i]=b[metric]
    def means(v,w=None):
        if w is None:w=np.ones(len(edits))
        masked=np.isfinite(v);numer=np.nansum(v*w,axis=-1);denom=np.sum(masked*w,axis=-1)
        result=np.divide(numer,denom,out=np.full(numer.shape,np.nan),where=denom>0)
        for side in range(2):
            for j in range(7):
                ts=[]
                for t in range(7):
                    ids=types==t;vs=v[side,6,j,ids];ws=w[ids]
                    den=np.sum(np.isfinite(vs)*ws)
                    ts.append(np.nansum(vs*ws)/den if den else np.nan)
                result[side,6,j]=np.mean(ts)
        return result
    ms=means(vals)
    score_rows=[];rank_rows=[]
    for k,metric in enumerate(METRICS):
        high=metric not in ["SOL","SCL"];ra=ranks(ms[0,k],high);rb=ranks(ms[1,k],high)
        for j,m in enumerate(METHODS):
            score_rows.append({"method":m,"metric":metric,"common_interactions":len(edits),
                "local_mean":ms[0,k,j],"gemini_mean":ms[1,k,j],"bias":ms[0,k,j]-ms[1,k,j],
                "local_rank":ra[j],"gemini_rank":rb[j],
                "local_observed":int(np.isfinite(vals[0,k,j]).sum()),"gemini_observed":int(np.isfinite(vals[1,k,j]).sum())})
        rank_rows.append({"metric":metric,**compare(ms[0,k],ms[1,k],high)})
    rng=np.random.default_rng(20261113);boot={m:{"spearman":[],"kendall":[],"pair_agreement":[]} for m in METRICS}
    pairwin=np.zeros((2,9,7,7));rankfreq=np.zeros((2,9,7,7));finite=np.zeros(9)
    for rep in range(args.bootstrap):
        counts=np.bincount(rng.integers(0,len(sourceids),len(sourceids)),minlength=len(sourceids))
        mm=means(vals,counts[src])
        for k,metric in enumerate(METRICS):
            if not np.isfinite(mm[:,k]).all():continue
            finite[k]+=1;high=metric not in ["SOL","SCL"];st=compare(mm[0,k],mm[1,k],high)
            if st["spearman"] is not None:boot[metric]["spearman"].append(st["spearman"])
            if st["kendall_tau_b"] is not None:boot[metric]["kendall"].append(st["kendall_tau_b"])
            boot[metric]["pair_agreement"].append(st["pair_exact_agreement"])
            for side in range(2):
                rr=ranks(mm[side,k],high)
                for i,rank in enumerate(rr):
                    # Fractional ranks split their frequency to adjacent bins.
                    lo=int(math.floor(rank))-1;hi=int(math.ceil(rank))-1
                    if lo==hi:rankfreq[side,k,i,lo]+=1
                    else:rankfreq[side,k,i,lo]+=.5;rankfreq[side,k,i,hi]+=.5
                for i,j in itertools.combinations(range(7),2):
                    d=relation(mm[side,k,i],mm[side,k,j])*(1 if high else -1)
                    pairwin[side,k,i,j]+=1 if d>0 else .5 if d==0 else 0
    ci=[]
    for row in rank_rows:
        metric=row["metric"];k=METRICS.index(metric)
        for label,key in [("spearman","spearman"),("kendall_tau_b","kendall"),("pair_exact_agreement","pair_agreement")]:
            xs=boot[metric][key];row[label+"_ci_low"]=float(np.quantile(xs,.025)) if xs else None
            row[label+"_ci_high"]=float(np.quantile(xs,.975)) if xs else None
        row["bootstrap_valid_repetitions"]=int(finite[k])
    pair_rows=[]
    for k,metric in enumerate(METRICS):
        high=metric not in ["SOL","SCL"]
        for i,j in itertools.combinations(range(7),2):
            la=relation(ms[0,k,i],ms[0,k,j])*(1 if high else -1);ga=relation(ms[1,k,i],ms[1,k,j])*(1 if high else -1)
            p=pairwin[1,k,i,j]/finite[k] if finite[k] else None
            pair_rows.append({"metric":metric,"model_A":METHODS[i],"model_B":METHODS[j],
                "local_A_better":la,"gemini_A_better":ga,"same_relation":la==ga,
                "local_A_better_bootstrap_probability":pairwin[0,k,i,j]/finite[k] if finite[k] else None,
                "gemini_A_better_bootstrap_probability":p,
                "reference_pair_stable_95pct":p is not None and (p>=.95 or p<=.05)})
    group_ranks=[]
    for field in ["split","category"]:
        cats=sorted({meta[local[METHODS[0]][e]["sample_id"]][field] for e in edits})
        for cat in cats:
            weights=np.array([meta[local[METHODS[0]][e]["sample_id"]][field]==cat for e in edits],dtype=float)
            mm=means(vals,weights)
            for k,metric in enumerate(METRICS):
                if np.isfinite(mm[:,k]).all():group_ranks.append({"group":field+":"+cat,"metric":metric,
                    **compare(mm[0,k],mm[1,k],metric not in ["SOL","SCL"])})
    load=json.loads((ROOT/"Model/worldline_local_judges/logs/Qwen3.8-27B/load.json").read_text())
    session=json.loads((RUN/"session.json").read_text());end=json.loads((RUN/"session_status.json").read_text())
    cfg=json.loads((RUN/"experiment.json").read_text())
    resources={"production_costs":cost,"resumed_session_wall_hours":(end["ended"]-session["started"])/3600,
        "resumed_7card_wall_hours_upper_proxy":7*(end["ended"]-session["started"])/3600,
        "recorded_valid_request_hours":sum(r["valid_request_hours"] for r in cost),
        "recorded_all_attempt_hours":sum(r["all_recorded_attempt_hours"] for r in cost),
        "separate_deployment_load_measurement":load,"production_config":cfg,
        "gemini_usage_on_common_nodes":gemtoken,"gemini_successful_records":len(edits)*7*2,
        "unknown":["Gemini service GPU/memory/energy","Gemini invoice/actual price","local rental price","true sampled GPU utilization integral"],
        "wall_clock_caution":"resumed wall includes load/IO, excludes first failed session and pause; 7xwall is reservation upper proxy, not measured GPU compute hours",
        "request_timing_caution":"elapsed_sec includes processor/schema/inference/validation; not isolated GPU generation"}
    for name,rows in [("scores_and_ranks.csv",score_rows),("ranking_agreement.csv",rank_rows),
                     ("pairwise_21_comparisons.csv",pair_rows),("group_ranking_agreement.csv",group_ranks),
                     ("production_runtime_memory.csv",cost)]:
        dumpcsv(out/name,rows)
    freq=[{"metric":metric,"judge":["Qwen","Gemini"][side],"method":METHODS[i],
           "rank_frequency":(rankfreq[side,k,i]/finite[k]).tolist() if finite[k] else None}
          for side in range(2) for k,metric in enumerate(METRICS) for i in range(7)]
    (out/"bootstrap_rank_frequencies.json").write_text(json.dumps(freq,ensure_ascii=False,indent=2))
    (out/"resources.json").write_text(json.dumps(resources,ensure_ascii=False,indent=2))
    (out/"analysis_provenance.json").write_text(json.dumps({"run":str(RUN),"common_edit_nodes":edits,
        "common_sources":len(sourceids),"common_interactions":len(edits)*7,"excluded_edit_nodes":["human_071_E2B"],
        "bootstrap_repetitions":args.bootstrap,"bootstrap_unit":"source video; same resample applied across all seven methods and both judges",
        "seed":20261113,"no_model_calls":True,"source_result_files":sourcefiles},ensure_ascii=False,indent=2))
    lines=["# 本地单卡27B裁判与Gemini：七生成模型比较的核心结果",
        "",
        "## 1. 结论边界",
        "本报告检验的是**单卡部署的本地VLM能否保留七个生成模型的相对比较**，不是逐交互完全一致。",
        "本次每实例只使用一张H20；整批采用七个单卡实例并行，并非只占一张卡。",
        "没有Gemini服务端硬件、能耗和实际费用，因此**不能证明硬件资源或总成本少于Gemini**。"
        "可证明的是本地需求可测、无逐次远程API依赖，并节省远程请求次数这一流程开销。",
        "",
        "## 2. 样本与公平配对",
        f"计划2100交互，实际2098有效。排名分析统一七方法共同有效的{len(edits)}编辑节点，"
        f"即{len(edits)*7}交互、{len(sourceids)}源视频。human_071_E2B在StreamEdit/Wan缺失，"
        "故排名表七方法都排除此节点，避免样本差造成排名变化。未补0。",
        "PSR采用七编辑一级类型等权；SOL/SEO/CA保留裁判自身适用分母并在CSV披露。",
        "",
        "## 3. 单卡本地配置与开销",
        table(["项目","数据/说明"],[
            ["模型","Qwen/Qwen3.8-27B"],["revision",cfg["revision"]],
            ["部署","BF16单卡，无量化/CPU权重卸载；七独立实例"],
            ["硬件","每实例H20约96GB"],["环境",f"PyTorch {load['torch']}；CUDA {load['cuda_runtime']}；Transformers 5.17.0 / SDPA"],
            ["输入","参考6fps，结果3fps，最多15秒，完整固定采样及独立末帧"],
            ["上下文/最大输出",f"{cfg['max_context']} / {cfg['max_output_tokens']} tokens"],
            ["加载后显存（另一次部署测量）",f"{load['loaded_nvidia_smi_mib']}MiB，不是本次全批常驻采样"],
            ["本次请求峰值（PyTorch allocated）",f"{max(r['peak_allocated_mib'] for r in cost):.0f}MiB；非nvidia-smi连续峰值"],
            ["恢复运行墙钟",f"{resources['resumed_session_wall_hours']:.2f}小时，含加载/IO，排除首次失败会话"],
            ["记录有效请求时长合计",f"{resources['recorded_valid_request_hours']:.2f}小时，非GPU利用率积分"],
            ["成功覆盖",f"2098/2100={2098/2100*100:.2f}%；2条输入恢复失败"]]),
        "",
        table(["方法","有效交互","均请求秒","中位秒","P90秒","请求内吞吐/小时","峰值MiB"],
              [[r["method"],r["valid_interactions"],fmt(r["mean_request_sec"],2),fmt(r["median_request_sec"],2),
                fmt(r["P90_request_sec"],2),fmt(r["request_only_interactions_per_hour"],1),
                fmt(r["peak_allocated_mib"],0)] for r in cost]),
        "请求时长包含processor/Schema/推理/校验，不是纯GPU生成。吞吐仅按请求时长倒数，不含解码/加载等待。",
        "",
        f"## 4. 七模型得分与名次（{len(edits)}共同节点）",
        "比例展示百分比；SOL/SCL秒；IS-g/CF-g为1～5。名次1为更好，并列使用平均名次。"]
    for k,metric in enumerate(METRICS):
        lines += ["### "+metric,table(["生成方法","Qwen分数","Qwen名次","Gemini分数","Gemini名次","两边适用数"],
            [[r["method"],fmt(r["local_mean"]*(100 if metric not in ["IS_g","CF_g","SOL","SCL"] else 1),2),
              fmt(r["local_rank"],1),fmt(r["gemini_mean"]*(100 if metric not in ["IS_g","CF_g","SOL","SCL"] else 1),2),
              fmt(r["gemini_rank"],1),f"{r['local_observed']}/{r['gemini_observed']}"]
             for r in score_rows if r["metric"]==metric])]
    lines += ["## 5. 七模型比较一致性",
        table(["指标","Spearman","Kendall τ-b","21对精确关系一致","Top1集合一致","Top3重合数","最大名次变动"],
            [[r["metric"],fmt(r["spearman"]),fmt(r["kendall_tau_b"]),fmt(r["pair_exact_agreement"]*100,1)+"%",
              r["top1_same_set"],r["top3_overlap"],fmt(r["max_rank_change"],1)] for r in rank_rows]),
        "两两关系精确一致将单边并列视为不同关系；并列不能任意打破来提高一致率。",
        "",
        "## 6. 源视频组bootstrap稳定性",
        f"{args.bootstrap}次重采样，以源视频为单位保留相关分支，同一次抽样同时应用全部方法和两裁判。",
        "区间为该子集内重采样诊断，不是模型正确率置信区间。PSR缺类型或SOL无有效时间的重采样不纳入，有效次数公开。",
        table(["指标","Spearman 95%区间","Kendall 95%区间","有效重采样"],
            [[r["metric"],f"[{fmt(r['spearman_ci_low'])}, {fmt(r['spearman_ci_high'])}]",
              f"[{fmt(r['kendall_tau_b_ci_low'])}, {fmt(r['kendall_tau_b_ci_high'])}]",r["bootstrap_valid_repetitions"]]
             for r in rank_rows]),
        "21对明细及参考优劣方向稳定概率见pairwise_21_comparisons.csv。稳定组定义预先固定为Gemini重采样"
        "同一优劣方向概率≥95%；不是根据Qwen是否一致挑选。小差距的排名互换宜解释为接近，而非强行认定冲突。",
        "",
        "## 7. 来源与五类视频的排序一致性",
        table(["分组","指标","Spearman","Kendall","21对一致率"],
            [[r["group"],r["metric"],fmt(r["spearman"]),fmt(r["kendall_tau_b"]),
              fmt(r["pair_exact_agreement"]*100,1)+"%"] for r in group_ranks]),
        "",
        "## 8. Gemini调用与资源对照",
        f"相同{len(edits)}节点×七方法，历史Gemini有{len(edits)*7*2}条成功评分调用记录；本地每交互一次完整九指标生成。",
        "远程两类请求与本地一次联合请求是工程设计差异，不等价于模型本身效率高两倍。",
        f"Gemini成功调用记录token合计：prompt={gemtoken['prompt']}、候选输出={gemtoken['output']}、"
        f"thinking={gemtoken['thinking']}、total={gemtoken['total']}。不含所有失败重试费用。",
        "不同模型token含义/计费方式不同，不能直接以token数推断计算量或成本。"
        "实际账单、GPU租赁价格和Gemini服务硬件未知，因此不填虚构费用/节省百分比。",
        "",
        "## 9. 可支持的论文表述与不可支持的表述",
        "建议：『单卡H20可运行BF16的27B本地VLM裁判。在固定视频编辑子集上，"
        "它在若干主要指标上保留Gemini对七个生成方法的相对排序；得分和个体判断仍有差异。"
        "本地部署提供明确可控的显存与运行开销，避免逐次依赖远程评分API。』",
        "不可提前写成『九指标完全一致』『单卡整批只用了单卡时间』『总体硬件资源/成本必然低于Gemini』。",
        "SOL系统性偏晚、PSR部分方法高估的原报告结论仍须披露，排名高相关并不使这些问题消失。",
        "本次Subset与开发反馈有部分交集，不能称为独立人工金标准；案例人工/助手帧复核仅支持具体差异解释。",
        "",
        "## 10. 输出与复现",
        "scores_and_ranks.csv：全部63方法指标得分/名次/分母；ranking_agreement.csv：相关与区间；"
        "pairwise_21_comparisons.csv：189对关系与稳定性；group_ranking_agreement.csv：分组；"
        "production_runtime_memory.csv/resources.json：资源；bootstrap_rank_frequencies.json：名次概率；"
        "analysis_provenance.json：共同节点、抽样设置、原结果路径。"]
    (out/"CORE_RESULTS.md").write_text("\n\n".join(lines),encoding="utf-8")
    print("OUTPUT",out)
    for r in rank_rows:print(r["metric"],r["spearman"],r["kendall_tau_b"],r["pair_exact_agreement"])
    print("RESOURCES",resources["resumed_session_wall_hours"],resources["recorded_valid_request_hours"],
          max(r["peak_allocated_mib"] for r in cost))


if __name__=="__main__":main()
