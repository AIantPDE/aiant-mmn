# PANT_ROUTE_PREVIEW_SEAM_V0

## 1. 目标

`aiant-mmn` 当前通过最小 adapter seam 面向 `aiant-pant` 提供 memory preview input。

当前目标不是直接控制 route，更不是生成 execution payload，
而是为 `aiant-pant` 的 route-owned `[5]` preview family 提供最小但非空的记忆语义输入。

---

## 2. 当前 seam 原则

当前适配原则：

- contract-first
- preview-only
- deterministic mapping
- fail-closed
- forbidden execution fields blocked
- route ownership remains in `aiant-pant`

---

## 3. 当前 adapter 做什么

当前 adapter 只做以下工作：

- 检查输入是否为支持的 memory output version
- 检查最小必需字段是否存在
- 阻断 execution-like 字段
- 将 memory preview output 映射为 pant route memory input
- 传播最小 trace

---

## 4. 当前 adapter 不做什么

当前 adapter 不做：

- route decision
- dispatch planning
- worker binding
- execution object generation
- backend side effect planning

---

## 5. fail-closed 原则

当前 seam 必须 fail-closed。

典型表现为：

- 遇到不支持的 version -> 拒绝
- 缺少关键字段 -> 拒绝
- 出现 execution-like 字段 -> 拒绝
- 输入 shape 不明确 -> 拒绝
