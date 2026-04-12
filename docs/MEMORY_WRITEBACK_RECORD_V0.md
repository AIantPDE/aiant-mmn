# MEMORY_WRITEBACK_RECORD_V0

## 1. 目标

`memory_writeback_record_v0` 是 `aiant-mmn` 当前阶段的最小记忆写回记录对象。

它的目标不是表达完整 MMN 写回治理系统，
也不是表达完整 posterior memory object，
而是表达一个最小但非空、稳定、可测试、可被下游 preview-only 消费的 memory write-back record object。

一句话概括：

> `MemoryWriteBackRecordV0` 用于表达“这次写回最终沉淀成了什么最小记录对象”。

---

## 2. 当前定位

在当前 `aiant-mmn` 语境里：

- `memory_writeback_request_v0` 负责表达当前哪些内容值得写回记忆层
- `memory_writeback_record_v0` 负责表达这次写回最终沉淀成了什么最小记录对象
- 该对象当前仍处于 preview-only / non-executing 阶段

也就是说：

> `MemoryWriteBackRecordV0` 当前回答的不是“写回请求为什么存在”，
> 而是“这次写回最终形成了什么最小沉淀记录”。

---

## 3. 当前字段

当前 `MemoryWriteBackRecordV0` 包含以下字段：

- `write_back_version`
- `write_back_id`
- `stored_memory_ref`
- `stored_memory_layer`
- `stored_memory_kind`
- `write_back_status`
- `retention_hint`
- `write_back_notes`
- `trace`

---

## 4. 字段原则

### write_back_version

当前对象 contract 版本。固定值：

- `memory_writeback_record_v0`

### write_back_id

当前写回记录对象的稳定标识。

当前格式：

- `memory-writeback-record::{write_back_seed}`

### stored_memory_ref

当前写回最终形成的最小记忆引用标识。

### stored_memory_layer

当前写回最终沉淀到的记忆层。

当前允许值：

- `hot`
- `warm`
- `cold`
- `posterior`

### stored_memory_kind

当前写回最终形成的最小记忆类型。

说明：

该字段当前保持为最小非空字符串，
不提前扩张为更复杂的 kind taxonomy。

### write_back_status

当前写回记录状态。

当前允许值：

- `stored`
- `skipped`
- `deferred`

### retention_hint

当前写回记录的最小保留提示。

当前允许值：

- `short_term`
- `medium_term`
- `long_term`

### write_back_notes

当前写回记录的最小说明文本。

### trace

当前写回记录对象的最小 trace 对象。

当前至少表达：

- `source_stage`
- `write_back_id`
- `stored_memory_ref`
- `stored_memory_layer`
- `write_back_status`

---

## 5. 当前 builder 行为

当前 `build_memory_writeback_record_v0(...)` 的最小行为包括：

- 校验 `write_back_seed` 非空
- 校验 `stored_memory_ref` 非空
- 校验 `stored_memory_layer` 属于允许枚举
- 校验 `stored_memory_kind` 非空
- 校验 `write_back_status` 属于允许枚举
- 校验 `retention_hint` 属于允许枚举
- 生成稳定 `write_back_id`
- 生成最小 `trace`
- 返回 `MemoryWriteBackRecordV0`

---

## 6. 非目标

当前对象明确不包含：

- write-back request reason graph
- execution payload
- worker target
- queue name
- dispatch plan
- backend mutation intent
- richer posterior governance fields

也就是说：

> `MemoryWriteBackRecordV0` 当前只表达最小写回结果记录语义，
> 不表达 executable plan，也不表达完整写回治理。

---

## 7. 与后续 richer MMN objects 的关系

当前对象不应被误解为：

- 完整 posterior memory object
- 完整 retention governance object

更准确地说：

> `MemoryWriteBackRecordV0` 是当前 `aiant-mmn` 在 preview-only / non-executing 阶段，
> 为 MMN 写回结果层提供的最小记录对象壳。

---

## 8. 当前阶段的一句话总结

可以用下面这句话概括当前对象：

> `MemoryWriteBackRecordV0` 是 `aiant-mmn` 当前阶段的最小记忆写回记录对象，
> 用于稳定表达“这次写回最终沉淀成了什么最小记录对象”。