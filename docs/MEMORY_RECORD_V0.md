# MEMORY_RECORD_V0

## 1. 目标

`memory_record_v0` 是 `aiant-mmn` 当前阶段的最小记忆记录对象。

它的目标不是表达完整长期记忆系统中的所有记忆单元，
也不是表达 execution intent，
而是表达一个最小但非空、稳定、可测试、可被 `memory_preview_output_v0` 承载的 memory record。

一句话概括：

> `MemoryRecordV0` 是当前 `aiant-mmn` 最小 memory preview object 中的记录级基本单元。

---

## 2. 当前定位

在当前 `aiant-mmn` 语境里：

- `memory_preview_output_v0` 是最小记忆预览对象
- `records` 是其中的最小记录集合
- `MemoryRecordV0` 则是 `records` 的成员类型

也就是说：

> `MemoryPreviewOutputV0` 负责表达“当前记忆预览输出是什么”，  
> `MemoryRecordV0` 负责表达“这次预览输出里包含哪些最小记录单元”。

---

## 3. 当前字段

当前 `MemoryRecordV0` 包含以下字段：

- `record_version`
- `record_id`
- `record_kind`
- `record_text`
- `reason_codes`
- `trace`

---

## 4. 字段原则

### record_version
当前对象 contract 版本。固定值：

- `memory_record_v0`

说明：

该字段用于表达当前记录对象所遵循的最小版本边界。

---

### record_id
当前记录对象的稳定标识。

当前格式：

- `memory-record::{record_seed}`

说明：

`record_id` 的作用不是表达业务执行身份，
而是表达：

- 当前记忆记录对象是谁
- 当前记录如何被 trace / preview / recall-facing 消费面稳定引用
- 当前记录如何在最小 preview object 内保持 identity-like 可见性

一句话概括：

> `record_id` 是当前最小 memory record 的稳定记录标识。

---

### record_kind
当前记录对象的记录类型。

当前允许值：

- `evidence_note`
- `summary_note`
- `trace_note`
- `citation_note`

说明：

该字段用于表达当前记录在 preview memory 语义中的最小功能角色。

例如：

- `evidence_note`：偏证据提示
- `summary_note`：偏摘要提示
- `trace_note`：偏来源/追踪提示
- `citation_note`：偏引用说明提示

一句话概括：

> `record_kind` 决定当前 memory record 属于哪种最小记录角色。

---

### record_text
当前记录对象的最小文本内容。

说明：

该字段用于表达当前 record 最小但非空的内容本体。  
它不是完整长期记忆库中的 rich content object，
而是当前 preview memory surface 上最小可读文本内容。

设计要求：

- 必须为非空字符串
- 当前阶段应保持简短、可测试、可稳定消费
- 不预先扩张为复杂内容 schema

一句话概括：

> `record_text` 是当前 memory record 的最小文本内容面。

---

### reason_codes
当前记录对象的最小原因码集合。

说明：

用于解释：

- 当前 record 为什么存在
- 当前 record 为什么被纳入 preview output
- 当前 record 属于哪类最小 memory signal

该字段当前仍保持最小原因码集合设计，
不扩张为更复杂的 reason graph / justification graph。

---

### trace
当前记录对象的最小 trace 对象。

当前至少表达：

- `source_stage`
- `record_id`
- `record_kind`
- `record_text`
- `reason_codes`

说明：

`trace` 当前的目标不是表达完整 lineage graph，
而是保证：

- 来源清楚
- 最小 identity 清楚
- 最小消费面可追踪
- 对 downstream 观察面保持足够透明

一句话概括：

> `trace` 是当前 memory record 的最小来源与关键字段追踪对象。

---

## 5. 当前 builder 行为

当前 `build_memory_record_v0(...)` 的最小行为包括：

- 校验 `record_seed` 非空
- 校验 `record_kind` 属于允许枚举
- 校验 `record_text` 非空
- 对 `reason_codes` 做最小规范化
- 生成稳定 `record_id`
- 生成最小 `trace`
- 返回 `MemoryRecordV0`

也就是说：

> 当前 builder 的目标是稳定构造最小 record object，  
> 而不是引入更重的记忆编排逻辑。

---

## 6. 当前支持的最小枚举

### record_kind

当前支持以下最小枚举值：

- `evidence_note`
- `summary_note`
- `trace_note`
- `citation_note`

这些枚举值的目标不是穷尽未来所有记忆类型，
而是先为 preview-only memory surface 固定最小记录角色。

---

## 7. 非目标

当前对象明确不包含：

- execution payload
- worker target
- queue name
- dispatch plan
- backend mutation intent
- long-term storage policy
- retrieval ranking score
- posterior correction strength
- write-back governance rule

也就是说：

> `MemoryRecordV0` 当前只表达最小 preview record semantics，  
> 不表达 executable plan，也不承担完整 MMN memory governance。

---

## 8. 与 `memory_preview_output_v0` 的关系

`MemoryRecordV0` 当前不独立承担完整 memory output 语义，
而是作为：

- `memory_preview_output_v0.records`

中的成员对象存在。

因此：

- `memory_preview_output_v0` 回答“这次 memory preview 输出整体是什么”
- `MemoryRecordV0` 回答“这次输出里具体有哪些最小记录”

可以先用下面的关系理解：

```text id="c8r0o8"
MemoryPreviewOutputV0
    └─ records
        ├─ MemoryRecordV0
        ├─ MemoryRecordV0
        └─ ...
```

---

## 9. 与更完整 MMN 的关系

当前 `MemoryRecordV0` 不应被误解为：

* 完整长期记忆单元
* 完整 recall object
* 完整 posterior memory object
* 完整 write-back object

更准确地说：

> `MemoryRecordV0` 是当前 `aiant-mmn` 在 preview-only / non-executing 阶段，
> 为最小 memory preview output 提供的记录级 contract object。

未来若 `aiant-mmn` 继续推进 richer MMN semantics，
可能会进一步出现：

* richer recall-facing records
* historical comparison objects
* posterior correction objects
* memory write-back objects

但这些都不应提前塞进当前 `MemoryRecordV0`。

---

## 10. 当前阶段的一句话总结

可以用下面这句话概括当前对象：

> `MemoryRecordV0` 是 `aiant-mmn` 当前阶段的最小记忆记录对象，
> 它以 `record_version / record_id / record_kind / record_text / reason_codes / trace`
> 构成最小但非空、稳定、可测试、可被 `memory_preview_output_v0` 承载的记录级 preview surface。
