# MEMORY_WRITEBACK_REQUEST_V0

## 1. 目标

`memory_writeback_request_v0` 是 `aiant-mmn` 当前阶段的最小记忆写回请求对象。

它的目标不是表达完整 MMN 写回系统，
也不是表达已完成的记忆沉淀记录，
而是表达一个最小但非空、稳定、可测试、可被下游 preview-only 消费的 memory write-back request object。

一句话概括：

> `MemoryWriteBackRequestV0` 用于表达“当前哪些内容值得写回记忆层，以及拟写去哪一层”。 

---

## 2. 当前定位

在当前 `aiant-mmn` 语境里：

- `historical_comparison_object_v0` 负责表达当前对象与历史对象之间的最小对照关系
- `posterior_correction_object_v0` 负责表达当前对象应如何被最小修正
- `memory_writeback_request_v0` 负责表达当前哪些结果或诊断内容值得被写回记忆层
- 该对象当前仍处于 preview-only / non-executing 阶段

也就是说：

> `MemoryWriteBackRequestV0` 当前回答的不是“写回已经完成了什么”，
> 而是“当前有哪些内容值得被写回、拟写去哪层、以什么最小方式写回”。

---

## 3. 当前字段

当前 `MemoryWriteBackRequestV0` 包含以下字段：

- `write_back_version`
- `write_back_id`
- `subject_id`
- `write_back_reason`
- `target_memory_layer`
- `source_evidence_refs`
- `write_back_mode`
- `trace`

---

## 4. 字段原则

### write_back_version

当前对象 contract 版本。固定值：

- `memory_writeback_request_v0`

### write_back_id

当前写回请求对象的稳定标识。

当前格式：

- `memory-writeback::{write_back_seed}`

### subject_id

当前被写回请求所围绕的主体标识。

### write_back_reason

当前写回请求的最小原因集合。

说明：

该字段用于表达：
- 为什么值得写回
- 当前写回请求属于哪类最小原因

### target_memory_layer

当前拟写入的目标记忆层集合。

当前允许值：

- `hot`
- `warm`
- `cold`
- `posterior`

说明：

写回请求应显式区分写去哪一层，
而不是统称“存起来”。

### source_evidence_refs

当前写回请求所依赖的最小证据引用集合。

### write_back_mode

当前写回模式。

当前允许值：

- `preview_only`
- `structured_posterior_update`

### trace

当前写回请求对象的最小 trace 对象。

当前至少表达：

- `source_stage`
- `write_back_id`
- `subject_id`
- `write_back_mode`
- `target_memory_layer_count`
- `source_evidence_ref_count`

---

## 5. 当前 builder 行为

当前 `build_memory_writeback_request_v0(...)` 的最小行为包括：

- 校验 `write_back_seed` 非空
- 校验 `subject_id` 非空
- 校验 `write_back_mode` 属于允许枚举
- 对 `write_back_reason`、`target_memory_layer`、`source_evidence_refs` 做最小规范化
- 校验 `target_memory_layer` 中每个值都属于允许枚举
- 生成稳定 `write_back_id`
- 生成最小 `trace`
- 返回 `MemoryWriteBackRequestV0`

---

## 6. 非目标

当前对象明确不包含：

- stored_memory_ref
- stored_memory_kind
- write_back_status
- retention_hint
- execution payload
- worker target
- queue name
- dispatch plan
- backend mutation intent

也就是说：

> `MemoryWriteBackRequestV0` 当前只表达最小写回请求语义，
> 不表达已完成写回记录，也不表达 executable plan。

---

## 7. 与后续 richer MMN objects 的关系

当前对象不应被误解为：

- `MemoryWriteBackRecord`
- `PosteriorMemoryObject`

更准确地说：

> `MemoryWriteBackRequestV0` 是当前 `aiant-mmn` 在 preview-only / non-executing 阶段，
> 为 MMN 写回能力提供的最小请求对象壳。

---

## 8. 当前阶段的一句话总结

可以用下面这句话概括当前对象：

> `MemoryWriteBackRequestV0` 是 `aiant-mmn` 当前阶段的最小记忆写回请求对象，
> 用于稳定表达“当前哪些内容值得写回、拟写去哪层、以什么最小方式写回”。