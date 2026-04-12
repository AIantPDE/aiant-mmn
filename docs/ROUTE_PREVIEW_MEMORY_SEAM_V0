# ROUTE_PREVIEW_MEMORY_SEAM_V0

时间： 2026年4月12日

## 1. 目标

`aiant-mmn` 当前通过最小 adapter seam 提供 preview-facing memory semantic input。

当前目标不是直接控制 route，更不是生成 execution payload，
而是先为当前 preview-only consumer chain 提供最小但非空的记忆语义输入。

需要特别强调的是：

- 该 seam 当前可以被 route-facing preview chain 消费
- 但这不应被解释为 `MMN` 在 AIant PDE 中以某一个 consumer 仓作为本体归属
- `MMN` 的系统角色仍以 AIant PDE 总分层中 `[5]` 与 `[6]` 的定义为准

---

## 2. 当前 seam 原则

当前适配原则：

- contract-first
- preview-only
- deterministic mapping
- fail-closed
- forbidden execution fields blocked
- seam is consumer-facing, not ownership-defining

---

## 3. 当前 adapter 做什么

当前 adapter 只做以下工作：

- 检查输入是否为支持的 memory output version
- 检查最小必需字段是否存在
- 阻断 execution-like 字段
- 将 memory preview output 映射为 preview-facing memory semantic input
- 传播最小 trace

---

## 4. 当前 adapter 不做什么

当前 adapter 不做：

- route decision
- dispatch planning
- worker binding
- execution object generation
- backend side effect planning
- 定义 MMN 的系统归属
- 把单一下游 consumer 上升为 MMN 的本体定位

---

## 5. fail-closed 原则

当前 seam 必须 fail-closed。

典型表现为：

- 遇到不支持的 version -> 拒绝
- 缺少关键字段 -> 拒绝
- 出现 execution-like 字段 -> 拒绝
- 输入 shape 不明确 -> 拒绝

---

## 相关文档

若需理解当前 seam 的上游 MMN 设计背景与对象族，请参见：

- `ARCHITECTURE_OVERVIEW.md`
- `MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md`
- `MMN_OBJECT_FAMILY_V0.md`
- `MEMORY_PREVIEW_OUTPUT_V0.md`
- `MMN_MINIMAL_FLOW_EXAMPLE_V0.md`