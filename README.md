# aiant-mmn

时间：2026年4月12日

`aiant-mmn` 是 AIant-PDE 当前阶段的最小记忆语义输出仓库。

当前阶段，它**不是**完整的 MMN 长期记忆 / 全量召回 / 记忆治理引擎；
而是一个 **contract-first / preview-oriented / non-executing** 的 memory-semantic producer host，
用于先固定最小但非空的 memory preview object 与最小 recall-facing / preview-facing 语义边界。

---

## 当前定位

当前阶段的 `aiant-mmn` 负责：

- 固定最小 memory preview output shape
- 提供最小 memory stub provider
- 提供最小 recall / citation stub
- 为未来的 MMN 记忆约束、历史对照、后验修正与回溯语义接入预留稳定接口
- 以 deterministic mapping 的方式输出 preview signal
- 以 fail-closed 的方式阻断 execution-like 字段渗透

当前不负责：

- 完整长期记忆系统
- 全量检索平台
- 复杂 citation governance
- memory serving runtime
- worker 执行耦合
- 正式 execution payload 生成
- queue / db / backend side effects

---

## 当前边界

本仓库当前明确保持以下边界：

- memory preview only
- non-executing
- contract-first
- deterministic output shape
- clear trace
- fail-closed integration
- no worker coupling
- no formal execution payload generation

这意味着 `aiant-mmn` 当前输出的是：

```text
memory semantic preview
```

而不是：
```text
execution instruction
```

---

## 为什么现在启动 aiant-mmn

**AIant PDE** 当前总体进入“双主线并行”阶段。

当前判断是：

`[5] 执行与策略层` 未来不能只沿着 route-owned preview family 做“名字递进”，否则会缺少记忆 / 引用 / 回溯 / posterior correction 约束
MMN 在 AIant PDE 中的本体职责，本来就包括记忆、历史对照、recall、上下文支撑与后验修正
因此需要一个最小但真实存在的 memory-semantic host，先把 MMN 的最小 preview object 与 memory-facing seam 稳定下来

`aiant-mmn` 在当前阶段的目标不是替代其他仓，
也不是提前承担 execution authority，
而是先为未来 richer MMN semantics 提供**稳定**、**可测试**、**可约束**的最小记忆语义宿主位。

---

## 当前最小分层

### contracts

定义最小 memory preview output contract 与 memory record contract。

### providers

提供最小 memory preview producer。当前仅提供 stub provider，用于输出稳定、可测试的最小 preview object。

### recall

提供最小 recall / citation stub。当前只表达离线 recall preference，不表达执行性召回动作。

### adapters

提供最小 preview-facing adapter seam。当前只做 contract-preserving adaptation，不做策略归属判断，也不预设某一个 consumer 仓就是 MMN 的本体归属。

### tests

验证 shape 稳定、provider 稳定、recall 稳定、adapter fail-closed。

---

## 首批最小输出字段

当前 `memory_preview_output_v0` 仅保留最小字段集：

- `memory_output_version`
- `memory_output_model_version`
- `memory_output_id`
- `records`
- `memory_strength_hint`
- `citation_hint`
- `reason_codes`
- `trace`

设计原则：

- 字段克制
- 不提前发明复杂记忆治理语义
- 不预埋 execution object
- 保持最小但非空
- 保持未来可扩展

---

## 与其他仓的关系

`aiant-mmn` 当前不直接控制 route，
也不拥有 execution authority。

它当前的职责是：

- 生成最小 memory preview output
- 通过 preview-facing adapter seam 向下游 consumer 提供可消费的 memory semantic input
- 在 integration 边界上保持 fail-closed

也就是说，当前阶段：

- `aiant-mmn` 负责“产出最小记忆预览语义”
- 下游 consumer 负责“在各自上下文中消费这些 preview semantics”
- `aiant-mmn` 不以任一单独下游仓作为自身的本体归属

---

## 当前设计原则

本仓库当前优先满足以下原则：

### 1. shape 先固定

先固定最小输出 shape，再讨论 richer memory semantics

### 2. preview 与 execution 分层

preview signal 不等于 execution intent

### 3. adapter 是接缝，不是执行器

adapter 只做 contract-preserving mapping，不做策略控制权判断

### 4. 默认拒绝越界

execution-like 字段、worker-like 字段、dispatch-like 字段进入 adapter 时默认阻断

### 5. trace 要简单但清晰

trace 当前只做最小来源追踪，不做复杂 lineage graph

### 6. 先对象壳，再 richer memory semantics

先让 preview object、memory record、recall seam 稳定存在，再继续扩展 historical comparison / posterior correction / memory write-back

---

## 文档导航

当前更细的 MMN 设计说明收口到 `docs/`：

- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md`
- `docs/MMN_OBJECT_FAMILY_V0.md`
- `docs/MEMORY_PREVIEW_OUTPUT_V0.md`
- `docs/ROUTE_PREVIEW_MEMORY_SEAM_V0.md`
- `docs/MMN_MINIMAL_FLOW_EXAMPLE_V0.md`
- `docs/README_DOC_CHAIN_V0.md`

建议阅读顺序：

```text
ARCHITECTURE_OVERVIEW
  -> MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0
  -> MMN_OBJECT_FAMILY_V0
  -> MEMORY_PREVIEW_OUTPUT_V0
  -> ROUTE_PREVIEW_MEMORY_SEAM_V0
  -> MMN_MINIMAL_FLOW_EXAMPLE_V0
```

一句话概括：

- `ARCHITECTURE_OVERVIEW` 说明仓定位与边界
- `MMN_DESIGN_INSIGHTS...` 说明为什么 MMN 不应只被理解为 memory bank / recall helper
- `MMN_OBJECT_FAMILY_V0` 说明当前阶段建议的最小对象族
- `MEMORY_PREVIEW_OUTPUT_V0` 说明当前已经固定下来的 preview object
- `ROUTE_PREVIEW_MEMORY_SEAM_V0` 说明当前最小 preview-facing seam 如何保持 contract-first / preview-only / fail-closed
- `MMN_MINIMAL_FLOW_EXAMPLE_V0` 说明 recall -> comparison -> correction -> write-back 的最小链条

---

## 目录结构

```text
aiant-mmn/
├─ README.md
├─ pyproject.toml
├─ .gitignore
├─ .vscode/
│  ├─ extensions.json
│  └─ settings.json
├─ src/
│  └─ mmn/
│     ├─ __init__.py
│     ├─ version.py
│     ├─ contracts/
│     │  ├─ __init__.py
│     │  ├─ memory_record_v0.py
│     │  └─ memory_preview_output_v0.py
│     ├─ providers/
│     │  ├─ __init__.py
│     │  └─ memory_stub_provider_v0.py
│     ├─ recall/
│     │  ├─ __init__.py
│     │  └─ recall_stub_v0.py
│     └─ adapters/
│        ├─ __init__.py
│        └─ route_preview_memory_adapter_v0.py
├─ tests/
│  ├─ test_memory_record_v0.py
│  ├─ test_memory_preview_output_v0.py
│  ├─ test_memory_stub_provider_v0.py
│  ├─ test_recall_stub_v0.py
│  └─ test_route_preview_memory_adapter_v0.py
└─ docs/
   ├─ ARCHITECTURE_OVERVIEW.md
   ├─ MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0.md
   ├─ MMN_OBJECT_FAMILY_V0.md
   ├─ MEMORY_PREVIEW_OUTPUT_V0.md
   ├─ ROUTE_PREVIEW_MEMORY_SEAM_V0.md
   ├─ MMN_MINIMAL_FLOW_EXAMPLE_V0.md
   └─ README_DOC_CHAIN_V0.md
```

---

## 当前仓与 fuller MMN 的关系

需要特别强调：

当前仓并不等于完整 MMN。

当前仓更适合被理解为：

- 最小 memory-semantic producer host
- preview-only memory seam host
- future richer MMN semantics 的 contract-preserving 起点

而不是：

- 完整 memory runtime
- 完整长期记忆系统
- 最终版 recall engine
- 最终版 posterior correction engine

换句话说：

> 当前 `aiant-mmn` 先解决“最小但稳定的 memory preview object 是否存在”，
再继续讨论更强的 recall family、historical comparison、posterior correction 与 memory write-back。

---

## 后续可能演进

在第二批或后续版本中，可以继续讨论：

- richer recall families
- historical comparison objects
- posterior correction objects
- memory write-back objects
- citation governance stub
- trace envelope contract
- memory-to-preview-consumer seam tightening
- memory registry / provenance registry

但这些都应建立在当前最小骨架已经稳定的前提上。

---

## 当前阶段的一句话总结

可以用下面这句话概括当前 `aiant-mmn`：

> `aiant-mmn` 当前不是完整 MMN 系统，
而是一个 contract-first、preview-only、non-executing 的最小记忆语义输出仓库；
它先把 memory preview output、recall stub 与最小 preview-facing seam 钉住，
为未来 richer MMN semantics 的接入预留稳定边界。


这版的核心，就是把 README 从“MMN 通过 pant 承接自身意义”改成“MMN 先稳定自身最小记忆语义宿主位”。这和总分层 AIANTPDE_README 里给 MMN 的定位一致。
