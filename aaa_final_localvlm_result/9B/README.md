# 9B最终结果索引

首读CORE_RESULTS.md。本轮有效2015/2100，公平比较267共同节点。

- scores_and_ranks.csv / ranking_agreement.csv：九指标均值、排序及不确定性
- pairwise_21_comparisons.csv / group_ranking_agreement.csv：完整两两/分组
- retry_success_and_failures.csv / failed_interactions.csv / failure_audit.json：9B特有失败与重试
- production_runtime_memory.csv / resources.json：实际时长与显存，非GPU利用率积分
- analysis_provenance.json / verified_result_files.json：输入集和哈希审计
- build_final_9b_result.py：生成程序副本（使用项目内27B模板和共用分析模块；从gemini_test环境执行）

未补0；bootstrap基于源视频组，排名一致不是人工正确率。报告必须同时引用缺失覆盖。
