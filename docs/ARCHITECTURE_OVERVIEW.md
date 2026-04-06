# ARCHITECTURE_OVERVIEW

`aiant-mmn` 当前阶段是 AIant-PDE 的最小记忆语义输出仓库。

它当前不是完整记忆系统，而是最小 memory-semantic producer host，用于：

- 固定最小 memory preview output shape
- 提供最小 memory stub provider
- 提供最小 recall / citation stub
- 为 `aiant-pant` 的 route-owned `[5]` preview family 预留稳定 memory seam

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
提供面向 `aiant-pant` 的最小 route preview seam。当前只做 contract-preserving adaptation，不做 route decision。

### tests
验证 shape 稳定、provider 稳定、recall 稳定、adapter fail-closed。

---

## 相关文档

当前更细的 MMN 设计说明，请继续参见：

- `MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md`
- `MMN_OBJECT_FAMILY_V0.md`
- `MEMORY_PREVIEW_OUTPUT_V0.md`
- `PANT_ROUTE_PREVIEW_SEAM_V0.md`
- `MMN_MINIMAL_FLOW_EXAMPLE_V0.md`