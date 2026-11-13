# 本地单卡27B裁判与Gemini：七生成模型比较的核心结果



## 1. 结论边界

本报告检验的是**单卡部署的本地VLM能否保留七个生成模型的相对比较**，不是逐交互完全一致。

本次每实例只使用一张H20；整批采用七个单卡实例并行，并非只占一张卡。

没有Gemini服务端硬件、能耗和实际费用，因此**不能证明硬件资源或总成本少于Gemini**。可证明的是本地需求可测、无逐次远程API依赖，并节省远程请求次数这一流程开销。



## 2. 样本与公平配对

计划2100交互，实际2098有效。排名分析统一七方法共同有效的299编辑节点，即2093交互、100源视频。human_071_E2B在StreamEdit/Wan缺失，故排名表七方法都排除此节点，避免样本差造成排名变化。未补0。

PSR采用七编辑一级类型等权；SOL/SEO/CA保留裁判自身适用分母并在CSV披露。



## 3. 单卡本地配置与开销

| 项目 | 数据/说明 |
|---|---|
| 模型 | Qwen/Qwen3.8-27B |
| revision | 37561816e66b5b9153b1b64c10968c18c1e6f4a0 |
| 部署 | BF16单卡，无量化/CPU权重卸载；七独立实例 |
| 硬件 | 每实例H20约96GB |
| 环境 | PyTorch 2.7.1+cu126；CUDA 12.6；Transformers 5.17.0 / SDPA |
| 输入 | 参考6fps，结果3fps，最多15秒，完整固定采样及独立末帧 |
| 上下文/最大输出 | 49152 / 12288 tokens |
| 加载后显存（另一次部署测量） | 52613MiB，不是本次全批常驻采样 |
| 本次请求峰值（PyTorch allocated） | 60580MiB；非nvidia-smi连续峰值 |
| 恢复运行墙钟 | 5.46小时，含加载/IO，排除首次失败会话 |
| 记录有效请求时长合计 | 31.92小时，非GPU利用率积分 |
| 成功覆盖 | 2098/2100=99.90%；2条输入恢复失败 |



| 方法 | 有效交互 | 均请求秒 | 中位秒 | P90秒 | 请求内吞吐/小时 | 峰值MiB |
|---|---|---|---|---|---|---|
| JoyAI-edit | 300 | 55.06 | 53.67 | 68.42 | 65.4 | 60230 |
| LiveEdit | 300 | 54.68 | 53.86 | 67.58 | 65.8 | 60230 |
| Lucy-Edit | 300 | 55.42 | 54.94 | 69.12 | 65.0 | 60230 |
| SANA-Streaming-edit | 300 | 53.84 | 53.21 | 66.92 | 66.9 | 60230 |
| StreamDiffusionV2-edit | 300 | 54.98 | 53.64 | 66.41 | 65.5 | 60230 |
| StreamEdit | 299 | 55.20 | 54.15 | 68.44 | 65.2 | 60580 |
| Wan2.1-VACE | 299 | 54.27 | 52.79 | 67.51 | 66.3 | 60228 |

请求时长包含processor/Schema/推理/校验，不是纯GPU生成。吞吐仅按请求时长倒数，不含解码/加载等待。



## 4. 七模型得分与名次（299共同节点）

比例展示百分比；SOL/SCL秒；IS-g/CF-g为1～5。名次1为更好，并列使用平均名次。

### EFA

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 35.59 | 1.0 | 38.66 | 1.0 | 299/299 |
| LiveEdit | 25.78 | 2.0 | 33.84 | 2.0 | 299/299 |
| Lucy-Edit | 10.51 | 7.0 | 18.95 | 7.0 | 299/299 |
| SANA-Streaming-edit | 14.44 | 5.0 | 21.27 | 6.0 | 299/299 |
| StreamDiffusionV2-edit | 13.35 | 6.0 | 22.19 | 5.0 | 299/299 |
| StreamEdit | 20.68 | 3.0 | 23.58 | 3.0 | 299/299 |
| Wan2.1-VACE | 17.95 | 4.0 | 23.33 | 4.0 | 299/299 |

### IS_g

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 2.38 | 1.0 | 2.45 | 1.0 | 299/299 |
| LiveEdit | 1.93 | 2.0 | 2.18 | 2.0 | 299/299 |
| Lucy-Edit | 1.39 | 7.0 | 1.61 | 7.0 | 299/299 |
| SANA-Streaming-edit | 1.49 | 5.0 | 1.76 | 6.0 | 299/299 |
| StreamDiffusionV2-edit | 1.43 | 6.0 | 1.78 | 5.0 | 299/299 |
| StreamEdit | 1.71 | 3.0 | 1.83 | 4.0 | 299/299 |
| Wan2.1-VACE | 1.62 | 4.0 | 1.85 | 3.0 | 299/299 |

### SOL

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 4.66 | 1.0 | 1.78 | 1.0 | 127/143 |
| LiveEdit | 7.79 | 2.0 | 2.76 | 2.0 | 95/132 |
| Lucy-Edit | 9.17 | 4.0 | 5.35 | 7.0 | 44/79 |
| SANA-Streaming-edit | 9.31 | 6.0 | 3.32 | 3.0 | 61/83 |
| StreamDiffusionV2-edit | 9.11 | 3.0 | 3.94 | 5.0 | 60/86 |
| StreamEdit | 9.19 | 5.0 | 3.37 | 4.0 | 80/93 |
| Wan2.1-VACE | 10.31 | 7.0 | 4.04 | 6.0 | 70/92 |

### SCL

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 11.02 | 1.0 | 11.13 | 1.0 | 299/299 |
| LiveEdit | 12.97 | 2.0 | 12.10 | 2.0 | 299/299 |
| Lucy-Edit | 14.24 | 7.0 | 13.76 | 7.0 | 299/299 |
| SANA-Streaming-edit | 13.93 | 5.0 | 13.16 | 4.0 | 299/299 |
| StreamDiffusionV2-edit | 13.92 | 4.0 | 13.25 | 6.0 | 299/299 |
| StreamEdit | 13.45 | 3.0 | 12.99 | 3.0 | 299/299 |
| Wan2.1-VACE | 14.02 | 6.0 | 13.21 | 5.0 | 299/299 |

### SEO

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 34.22 | 1.0 | 30.82 | 1.0 | 213/207 |
| LiveEdit | 17.93 | 2.0 | 22.99 | 2.0 | 209/202 |
| Lucy-Edit | 4.51 | 7.0 | 7.16 | 7.0 | 210/204 |
| SANA-Streaming-edit | 6.04 | 6.0 | 11.02 | 4.0 | 212/206 |
| StreamDiffusionV2-edit | 8.16 | 4.0 | 10.16 | 6.0 | 210/205 |
| StreamEdit | 12.65 | 3.0 | 13.07 | 3.0 | 211/210 |
| Wan2.1-VACE | 6.34 | 5.0 | 10.67 | 5.0 | 209/209 |

### DSR_Contrast

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 25.08 | 1.0 | 23.75 | 1.0 | 299/299 |
| LiveEdit | 12.04 | 2.0 | 17.06 | 2.0 | 299/299 |
| Lucy-Edit | 2.68 | 7.0 | 4.68 | 7.0 | 299/299 |
| SANA-Streaming-edit | 5.02 | 4.5 | 9.70 | 4.5 | 299/299 |
| StreamDiffusionV2-edit | 5.02 | 4.5 | 8.70 | 6.0 | 299/299 |
| StreamEdit | 8.36 | 3.0 | 11.37 | 3.0 | 299/299 |
| Wan2.1-VACE | 4.68 | 6.0 | 9.70 | 4.5 | 299/299 |

### PSR

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 80.27 | 1.0 | 67.58 | 2.0 | 299/299 |
| LiveEdit | 50.72 | 5.0 | 33.30 | 5.0 | 299/299 |
| Lucy-Edit | 32.80 | 7.0 | 19.61 | 6.0 | 299/299 |
| SANA-Streaming-edit | 76.18 | 2.0 | 71.35 | 1.0 | 299/299 |
| StreamDiffusionV2-edit | 41.63 | 6.0 | 16.58 | 7.0 | 299/299 |
| StreamEdit | 63.96 | 4.0 | 58.84 | 4.0 | 299/299 |
| Wan2.1-VACE | 71.58 | 3.0 | 67.55 | 3.0 | 299/299 |

### CF_g

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 3.77 | 1.0 | 3.48 | 3.0 | 299/299 |
| LiveEdit | 2.66 | 5.0 | 2.15 | 5.0 | 299/299 |
| Lucy-Edit | 2.06 | 7.0 | 1.79 | 7.0 | 299/299 |
| SANA-Streaming-edit | 3.71 | 2.0 | 3.70 | 1.0 | 299/299 |
| StreamDiffusionV2-edit | 2.31 | 6.0 | 1.82 | 6.0 | 299/299 |
| StreamEdit | 3.06 | 4.0 | 3.06 | 4.0 | 299/299 |
| Wan2.1-VACE | 3.58 | 3.0 | 3.49 | 2.0 | 299/299 |

### CA_HDF

| 生成方法 | Qwen分数 | Qwen名次 | Gemini分数 | Gemini名次 | 两边适用数 |
|---|---|---|---|---|---|
| JoyAI-edit | 35.71 | 1.0 | 44.64 | 1.0 | 56/56 |
| LiveEdit | 21.43 | 2.0 | 28.57 | 2.0 | 56/56 |
| Lucy-Edit | 5.36 | 6.5 | 3.57 | 7.0 | 56/56 |
| SANA-Streaming-edit | 7.14 | 5.0 | 17.86 | 4.0 | 56/56 |
| StreamDiffusionV2-edit | 5.36 | 6.5 | 7.14 | 6.0 | 56/56 |
| StreamEdit | 14.29 | 3.5 | 19.64 | 3.0 | 56/56 |
| Wan2.1-VACE | 14.29 | 3.5 | 12.50 | 5.0 | 56/56 |

## 5. 七模型比较一致性

| 指标 | Spearman | Kendall τ-b | 21对精确关系一致 | Top1集合一致 | Top3重合数 | 最大名次变动 |
|---|---|---|---|---|---|---|
| EFA | 0.964 | 0.905 | 95.2% | True | 3 | 1.0 |
| IS_g | 0.929 | 0.810 | 90.5% | True | 2 | 1.0 |
| SOL | 0.571 | 0.429 | 71.4% | True | 2 | 3.0 |
| SCL | 0.893 | 0.810 | 90.5% | True | 3 | 2.0 |
| SEO | 0.857 | 0.714 | 85.7% | True | 3 | 2.0 |
| DSR_Contrast | 0.918 | 0.850 | 85.7% | True | 3 | 1.5 |
| PSR | 0.929 | 0.810 | 90.5% | False | 3 | 1.0 |
| CF_g | 0.893 | 0.810 | 90.5% | False | 3 | 2.0 |
| CA_HDF | 0.927 | 0.851 | 85.7% | True | 2 | 1.5 |

两两关系精确一致将单边并列视为不同关系；并列不能任意打破来提高一致率。



## 6. 源视频组bootstrap稳定性

1000次重采样，以源视频为单位保留相关分支，同一次抽样同时应用全部方法和两裁判。

区间为该子集内重采样诊断，不是模型正确率置信区间。PSR缺类型或SOL无有效时间的重采样不纳入，有效次数公开。

| 指标 | Spearman 95%区间 | Kendall 95%区间 | 有效重采样 |
|---|---|---|---|
| EFA | [0.607, 1.000] | [0.429, 1.000] | 1000 |
| IS_g | [0.643, 1.000] | [0.524, 1.000] | 1000 |
| SOL | [0.179, 0.929] | [0.143, 0.810] | 1000 |
| SCL | [0.643, 1.000] | [0.524, 1.000] | 1000 |
| SEO | [0.571, 1.000] | [0.429, 1.000] | 1000 |
| DSR_Contrast | [0.679, 1.000] | [0.524, 1.000] | 1000 |
| PSR | [0.821, 0.964] | [0.619, 0.905] | 1000 |
| CF_g | [0.857, 1.000] | [0.714, 1.000] | 1000 |
| CA_HDF | [0.491, 0.973] | [0.390, 0.949] | 1000 |

21对明细及参考优劣方向稳定概率见pairwise_21_comparisons.csv。稳定组定义预先固定为Gemini重采样同一优劣方向概率≥95%；不是根据Qwen是否一致挑选。小差距的排名互换宜解释为接近，而非强行认定冲突。



## 7. 来源与五类视频的排序一致性

| 分组 | 指标 | Spearman | Kendall | 21对一致率 |
|---|---|---|---|---|
| split:real | EFA | 0.847 | 0.781 | 85.7% |
| split:real | IS_g | 0.775 | 0.683 | 81.0% |
| split:real | SOL | 0.321 | 0.143 | 57.1% |
| split:real | SCL | 0.857 | 0.714 | 85.7% |
| split:real | SEO | 0.821 | 0.714 | 85.7% |
| split:real | DSR_Contrast | 0.865 | 0.808 | 66.7% |
| split:real | PSR | 0.821 | 0.619 | 81.0% |
| split:real | CF_g | 0.893 | 0.810 | 90.5% |
| split:real | CA_HDF | 0.750 | 0.684 | 71.4% |
| split:synthetic | EFA | 0.964 | 0.905 | 95.2% |
| split:synthetic | IS_g | 0.893 | 0.810 | 90.5% |
| split:synthetic | SOL | 0.821 | 0.619 | 81.0% |
| split:synthetic | SCL | 0.964 | 0.905 | 95.2% |
| split:synthetic | SEO | 0.964 | 0.905 | 95.2% |
| split:synthetic | DSR_Contrast | 0.973 | 0.950 | 90.5% |
| split:synthetic | PSR | 0.929 | 0.810 | 90.5% |
| split:synthetic | CF_g | 0.964 | 0.905 | 95.2% |
| split:synthetic | CA_HDF | 0.532 | 0.411 | 61.9% |
| category:embodied | EFA | 0.393 | 0.238 | 61.9% |
| category:embodied | IS_g | 0.445 | 0.309 | 57.1% |
| category:embodied | SOL | 0.750 | 0.619 | 81.0% |
| category:embodied | SCL | 0.714 | 0.619 | 81.0% |
| category:embodied | SEO | 0.607 | 0.524 | 76.2% |
| category:embodied | DSR_Contrast | 0.807 | 0.718 | 76.2% |
| category:embodied | PSR | 0.786 | 0.619 | 81.0% |
| category:embodied | CF_g | 0.811 | 0.683 | 81.0% |
| category:embodied | CA_HDF | 0.902 | 0.882 | 81.0% |
| category:human | EFA | 0.919 | 0.781 | 85.7% |
| category:human | IS_g | 0.857 | 0.714 | 85.7% |
| category:human | SOL | 0.679 | 0.524 | 76.2% |
| category:human | SCL | 0.536 | 0.429 | 71.4% |
| category:human | SEO | 0.571 | 0.429 | 71.4% |
| category:human | DSR_Contrast | 0.523 | 0.390 | 66.7% |
| category:human | PSR | 0.857 | 0.714 | 85.7% |
| category:human | CF_g | 0.901 | 0.781 | 85.7% |
| category:human | CA_HDF | 0.791 | 0.723 | 66.7% |
| category:object | EFA | 0.821 | 0.714 | 85.7% |
| category:object | IS_g | 0.929 | 0.810 | 90.5% |
| category:object | SOL | 0.714 | 0.524 | 76.2% |
| category:object | SCL | 0.536 | 0.429 | 71.4% |
| category:object | SEO | 0.821 | 0.714 | 85.7% |
| category:object | DSR_Contrast | 0.727 | 0.651 | 66.7% |
| category:object | PSR | 0.857 | 0.714 | 85.7% |
| category:object | CF_g | 0.964 | 0.905 | 95.2% |
| category:object | CA_HDF | 0.397 | 0.271 | 57.1% |
| category:process | EFA | 0.571 | 0.429 | 71.4% |
| category:process | IS_g | 0.571 | 0.429 | 71.4% |
| category:process | SOL | 0.357 | 0.333 | 66.7% |
| category:process | SCL | 0.857 | 0.714 | 85.7% |
| category:process | SEO | 0.857 | 0.714 | 85.7% |
| category:process | DSR_Contrast | 0.891 | 0.800 | 90.5% |
| category:process | PSR | 0.857 | 0.714 | 85.7% |
| category:process | CF_g | 0.821 | 0.619 | 81.0% |
| category:process | CA_HDF | 0.750 | 0.684 | 71.4% |
| category:scene | EFA | 0.964 | 0.905 | 95.2% |
| category:scene | IS_g | 0.855 | 0.751 | 81.0% |
| category:scene | SOL | 0.357 | 0.333 | 66.7% |
| category:scene | SCL | 0.929 | 0.810 | 90.5% |
| category:scene | SEO | 1.000 | 1.000 | 100.0% |
| category:scene | DSR_Contrast | 0.955 | 0.878 | 90.5% |
| category:scene | PSR | 0.964 | 0.905 | 95.2% |
| category:scene | CF_g | 0.929 | 0.810 | 90.5% |
| category:scene | CA_HDF | 0.846 | 0.743 | 71.4% |



## 8. Gemini调用与资源对照

相同299节点×七方法，历史Gemini有4186条成功评分调用记录；本地每交互一次完整九指标生成。

远程两类请求与本地一次联合请求是工程设计差异，不等价于模型本身效率高两倍。

Gemini成功调用记录token合计：prompt=27236164、候选输出=2624161、thinking=4440798、total=34301123。不含所有失败重试费用。

不同模型token含义/计费方式不同，不能直接以token数推断计算量或成本。实际账单、GPU租赁价格和Gemini服务硬件未知，因此不填虚构费用/节省百分比。



## 9. 可支持的论文表述与不可支持的表述

建议：『单卡H20可运行BF16的27B本地VLM裁判。在固定视频编辑子集上，它在若干主要指标上保留Gemini对七个生成方法的相对排序；得分和个体判断仍有差异。本地部署提供明确可控的显存与运行开销，避免逐次依赖远程评分API。』

不可提前写成『九指标完全一致』『单卡整批只用了单卡时间』『总体硬件资源/成本必然低于Gemini』。

SOL系统性偏晚、PSR部分方法高估的原报告结论仍须披露，排名高相关并不使这些问题消失。

本次Subset与开发反馈有部分交集，不能称为独立人工金标准；案例人工/助手帧复核仅支持具体差异解释。



## 10. 输出与复现

scores_and_ranks.csv：全部63方法指标得分/名次/分母；ranking_agreement.csv：相关与区间；pairwise_21_comparisons.csv：189对关系与稳定性；group_ranking_agreement.csv：分组；production_runtime_memory.csv/resources.json：资源；bootstrap_rank_frequencies.json：名次概率；analysis_provenance.json：共同节点、抽样设置、原结果路径。