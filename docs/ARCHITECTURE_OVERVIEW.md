# ARCHITECTURE_OVERVIEW

时间：2026年4月12日
  
`aiant-mmn` 当前阶段是 AIant-PDE 的最小记忆语义输出仓库。

它当前不是完整记忆系统，而是最小 memory-semantic producer host，用于：

- 固定最小 memory preview output shape
- 提供最小 memory stub provider
- 提供最小 recall / citation stub
- 为未来 richer MMN semantics 预留稳定 memory-semantic seam

当前边界：

- preview-only
- non-executing
- no worker coupling
- no formal execution payload
- deterministic output shape
- fail-closed integration

---

## 当前最小分层

### contracts
定义最小 memory preview output contract 与 memory record contract。

### providers
提供最小 memory preview producer。当前仅提供 stub provider，用于输出稳定、可测试的最小 preview object。

### recall
提供最小 recall / citation stub。当前只表达离线 recall preference，不表达执行性召回动作。

### adapters
提供最小 preview-facing adapter seam。当前只做 contract-preserving adaptation，不做策略控制权判断，也不把单一下游 consumer 预设为 MMN 的本体归属。

### tests
验证 shape 稳定、provider 稳定、recall 稳定、adapter fail-closed，以及最小正向宿主链的冒烟闭环。

---

## 当前已落地的最小正向宿主链

当前 `aiant-mmn` 已实际落地的最小正向链为：

```text
MemoryStubProviderV0
  -> MemoryPreviewOutputV0
  -> recall_stub_v0
  -> route_preview_memory_adapter_v0
```

该链当前只用于证明：

- 最小 memory preview output 可被稳定生成
- 最小 recall stub 可基于 preview output 形成
- 最小 preview-facing memory semantic input 可由 adapter seam 稳定映射
- 全链路保持 preview-only / non-executing / deterministic / fail-closed 边界

这意味着当前 `aiant-mmn` 已经不仅具备：

- 对象层
- provider 层
- seam 层

还具备一条最小但真实存在的正向宿主链，
可用于证明当前 memory-semantic producer host 不是抽象概念，
而是已经形成：

```text
provider
  -> preview object
  -> recall stub
  -> preview-facing memory input
```

的一条可测试最小闭环。

需要特别强调的是：

- 该链当前仍然是 preview-only
- 不拥有 route decision
- 不生成 execution payload
- 不耦合 worker
- 不引入 backend side effects

因此，它的意义不是“记忆系统已完整”，
而是：

> `aiant-mmn` 当前阶段已经具备一个最小、可测试、可约束的 memory host 正向闭环，
可作为后续 richer memory semantics 扩展的 contract-preserving 起点。

---

## 当前已落地的最小 MMN 本体对象链

在最小正向宿主链之外，`aiant-mmn` 当前还已经落地了一条最小 MMN 本体对象链：

```text
HistoricalComparisonObjectV0
  -> PosteriorCorrectionObjectV0
  -> MemoryWriteBackRequestV0
  -> MemoryWriteBackRecordV0
```

该链当前只用于证明：

- `HistoricalComparisonObjectV0` 可以稳定表达当前对象与历史对象之间的最小对照关系
- `PosteriorCorrectionObjectV0` 可以稳定表达基于这些对照关系的最小修正方向与强度
- `MemoryWriteBackRequestV0` 可以稳定表达哪些内容值得写回、拟写去哪层、以什么最小方式写回
- `MemoryWriteBackRecordV0` 可以稳定表达这次写回最终沉淀成了什么最小记录对象
- 全链路仍保持 preview-only / non-executing / deterministic / contract-first 边界

这意味着当前 `aiant-mmn` 已经不仅拥有：

- 最小 memory preview host
- 最小 recall-facing seam
- 最小 preview-facing adapter seam

还开始拥有一组真正属于 MMN 本体职责范围内的对象族壳。

可以先用下面这条链理解：

```text
historical comparison
  -> posterior correction
  -> writeback request
  -> writeback record
```

需要特别强调的是：

- 该链当前仍然不是完整 MMN 系统
- 它不表达完整 posterior governance
- 不表达完整 retention governance
- 不表达完整长期记忆系统
- 不表达 executable write-back plan

因此，它的意义不是“MMN 已经完整”，
而是：

> `aiant-mmn` 当前阶段已经不再只是一个最小 memory host，
而是开始具备一条最小但真实存在的 MMN 本体对象链，
可作为后续 richer recall / comparison / correction / write-back semantics 的 contract-preserving 起点。

---

## 相关文档

当前更细的 MMN 设计说明，请继续参见：

- `MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md`
- `MMN_OBJECT_FAMILY_V0.md`
- `MEMORY_PREVIEW_OUTPUT_V0.md`
- `ROUTE_PREVIEW_MEMORY_SEAM_V0.md`
- `MMN_MINIMAL_FLOW_EXAMPLE_V0.md`

> 这版增补做的事很克制：把 pant 从“MMN 的归属解释”里拿掉，只保留“preview-facing seam”这个中性层次。没有改现有概览文档的定位、最小分层和正向宿主链，只是额外增加一个“当前已落地的最小 MMN 本体对象链”小节，把最近一连串落地的 contract object 收成一个可读的架构结论。它和当前文档里 **“preview-only / non-executing / deterministic / fail-closed”** 的边界完全一致。