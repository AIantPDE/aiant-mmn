# README_DOC_CHAIN_V0

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

串成一条清楚的文档链。

---

## 2. 当前文档分工

### `ARCHITECTURE_OVERVIEW.md`

回答：

```text
aiant-mmn 当前在 AIant PDE 中处于什么位置
````

重点包括：

* 当前仓定位
* 当前最小分层
* preview-only / non-executing 边界
* 与 `aiant-pant` 的最小 memory seam 关系

---

### `MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md`

回答：

```text
为什么 MMN 不应只被理解为 memory bank 或 recall helper
```

重点包括：

* 记忆分层
* recall 治理
* 历史对照
* posterior correction
* 写回纪律

---

### `MMN_OBJECT_FAMILY_V0.md`

回答：

```text
如果把 MMN 对象化，最小对象族应如何划分
```

重点包括：

* hot / warm / cold / posterior memory objects
* recall objects
* historical comparison object
* posterior correction object
* write-back objects

---

### `MEMORY_PREVIEW_OUTPUT_V0.md`

回答：

```text
当前阶段已经落到 contract-facing 的最小 memory preview object 是什么
```

重点包括：

* `memory_preview_output_v0` 当前字段
* 最小枚举
* 非目标
* preview semantics 边界

---

### `ROUTE_PREVIEW_MEMORY_SEAM_V0.md`

回答：

```text
当前 memory preview output 如何通过 adapter seam 接入 aiant-pant
```

重点包括：

* contract-first
* preview-only
* deterministic mapping
* fail-closed
* route ownership remains in `aiant-pant`

---

### `MMN_MINIMAL_FLOW_EXAMPLE_V0.md`

回答：

```text
一条最小对象链如何从 recall 走到 comparison、correction 与 write-back
```

重点包括：

* `MemoryRecallRequest`
* `MemoryRecallResult`
* `HistoricalComparisonObject`
* `PosteriorCorrectionObject`
* `MemoryWriteBackRequest`
* `MemoryWriteBackRecord`

---

## 3. 推荐阅读顺序

```text
ARCHITECTURE_OVERVIEW
  -> MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0
  -> MMN_OBJECT_FAMILY_V0
  -> MEMORY_RECORD_V0
  -> MEMORY_PREVIEW_OUTPUT_V0
  -> ROUTE_PREVIEW_MEMORY_SEAM_V0.md
  -> MMN_MINIMAL_FLOW_EXAMPLE_V0
```

---

## 4. 当前阶段的一句话总结

当前 `aiant-mmn` 的文档链应先回答：

```text
这个仓是什么
-> 为什么 MMN 应这样设计
-> MMN 至少有哪些对象
-> 当前已经落到哪一个 preview object
-> 这个 object 如何接入 pant
-> 这条链未来如何向 recall / comparison / correction / write-back 扩展
```
