# HISTORICAL_COMPARISON_OBJECT_V0

## 1. 目标

`historical_comparison_object_v0` 是 `aiant-mmn` 当前阶段的最小历史对照对象。

它的目标不是表达完整 MMN 历史对照系统，
也不是表达 posterior correction，
而是表达一个最小但非空、稳定、可测试、可被下游 preview-only 消费的 historical comparison object。

一句话概括：

> `HistoricalComparisonObjectV0` 用于表达“当前对象与历史对象相比，最小可见的对照关系是什么”。

---

## 2. 当前定位

在当前 `aiant-mmn` 语境里：

- `memory_preview_output_v0` 负责表达最小记忆预览输出
- `historical_comparison_object_v0` 负责表达当前对象与历史对象之间的最小对照关系
- 该对象当前仍处于 preview-only / non-executing 阶段

也就是说：

> `HistoricalComparisonObjectV0` 当前回答的不是“应当如何修正当前对象”，
> 而是“当前对象与历史对象之间有哪些最小相同点、差异点与对照摘要”。

---

## 3. 当前字段

当前 `HistoricalComparisonObjectV0` 包含以下字段：

- `comparison_version`
- `comparison_id`
- `subject_id`
- `current_pattern_summary`
- `historical_pattern_refs`
- `matched_dimensions`
- `divergent_dimensions`
- `comparison_confidence`
- `comparison_notes`
- `trace`

---

## 4. 字段原则

### comparison_version

当前对象 contract 版本。固定值：

- `historical_comparison_object_v0`

### comparison_id

当前历史对照对象的稳定标识。

当前格式：

- `historical-comparison::{comparison_seed}`

### subject_id

当前被对照对象的稳定标识。

说明：

该字段用于表达：

- 这次 historical comparison 是围绕谁展开的
- downstream 如何稳定引用这次对照对象

### current_pattern_summary

当前对象的最小结构摘要。

说明：

该字段当前只要求为非空字符串，
用于表达当前被对照对象的最小模式摘要。

### historical_pattern_refs

当前对照所引用的历史模式引用集合。

说明：

该字段当前保持最小字符串引用集合形式，
不提前扩张为更重的历史对象嵌套结构。

### matched_dimensions

当前对象与历史对象之间的最小匹配维度集合。

### divergent_dimensions

当前对象与历史对象之间的最小差异维度集合。

### comparison_confidence

当前历史对照对象的最小置信提示。

当前允许值：

- `low`
- `medium`
- `high`

### comparison_notes

当前历史对照的最小说明文本。

说明：

该字段只表达最小对照说明，
不提前扩张为 richer explanation graph。

### trace

当前历史对照对象的最小 trace 对象。

当前至少表达：

- `source_stage`
- `comparison_id`
- `subject_id`
- `comparison_confidence`
- `historical_pattern_ref_count`

---

## 5. 当前 builder 行为

当前 `build_historical_comparison_object_v0(...)` 的最小行为包括：

- 校验 `comparison_seed` 非空
- 校验 `subject_id` 非空
- 校验 `current_pattern_summary` 非空
- 校验 `comparison_confidence` 属于允许枚举
- 对 tuple-like 字段做最小规范化
- 生成稳定 `comparison_id`
- 生成最小 `trace`
- 返回 `HistoricalComparisonObjectV0`

---

## 6. 非目标

当前对象明确不包含：

- correction direction
- correction strength
- write-back intent
- execution payload
- worker target
- queue name
- dispatch plan
- backend mutation intent

也就是说：

> `HistoricalComparisonObjectV0` 当前只表达最小历史对照语义，
> 不表达 posterior correction，也不表达 executable plan。

---

## 7. 与后续 richer MMN objects 的关系

当前对象不应被误解为：

- `PosteriorCorrectionObject`
- `MemoryWriteBackRequest`
- `MemoryWriteBackRecord`

更准确地说：

> `HistoricalComparisonObjectV0` 是当前 `aiant-mmn` 在 preview-only / non-executing 阶段，
> 为 MMN 历史对照能力提供的最小对象壳。

---

## 8. 当前阶段的一句话总结

可以用下面这句话概括当前对象：

> `HistoricalComparisonObjectV0` 是 `aiant-mmn` 当前阶段的最小历史对照对象，
> 用于稳定表达“当前对象与历史对象之间的最小对照关系”。