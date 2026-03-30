# MEMORY_PREVIEW_OUTPUT_V0

## 1. 目标

`memory_preview_output_v0` 是 `aiant-mmn` 当前阶段的最小记忆预览对象。

它的目标不是表达完整记忆系统结果，
也不是表达 execution intent，
而是表达一个最小但非空、稳定、可测试的 memory preview signal。

---

## 2. 当前字段

- `memory_output_version`
- `memory_output_model_version`
- `memory_output_id`
- `records`
- `memory_strength_hint`
- `citation_hint`
- `reason_codes`
- `trace`

---

## 3. 字段原则

### memory_output_version
当前对象 contract 版本。固定值：

- `memory_preview_output_v0`

### memory_output_model_version
当前 memory producer model family/version 标识。固定值：

- `memory_preview_output_model_v0`

### memory_output_id
当前输出对象的稳定 id。当前格式：

- `memory-preview::{output_seed}`

### records
最小记录集合，成员类型为 `MemoryRecordV0`。

### memory_strength_hint
记忆强度提示，允许值：

- `weak`
- `medium`
- `strong`

### citation_hint
引用可用性提示，允许值：

- `none`
- `limited`
- `available`

### reason_codes
最小原因码集合。用于解释当前 memory preview 为何走到当前输出路径。

### trace
最小 trace 对象。当前只要求能明确来源 stage 与关键字段。

---

## 4. 非目标

当前对象明确不包含：

- execution payload
- worker target
- queue name
- db write plan
- dispatch plan
- backend mutation intent

也就是说，该对象当前只表达 preview semantics，不表达 executable plan。

---

## 5. 支持的最小枚举

- `record_kind`: `evidence_note` / `summary_note` / `trace_note` / `citation_note`
- `memory_strength_hint`: `weak` / `medium` / `strong`
- `citation_hint`: `none` / `limited` / `available`
