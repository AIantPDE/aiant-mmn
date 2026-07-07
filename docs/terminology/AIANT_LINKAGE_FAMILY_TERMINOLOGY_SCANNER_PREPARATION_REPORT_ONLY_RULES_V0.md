# AIANT Linkage-family Terminology Scanner Preparation Report-only Rules V0

Status: draft scanner-preparation guidance  
Owner: AIANT terminology / governance preparation  
Scope: docs + manifest + regression tests only  
Mode: report-only candidate rules  
Sentinel: `AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_PREPARATION_REPORT_ONLY_RULES_V0_READY`

## 1. 目的

本文档承接：

- `AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0`
- `AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0`

目标不是实现 scanner，而是把链路类术语的高风险混用场景，预先整理成
**report-only scanner candidate rules**。

本文件只回答一个问题：

```text
如果以后要做术语 scanner，哪些混用场景应该先被报告出来，让 reviewer 人工判断？
```

它不回答：

```text
如何自动替换？
如何阻断 CI？
如何修改正式 registry？
如何改 contracts schema？
如何改变 runtime 行为？
```

## 2. 非授权边界

本文件保持以下边界：

```text
report-only rules only
scanner-preparation only
no scanner implementation
no CI gating
no automatic replacement
no formal terminology registry activation
no contracts schema change
no runtime behavior change
no cross-repo file mutation
non-executing
non-authorizing
```

如果未来接入 scanner，这些规则默认只能产生 report：

```text
found candidate terminology ambiguity
review recommended
no automatic rewrite
no blocking failure
```

除非后续单独通过 governance / contracts / CI decision 明确升级，否则不得把本文件解释为
CI blocking policy。

## 3. 术语 scanner 的 report-only 原则

### 3.1 只报告，不裁决

候选规则只能报告：

```text
这里可能把 chain / lane / trace / route / path / lineage / bridge / seam / handoff / loop 等术语
混译成了泛化的“链路”。
```

候选规则不能直接裁决：

```text
该用词一定错误。
该 PR 必须失败。
该词必须自动替换。
```

### 3.2 必须保留上下文

同一个词在不同仓库、不同上下文中可能合理。例如：

```text
route 在 P-ant 中通常强调 route preview / route admission。
path 在 Core 中通常强调 topology reachability。
link 在 MMN AEM 中可能是 attribution link。
edge 在 GANT 中可能是 graph edge。
```

因此 scanner 报告必须携带：

```text
file_path
line_number
matched_text
nearby_context
candidate_rule_id
recommended_review_question
suggested_precise_terms
non_authorizing_note
```

### 3.3 不得自动替换中文“链路”

中文“链路”可以作为泛称出现，但正式术语应尽量精确。scanner 可以报告：

```text
“链路”可能需要英文锚点或更精确译法。
```

但不得自动把“链路”替换成“有序链 / 路由 / 路径 / 轨迹 / 血缘 / 接缝 / 桥接”。

## 4. 高风险候选规则族

### RULE-LINKAGE-001: generic_zh_linkage_without_english_anchor

风险：中文“链路”单独出现，但没有明确英文锚点。

典型触发：

```text
执行链路
治理链路
证据链路
运行链路
能力链路
```

推荐 review question：

```text
这里的“链路”具体是 chain, lane, trace, route, path, lineage, bridge, seam,
handoff, loop, link, surface, or boundary 中的哪一个？
```

建议处理：

```text
保留中文表达，但补英文锚点；或替换为更精确中文术语。
```

示例：

```text
AEM ordered chain / AEM 有序链
field-registry-feedback lane / 字段注册反馈治理路线
promotion decision trace / 晋级决策审计轨迹
runtime route admission / 运行路由准入
```

### RULE-LINKAGE-002: chain_lane_trace_confusion

风险：把顺序、归类、复盘混在一起。

区分：

```text
chain = 有序链，回答“必须按什么顺序走？”
lane  = 治理路线，回答“这批工作属于哪类路线？”
trace = 可追溯轨迹，回答“它如何走到现在？”
```

典型高风险场景：

```text
把 PR 家族叫 chain，但实际表达的是 governance lane。
把历史修正记录叫 lane，但实际表达的是 trace。
把 AEM ordered chain 说成 scanner lane，弱化了不可跳跃顺序。
```

### RULE-LINKAGE-003: path_route_confusion

风险：把 topology reachability 和 admission-selected route 混同。

区分：

```text
path  = 路径，强调拓扑可达。
route = 路由，强调选择、预览、准入、拒绝。
```

典型高风险场景：

```text
core topology path 被写成 route admission。
pant route preview 被写成 generic path。
runtime route denial 被写成 path failure，弱化准入语义。
```

### RULE-LINKAGE-004: lineage_trace_provenance_confusion

风险：把来源继承、过程复盘、来源证明混同。

区分：

```text
lineage    = 血缘，回答“从哪些来源继承或派生？”
trace      = 可追溯轨迹，回答“经历了哪些步骤、receipt、decision？”
provenance = 来源证明，回答“来源是谁、何时、如何被证明可信？”
```

典型高风险场景：

```text
把 evidence provenance 写成 evidence trace。
把 PR correction trace 写成 lineage。
把 canonical hash lineage 写成 audit trail。
```

### RULE-LINKAGE-005: bridge_seam_handoff_confusion

风险：把跨层桥接、薄接口接缝、阶段移交混同。

区分：

```text
bridge  = 桥接 / 过桥，强调跨层安全连接。
seam    = 接缝，强调模块之间的薄接口。
handoff = 移交，强调上游把 envelope/context 交给下游。
```

典型高风险场景：

```text
把 explain_bundle seam 写成 bridge。
把 execution_handoff_envelope 写成 execution bridge。
把 [4] -> [5] runtime bridge 写成 generic seam。
```

### RULE-LINKAGE-006: flow_pipeline_loop_confusion

风险：把流动、分阶段处理、反馈回流混同。

区分：

```text
flow     = 信息流 / 数据流 / 控制流。
pipeline = 管线 / 流水线，强调多阶段处理。
loop     = 闭环 / 回路，强调反馈回流。
```

典型高风险场景：

```text
把 feedback validation loop 写成 one-way flow。
把 extraction pipeline 写成 generic route。
把 semantic flow 写成 runtime pipeline，暗示执行化。
```

### RULE-LINKAGE-007: link_chain_confusion

风险：把单个对象关系误写成完整有序链。

区分：

```text
link  = 关联 / 链接，通常是两个对象之间的关系。
chain = 有序链，通常是多个阶段或关系构成的有序结构。
```

典型高风险场景：

```text
把 attribution_link_ref 翻成归因链结果。
把 object-to-object relation link 写成 process chain。
把 candidate field reference link 写成 capability chain。
```

### RULE-LINKAGE-008: surface_boundary_confusion

风险：把可消费暴露面和禁止越界边界混同。

区分：

```text
surface  = 暴露面 / 合同表面，表示可被消费的对象集合或接口面。
boundary = 边界，表示允许与禁止的治理范围。
```

典型高风险场景：

```text
把 accepted schema surface 写成 accepted schema boundary。
把 non-authorizing boundary 写成 non-authorizing surface。
把 preview surface 写成 runtime boundary breach。
```

### RULE-LINKAGE-009: graph_edge_link_chain_confusion

适用仓库：`aiant-gant`，也适用于 Core graph/topology docs。

风险：把 graph / node / edge / link / chain 都翻成链路。

区分：

```text
graph = 图 / 关系图
node  = 节点
edge  = 边
link  = 对象间关联
chain = 有序链
```

典型高风险场景：

```text
graph edge 被写成 chain。
object relation link 被写成 edge，而上下文不是图结构。
graph propagation review chain 被写成 graph execution path。
```

边界：

```text
aiant-gant 当前只能是 graph relation preview / graph propagation candidate。
不得引入 graph action route / graph execution path / live graph propagation loop。
```

### RULE-LINKAGE-010: tft_sequence_window_chain_confusion

适用仓库：`aiant-tft`。

风险：把 temporal sequence / temporal window / construction chain 混同。

区分：

```text
sequence = 时间序列
window   = 时间窗口
chain    = 构造有序链或审查有序链
```

典型高风险场景：

```text
temporal sequence 被写成 temporal chain。
temporal window 被写成 live forecast route。
temporal preview surface 被写成 prediction execution path。
```

边界：

```text
aiant-tft 当前只能是 temporal preview / temporal window candidate。
不得引入 live forecast route / prediction execution path / runtime forecasting pipeline。
```

### RULE-LINKAGE-011: drl_execution_semantics_boundary

适用仓库：`aiant-drl`。

风险：把 policy candidate observation 误写成执行授权。

允许术语：

```text
policy candidate observation surface
policy candidate review chain
policy candidate audit trace
policy feature lineage
offline observation provenance
no-action-execution boundary
```

高风险术语：

```text
policy execution chain
live decision route
action execution path
runtime policy loop
```

边界：

```text
aiant-drl 当前只能是 policy candidate observation / offline observation candidate。
不得引入 action execution 或 runtime decision 语义。
```

### RULE-LINKAGE-012: marl_live_action_semantics_boundary

适用仓库：`aiant-marl`。

风险：把 multi-agent interaction candidate 误写成 live action system。

允许术语：

```text
multi-agent interaction preview surface
multi-agent interaction review chain
agent interaction audit trace
interaction topology
agent interaction path, only for topological reachability
agent coordination route, only for explicit preview/admission/denial
coordination feedback loop, only for explicit feedback return
no-live-action boundary
```

高风险术语：

```text
agent action execution route
live coordination path
multi-agent policy execution chain
runtime agent loop
```

边界：

```text
aiant-marl 当前只能是 multi-agent candidate interaction / topology candidate。
不得引入 live action 或 runtime agent execution 语义。
```

## 5. 报告格式建议

未来如果实现 scanner，建议 report item 最小结构为：

```json
{
  "rule_id": "RULE-LINKAGE-003",
  "mode": "report_only",
  "severity": "review",
  "file_path": "docs/example.md",
  "line_number": 42,
  "matched_text": "runtime path admission",
  "nearby_context": "...",
  "recommended_review_question": "Is this path or route?",
  "suggested_precise_terms": ["runtime route admission", "topology path"],
  "auto_replace_allowed": false,
  "ci_blocking_allowed": false,
  "non_authorizing_note": "This report does not change runtime behavior."
}
```

## 6. Review checklist

PR reviewer 可以使用以下人工 checklist：

```text
[ ] 是否把“链路”泛称补上了英文锚点？
[ ] 是否区分 chain / lane / trace？
[ ] 是否区分 path / route？
[ ] 是否区分 lineage / trace / provenance？
[ ] 是否区分 bridge / seam / handoff？
[ ] 是否区分 flow / pipeline / loop？
[ ] 是否区分 link / chain？
[ ] 是否区分 surface / boundary？
[ ] 对 GANT 是否区分 graph / node / edge / link / chain？
[ ] 对 TFT 是否区分 sequence / window / chain？
[ ] 对 DRL 是否避免 action execution 语义？
[ ] 对 MARL 是否避免 live action / runtime agent execution 语义？
[ ] 是否仍保持 report-only、non-executing、non-authorizing？
```

## 7. Not ready for scanner activation

本文件显式声明：当前阶段还不能激活 scanner。

未完成项：

```text
no scanner CLI
no scanner engine
no file traversal implementation
no match engine
no suppression format
no baseline report
no CI policy
no governance approval for blocking mode
no cross-repo rollout plan
```

因此 sentinel 只表示 report-only rules preparation ready：

```text
AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_PREPARATION_REPORT_ONLY_RULES_V0_READY
```
