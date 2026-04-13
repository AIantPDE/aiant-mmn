# README_DOC_CHAIN_V0

时间：2026年4月13日

## 1. 目的

本文档用于说明 `aiant-mmn/docs/` 当前各文档的分工与推荐阅读顺序。

当前目标不是把 MMN 一次性定义成完整记忆系统，
而是先把：

- 仓定位
- 设计理由
- 对象族
- 当前最小 preview object
- 与 `aiant-pant` 的 seam
- 最小流向示例
- 当前阶段的 checkpoint / handoff
- write-back 的时间序列纪律
- fixture / golden regression 的冻结策略

串成一条清楚的文档链。

---

## 2. 当前文档分工

### `ARCHITECTURE_OVERVIEW.md`

回答：

```text
aiant-mmn 当前在 AIant PDE 中处于什么位置
```

重点包括：

- 当前仓定位
- 当前最小分层
- preview-only / non-executing 边界
- 与 `aiant-pant` 的最小 memory seam 关系
- 当前已落地的最小正向宿主链
- 当前已落地的最小 MMN 本体对象链

---

### `MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md`

回答：

```text
为什么 MMN 不应只被理解为 memory bank 或 recall helper
```

重点包括：

- 记忆分层
- recall 治理
- 历史对照
- posterior correction
- 写回纪律

---

### `MMN_OBJECT_FAMILY_V0.md`

回答：

```text
如果把 MMN 对象化，最小对象族应如何划分
```

重点包括：

- hot / warm / cold / posterior memory objects
- recall objects
- historical comparison object
- posterior correction object
- write-back objects

---

### `MEMORY_RECORD_V0.md`

回答：

```text
当前 preview output 中的最小记录级 contract object 是什么
```

重点包括：

- `MemoryRecordV0` 当前字段
- record-level identity / trace / reason visibility
- preview record semantics 边界
- 与 `MemoryPreviewOutputV0.records` 的关系

---

### `MEMORY_PREVIEW_OUTPUT_V0.md`

回答：

```text
当前阶段已经落到 contract-facing 的最小 memory preview object 是什么
```

重点包括：

- `memory_preview_output_v0` 当前字段
- 最小枚举
- 非目标
- preview semantics 边界

---

### `ROUTE_PREVIEW_MEMORY_SEAM_V0.md`

回答：

```text
当前 memory preview output 如何通过 adapter seam 接入 aiant-pant
```

重点包括：

- contract-first
- preview-only
- deterministic mapping
- fail-closed
- route ownership remains in aiant-pant

---

### `MMN_MINIMAL_FLOW_EXAMPLE_V0.md`

回答：

```text
一条最小对象链如何从 recall 走到 comparison、correction 与 write-back
```

重点包括：

- `MemoryRecallRequest`
- `MemoryRecallResult`
- `HistoricalComparisonObject`
- `PosteriorCorrectionObject`
- `MemoryWriteBackRequest`
- `MemoryWriteBackRecord`

---

## 3. 阶段性 checkpoint / write-back / fixture 文档

当阅读者已经理解当前仓的最小 memory host、preview output / record 层与最小 MMN 本体对象族后，建议继续进入本组文档。

本组文档的目标不是继续扩张 object shell，
而是对当前阶段已经 landed 的最小结构边界、时间序列中的 write-back 理解，以及 fixture / golden test 的冻结策略做正式收口。

### `MMN_ARCHITECTURE_CHECKPOINT_V0.md`

回答：

```text
当前 aiant-mmn 在本阶段到底是什么
```

重点包括：

- 当前仓为什么应理解为：
  - minimal memory-semantic producer host
  - minimal MMN object host
-当前哪些对象 / 链路已经 landed
-当前哪些部分仍只是 preview-only shell
-为什么当前阶段更适合先做 checkpoint 固化，而不是继续无边界扩 object shell

### `MMN_HANDOFF_CHECKPOINT_V0.md`

回答：

```text
当前阶段如何向新 chat / 新工作面交接
```

重点包括：

- 当前哪些内容已足够稳定
- 当前哪些内容仍需谨慎理解
- 下一步默认应继续做什么
- 下一步默认不应继续做什么

### `MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0.md`

回答：

```text
为什么 write-back 不应按固定日历时间定义
```

重点包括：

- `MemoryWriteBackRequestV0` 与 `MemoryWriteBackRecordV0` 当前分别表达什么
- 为什么“再次出现”不能简单按自然日间隔定义
- 为什么应按：
  - 新的独立事件实例
  - 可比较结构模式
  - outcome horizon 已闭合
    来理解 write-back 触发语义

### `MMN_FIXTURE_STRATEGY_V0.md`

回答：

```text
为什么当前阶段优先冻结 preview output / record 层与最小 MMN object chain 层
```

重点包括：

- 当前 golden fixtures 属于什么层级
- 当前 golden tests 主要防止哪些边界漂移
- 为什么当前默认不继续无边界冻结 richer MMN semantics

---

## 4. 推荐阅读顺序

若阅读者希望从总体架构一路读到当前阶段的收口文档，
建议阅读顺序如下：

```text
ARCHITECTURE_OVERVIEW
  -> MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0
  -> MMN_OBJECT_FAMILY_V0
  -> MEMORY_RECORD_V0
  -> MEMORY_PREVIEW_OUTPUT_V0
  -> ROUTE_PREVIEW_MEMORY_SEAM_V0
  -> MMN_MINIMAL_FLOW_EXAMPLE_V0
  -> MMN_ARCHITECTURE_CHECKPOINT_V0
  -> MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0
  -> MMN_FIXTURE_STRATEGY_V0
  -> MMN_HANDOFF_CHECKPOINT_V0
```

---

## 5. 当前阶段最短阅读路径

若阅读者只想快速理解本轮新增文档的作用，
建议最短路径为：

```text
MMN_ARCHITECTURE_CHECKPOINT_V0
  -> MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0
  -> MMN_FIXTURE_STRATEGY_V0
  -> MMN_HANDOFF_CHECKPOINT_V0
```

若阅读者希望连同 preview output / record 层与 object family 一并理解，
建议路径为：

```text
MEMORY_PREVIEW_OUTPUT_V0
  -> MEMORY_RECORD_V0
  -> MMN_OBJECT_FAMILY_V0
  -> MMN_MINIMAL_FLOW_EXAMPLE_V0
  -> MMN_ARCHITECTURE_CHECKPOINT_V0
  -> MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0
  -> MMN_FIXTURE_STRATEGY_V0
  -> MMN_HANDOFF_CHECKPOINT_V0
```

---

## 6. 当前阶段的一句话总结

当前 aiant-mmn 的文档链应先回答：

```text
这个仓是什么
-> 为什么 MMN 应这样设计
-> MMN 至少有哪些对象
-> 当前已经落到哪一个 preview object / record layer
-> 这个 object 如何接入 pant
-> 最小对象链如何走到 comparison / correction / write-back
-> 当前阶段为什么先做 checkpoint / handoff / write-back discipline / fixture freeze
```
