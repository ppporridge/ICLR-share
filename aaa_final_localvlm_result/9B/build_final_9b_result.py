"""Reuse 27B report mathematics, not its model/count claims; add 9B retry audit."""
import collections
import csv
import hashlib
import json
from pathlib import Path
import statistics
import sys

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/"metric/qwen3_5-9b/20261113_subset100_H_directed_7gpu_v2"
OUT=Path(__file__).parent/"aaa_final_localvlm_result/9B"
METHODS=["JoyAI-edit","LiveEdit","Lucy-Edit","SANA-Streaming-edit","StreamDiffusionV2-edit","StreamEdit","Wan2.1-VACE"]


def failure_kind(error):
    if "Final cumulative status must equal" in error:return "累计位与最终pass矛盾"
    if "current_frame_status" in error or "final_anchor_current_status" in error:return "持续性与current数组矛盾"
    if "failure_reason" in error:return "pass与失败原因矛盾"
    if "Unterminated" in error or "JSONDecode" in error:return "JSON未闭合或截断"
    if "schema" in error.lower() or "ValidationError" in error:return "Schema或证据范围"
    if "CF-g" in error:return "CF-g与PSR矛盾"
    if "IS-g" in error or "IS-a" in error:return "量表交叉约束"
    return "其他"


def write_csv(path,rows):
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)))
        w.writeheader();w.writerows(rows)


def main():
    if OUT.exists():raise ValueError("Do not overwrite prior final output")
    end=json.loads((RUN/"session_status.json").read_text())
    if any(code!=0 for code in end["worker_returncodes"]):raise ValueError("Worker did not finish normally")
    local={};missing=[];retry_rows=[];type_counts=collections.Counter();details=[]
    expected=json.loads((RUN/"records.json").read_text())
    snapshot=[]
    import jsonschema
    for m in METHODS:
        local[m]={}
        first=second=third=0;attempt_total=0;failed_attempts=0;identical=0
        for rec in [r for r in expected if r["method"]==m]:
            sid=rec["sample_id"];d=RUN/"methods"/m/"attempts"/sid
            attempts=[]
            for p in sorted(d.glob("attempt_*/status.json")):
                s=json.loads(p.read_text());attempts.append(s);attempt_total+=1
                if s["status"]!="valid":failed_attempts+=1
            file=RUN/"methods"/m/"records"/(sid+".json")
            if file.exists():
                r=json.loads(file.read_text())
                payload=Path(r["raw_answer_file"]).read_bytes()
                if hashlib.sha256(payload).hexdigest()!=r["raw_answer_sha256"]:raise ValueError("Raw hash mismatch "+sid)
                raw=json.loads(payload)
                jsonschema.Draft202012Validator(json.loads(Path(r["schema_file"]).read_text())).validate(raw)
                assert r["generation_calls"]==1
                n=int(Path(r["attempt_directory"]).name.split("_")[-1])
                first+=n==1;second+=n==2;third+=n==3
                local[m][r["edit_id"]]=r
                snapshot.append({"path":str(file),"sha256":hashlib.sha256(file.read_bytes()).hexdigest()})
            else:
                if len(attempts)!=3:raise ValueError("Missing interaction without 3 completed attempts "+sid)
                kind=failure_kind(attempts[-1].get("error",""));type_counts[kind]+=1
                missing.append({"method":m,"sample_id":sid,"edit_id":rec["edit_id"],"video_id":rec["video_id"],
                                "split":rec["split"],"video_type":rec["category"],"edge":rec["edge_name"],
                                "failure_type":kind,"last_error":attempts[-1].get("error","")})
            if len(attempts)>1:
                answers=[p.read_bytes() for p in sorted(d.glob("attempt_*/answer.txt"))]
                identical+=len(answers)>1 and len({hashlib.sha256(a).hexdigest() for a in answers})==1
                prompts=[p.read_bytes() for p in sorted(d.glob("attempt_*/prompt.txt"))]
                details.append({"method":m,"sample_id":sid,"attempts":len(attempts),
                    "obtained_valid_score":file.exists(),
                    "prompt_hash_count":len({hashlib.sha256(a).hexdigest() for a in prompts}),
                    "answer_hash_count":len({hashlib.sha256(a).hexdigest() for a in answers})})
        retry_rows.append({"method":m,"planned":300,"valid":len(local[m]),
            "first_attempt_success":first,"second_attempt_success":second,"third_attempt_success":third,
            "retry_success":second+third,"exhausted_failures":300-len(local[m]),
            "total_attempts":attempt_total,"failed_attempts":failed_attempts,
            "identical_answers_repeated_interactions":identical})
    common=sorted(set.intersection(*(set(local[m]) for m in METHODS)))
    excluded=sorted(set(r["edit_id"] for r in expected)-set(common))
    total=sum(len(x) for x in local.values());miss=2100-total
    # Preserve original builder content/maths; substitutions below are only report plumbing/text.
    template=ROOT/"gemini_test/aaa_final_localvlm_result/27B/build_final_localvlm_result.py"
    code=template.read_text()
    old_root='ROOT=Path(__file__).resolve().parents[1]'
    code=code.replace(old_root,f"ROOT=Path({str(ROOT)!r})")
    code=code.replace('RUN=ROOT/"metric/qwen3_8-27b/20261112_subset100_H_7gpu_v1"',f"RUN=Path({str(RUN)!r})")
    code=code.replace("assert len(edits)==299","assert len(edits)=="+str(len(common)))
    code=code.replace("Qwen3.8-27B","Qwen3.5-9B").replace("27B","9B")
    code=code.replace('"excluded_edit_nodes":["human_071_E2B"]',f'"excluded_edit_nodes":{excluded!r}')
    code=code.replace("实际2098有效。","实际"+str(total)+"有效。")
    code=code.replace("2098/2100={2098/2100*100:.2f}%；2条输入恢复失败",
                      f"{total}/2100={total/2100*100:.2f}%；{miss}条三次尝试后仍无有效评分")
    code=code.replace("human_071_E2B在StreamEdit/Wan缺失，",
                      f"{len(excluded)}个节点在至少一种方法缺失，")
    code=code.replace("恢复运行墙钟","本轮运行墙钟")
    code=code.replace("排除首次失败会话","不含旧无定向重试版本")
    sys.argv=[str(Path(__file__)),"--output",str(OUT),"--bootstrap","1000"]
    exec(compile(code,str(template),"exec"),{"__name__":"__main__","__file__":str(template)})
    write_csv(OUT/"retry_success_and_failures.csv",retry_rows)
    write_csv(OUT/"failed_interactions.csv",missing)
    write_csv(OUT/"retry_request_variation.csv",details)
    (OUT/"verified_result_files.json").write_text(json.dumps(snapshot,indent=2))
    stats={"valid":total,"planned":2100,"missing":miss,"common_nodes":len(common),
           "common_interactions":len(common)*7,"excluded_nodes":excluded,
           "first_success":sum(r["first_attempt_success"] for r in retry_rows),
           "retry_success":sum(r["retry_success"] for r in retry_rows),
           "failure_types":dict(type_counts),"method_details":retry_rows}
    (OUT/"failure_audit.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2))
    lines=["\n\n## 11. 9B特有的失败、定向重试与选择偏差",
        f"本轮{total}/2100有效（{total/2100*100:.2f}%），{miss}个交互三次仍失败，未补0。",
        f"首次成功{stats['first_success']}；定向重试后成功{stats['retry_success']}。",
        "计数为交互；失败尝试不等于失败视频。重试是在完整相同视觉输入上加入原校验错误，"
        "重新生成完整答案，不程序修分或修改数组。",
        "旧无定向重试版本常重复相同prompt与答案，其失败结果及LiveEdit空哈希修复不并入本轮；"
        "它们属于工程迭代历史，不能当作9B能力失败或本轮首次成功。",
        "本轮主要失败是跨字段一致性，说明合法JSON不等于逻辑一致。"
        "缺失可能与指令/原子复杂度相关，故不能认定为随机缺失。",
        "公平排序统一排除任一方法缺失的节点；被排除节点其他方法有效评分仍保存在原run。"
        "共同集排名高相关不能证明全部2100交互都可靠，也不能替代失败覆盖率。",
        "\n### 三次后失败类型"]
    lines+=["|类型|交互数|","|---|---:|"]+[f"|{k}|{v}|" for k,v in type_counts.items()]
    lines+=["\n### 各方法成功及重试",
            "|方法|首试成功|第二次成功|第三次成功|最终失败|",
            "|---|---:|---:|---:|---:|"]
    lines += [f"|{r['method']}|{r['first_attempt_success']}|{r['second_attempt_success']}|{r['third_attempt_success']}|{r['exhausted_failures']}|" for r in retry_rows]
    lines += ["\n### 报告解读",
        "均值偏差与相对排序分别报告。个体分歧可接受，但观察幻觉、事件开始与状态存在混淆、"
        "时钟问题不应未经复核一概归因模型较小。SOL/SEO/CA自身分母须一并引用。",
        "本轮不支持宣称9B比27B更准确或与Gemini完全等价；两模型有效共同集不同，"
        "若直接比较需要再取两裁判七方法共同节点，而非比较各自报告的相关系数。",
        "file_hashes.json覆盖交付文件；未复制巨大原始媒体，但所有源路径与raw哈希可追溯。"]
    core=OUT/"CORE_RESULTS.md"
    core.write_text(core.read_text()+"\n".join(lines),encoding="utf-8")
    (OUT/"README.md").write_text(
        f"# 9B最终结果索引\n\n首读CORE_RESULTS.md。本轮有效{total}/2100，公平比较{len(common)}共同节点。\n\n"
        "- scores_and_ranks.csv / ranking_agreement.csv：九指标均值、排序及不确定性\n"
        "- pairwise_21_comparisons.csv / group_ranking_agreement.csv：完整两两/分组\n"
        "- retry_success_and_failures.csv / failed_interactions.csv / failure_audit.json：9B特有失败与重试\n"
        "- production_runtime_memory.csv / resources.json：实际时长与显存，非GPU利用率积分\n"
        "- analysis_provenance.json / verified_result_files.json：输入集和哈希审计\n"
        "- build_final_9b_result.py：生成程序副本（使用项目内27B模板和共用分析模块）\n\n"
        "未补0；bootstrap基于源视频组，排名一致不是人工正确率。报告必须同时引用缺失覆盖。\n")
    (OUT/"build_final_9b_result.py").write_bytes(Path(__file__).read_bytes())
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file()}
    (OUT/"file_hashes.json").write_text(json.dumps(hashes,indent=2))
    print("9B_FINAL",json.dumps(stats,ensure_ascii=False))


if __name__=="__main__":main()
