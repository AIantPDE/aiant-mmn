# POSTERIOR_CORRECTION_OBJECT_V0

## 1. 目标

`posterior_correction_object_v0` 是 `aiant-mmn` 当前阶段的最小后验修正对象。

它的目标不是表达完整 MMN 后验修正系统，
也不是表达 write-back 或 execution intent，
而是表达一个最小但非空、稳定、可测试、可被下游 preview-only 消费的 posterior correction object。

一句话概括：

> `PosteriorCorrectionObjectV0` 用于表达“基于当前历史对照与已有支撑，当前对象应如何被最小修正”。

---

## 2. 当前定位

在当前 `aiant-mmn` 语境里：

- `historical_comparison_object_v0` 负责表达当前对象与历史对象之间的最小对照关系
- `posterior_correction_object_v0` 负责表达基于这些对照关系，当前对象应如何被最小修正
- 该对象当前仍处于 preview-only / non-executing 阶段

也就是说：

> `PosteriorCorrectionObjectV0` 当前回答的不是“应如何写回记忆层”，
> 而是“当前对象的最小修正方向、强度与依据是什么”。

---

## 3. 当前字段

当前 `PosteriorCorrectionObjectV0` 包含以下字段：

- `correction_version`
- `correction_id`
- `subject_id`
- `correction_target`
- `correction_direction`
- `correction_strength`
- `correction_basis`
- `posterior_notes`
- `trace`

---

## 4. 字段原则

### correction_version

当前对象 contract 版本。固定值：

- `posterior_correction_object_v0`

### correction_id

当前后验修正对象的稳定标识。

当前格式：

- `posterior-correction::{correction_seed}`

### subject_id

当前被修正对象的稳定标识。

说明：

该字段用于表达：

- 这次 posterior correction 围绕谁展开
- downstream 如何稳定引用这次修正对象

### correction_target

当前修正对象作用的最小目标集合。

说明：

该字段当前保持最小字符串集合形式，
用于表达当前修正主要指向哪些维度或对象面。

### correction_direction

当前修正方向。

当前允许值：

- `up`
- `down`
- `neutral`

### correction_strength

当前修正强度提示。

当前允许值：

- `light`
- `medium`
- `strong`

### correction_basis

当前修正依据的最小集合。

说明：

该字段当前保持最小字符串集合形式，
用于表达这次修正基于哪些最小后验依据。

### posterior_notes

当前后验修正的最小说明文本。

说明：

该字段只表达最小修正说明，
不提前扩张为 richer explanation graph。

### trace

当前后验修正对象的最小 trace 对象。

当前至少表达：

- `source_stage`
- `correction_id`
- `subject_id`
- `correction_direction`
- `correction_strength`
- `correction_basis_count`

---

## 5. 当前 builder 行为

当前 `build_posterior_correction_object_v0(...)` 的最小行为包括：

- 校验 `correction_seed` 非空
- 校验 `subject_id` 非空
- 校验 `correction_direction` 属于允许枚举
- 校验 `correction_strength` 属于允许枚举
- 对 tuple-like 字段做最小规范化
- 生成稳定 `correction_id`
- 生成最小 `trace`
- 返回 `PosteriorCorrectionObjectV0`

---

## 6. 非目标

当前对象明确不包含：

- write-back layer
- write-back mode
- retention hint
- execution payload
- worker target
- queue name
- dispatch plan
- backend mutation intent

也就是说：

> `PosteriorCorrectionObjectV0` 当前只表达最小后验修正语义，
> 不表达 write-back，也不表达 executable plan。

---

## 7. 与后续 richer MMN objects 的关系

当前对象不应被误解为：

- `MemoryWriteBackRequest`
- `MemoryWriteBackRecord`

更准确地说：

> `PosteriorCorrectionObjectV0` 是当前 `aiant-mmn` 在 preview-only / non-executing 阶段，
> 为 MMN 后验修正能力提供的最小对象壳。

---

## 8. 当前阶段的一句话总结

可以用下面这句话概括当前对象：

> `PosteriorCorrectionObjectV0` 是 `aiant-mmn` 当前阶段的最小后验修正对象，
> 用于稳定表达“当前对象应如何被最小修正”。