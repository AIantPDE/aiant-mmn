# MEMORY_WRITEBACK_RECORD_V0

## 1. 目标

`memory_writeback_record_v0` 是 `aiant-mmn` 当前阶段的最小记忆写回记录对象。

它的目标不是表达完整 MMN 写回系统中的持久化总账，
也不是表达完整长期记忆层已经实现的 backend receipt，
而是表达一个最小但非空、稳定、可测试、可被下游 preview-only 消费的 memory write-back record object。

一句话概括：

> `MemoryWriteBackRecordV0` 用于表达“这次写回最终沉淀成了什么最小记录对象”。

---

## 2. 当前定位

在当前 `aiant-mmn` 语境里：

- `historical_comparison_object_v0` 负责表达当前对象与历史对象之间的最小对照关系
- `posterior_correction_object_v0` 负责表达当前对象应如何被最小修正
- `memory_writeback_request_v0` 负责表达当前哪些内容值得被写回、拟写去哪层、以什么最小方式写回
- `memory_writeback_record_v0` 负责表达该写回申请在最小治理后最终沉淀成了什么最小记录对象
- 该对象当前仍处于 preview-only / non-executing 阶段

也就是说：

> `MemoryWriteBackRecordV0` 当前回答的不是“如何执行写回”，
> 而是“这次写回最终形成了什么最小记录”。

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

说明：

该字段用于表达当前写回记录对象自身的稳定 identity，
而不是表达 backend task id 或数据库 transaction id。

---

### stored_memory_ref

当前写回最终沉淀出的最小记忆引用标识。

说明：

该字段用于表达：

- 当前写回结果最终指向了哪条最小 memory ref
- 当前最小记录对象如何被后续 preview / recall-facing 消费面引用

它当前不是正式 backend 主键，
而是最小 memory record reference。

---

### stored_memory_layer

当前写回最终沉淀到的目标记忆层。

当前允许值：

- `hot`
- `warm`
- `cold`
- `posterior`

说明：

该字段用于表达最终沉淀在哪一层，
而不是统称“已经存起来”。

---

### stored_memory_kind

当前写回最终形成的最小记忆种类。

说明：

该字段用于表达这次写回沉淀出的对象属于哪一类最小 memory kind。

例如可以是：

- `preview_memory_note`
- `propagation_realization_correction`
- `posterior_memory_note`
- `historical_failure_note`

当前阶段不要求穷举完整 kind taxonomy，
但要求它至少能表达“这次最终形成了什么类型的最小记录对象”。

---

### write_back_status

当前写回记录状态。

当前允许值建议保持最小集合，例如：

- `stored`
- `deferred`
- `discarded`

说明：

该字段用于表达：

- 当前写回申请最终是否形成了记录
- 若未形成正式沉淀，是延后还是放弃

它当前不是后台执行状态机，
而是最小结果状态。

---

### retention_hint

当前写回记录的最小保留提示。

当前允许值建议保持最小集合，例如：

- `short_term`
- `mid_term`
- `long_term`

说明：

该字段不是完整 retention governance，
而只是最小保留倾向提示。

---

### write_back_notes

当前写回记录的最小说明文本。

说明：

该字段用于表达：

- 这次写回最后沉淀成了怎样的最小经验说明
- 当前记录为什么值得被留下
- 当前记录如何被后续观察面快速理解

它当前不是完整 memory content object，
而是最小说明文本面。

---

### trace

当前写回记录对象的最小 trace 对象。

当前至少表达：

- `source_stage`
- `write_back_id`
- `stored_memory_ref`
- `stored_memory_layer`
- `write_back_status`

说明：

`trace` 当前的目标不是表达完整 lineage graph，
而是保证：

- 当前写回记录对象的最小来源清楚
- 当前记录引用清楚
- 当前沉淀层级清楚
- 当前状态清楚

---

## 5. 当前 builder 行为

当前 `build_memory_writeback_record_v0(...)` 的最小行为包括：

- 校验 `write_back_seed` 非空
- 校验 `stored_memory_ref` 非空
- 校验 `stored_memory_layer` 属于允许枚举
- 校验 `write_back_status` 属于允许枚举
- 校验 `retention_hint` 属于允许枚举
- 对 `stored_memory_kind`、`write_back_notes` 做最小规范化
- 生成稳定 `write_back_id`
- 生成最小 `trace`
- 返回 `MemoryWriteBackRecordV0`

也就是说：

> 当前 builder 的目标是稳定构造最小 write-back record object，
> 而不是引入更重的 persistence orchestration。

---

## 6. 非目标

当前对象明确不包含：

- execution payload
- worker target
- queue name
- dispatch plan
- backend mutation command
- database transaction receipt
- full retention policy
- full writeback governance state machine
- full audit ledger
- complete persistence ownership

也就是说：

> `MemoryWriteBackRecordV0` 当前只表达最小写回结果记录语义，
> 不表达 executable write-back plan，也不表达完整 backend persistence system。

---

## 7. 与 `MemoryWriteBackRequestV0` 的关系

当前至少应显式区分：

- `MemoryWriteBackRequestV0`
- `MemoryWriteBackRecordV0`

二者不是同一层。

更准确地说：

- `MemoryWriteBackRequestV0` 回答  
  “当前哪些内容值得申请写回、拟写去哪层、以什么最小方式写回”

- `MemoryWriteBackRecordV0` 回答  
  “该写回申请在最小治理后，最终沉淀成了什么最小记录对象”

因此：

> `MemoryWriteBackRequestV0` 更偏请求语义，
> `MemoryWriteBackRecordV0` 更偏结果记录语义。

---

## 8. 与后续 richer MMN objects 的关系

当前对象不应被误解为：

- 完整 posterior memory ledger
- 完整长期记忆主存对象
- 完整 retention-governed persistence receipt

更准确地说：

> `MemoryWriteBackRecordV0` 是当前 `aiant-mmn` 在 preview-only / non-executing 阶段，
> 为 MMN 写回能力提供的最小记录对象壳。

---

## 9. 与时间序列 write-back 纪律的关系

当前对象只定义最小 write-back record contract，
并不单独完成时间序列中的 write-back 治理解释。

尤其需要继续保持清楚的是：

- 当前对象不等于 backend persistence receipt
- 当前对象不意味着“到某个固定天数自动生成记录”
- 当前对象只表达：
  - 当前写回申请最终是否形成了记录
  - 最终沉淀到了哪一层
  - 最终形成了哪类最小 memory record

关于当前 `MemoryWriteBackRecordV0` 在时间序列语境中的最小纪律解释，
请继续参见：

- `MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0.md`

该文档会进一步说明：

- 为什么 `write-back` 不应按固定日历时间定义
- 什么才算新的独立事件实例
- 什么才算 outcome horizon 已闭合
- 在什么条件下 record 更适合形成

---

## 10. 当前阶段的一句话总结

可以用下面这句话概括当前对象：

> `MemoryWriteBackRecordV0` 是 `aiant-mmn` 当前阶段的最小记忆写回记录对象，
> 用于稳定表达“这次写回最终沉淀成了什么最小记录对象”。