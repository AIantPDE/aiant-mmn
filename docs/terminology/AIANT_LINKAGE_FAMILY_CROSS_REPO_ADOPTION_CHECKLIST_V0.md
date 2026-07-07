# AIANT 链路类术语跨仓采用检查清单 V0

Status: draft adoption checklist  
Scope: cross-repo terminology adoption guidance  
Boundary: docs / manifest / regression tests only  
Sentinel: `AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0_READY`

## 1. 目的

本文件用于把 `AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0` 中的链路类术语规范，
映射到 AIANT 多仓文档场景中。它不是 formal terminology registry，
也不是 scanner implementation，只是一个 cross-repo adoption checklist。

本文件关注的问题是：

```text
同一个中文“链路”在不同仓库、不同文档场景里，
到底应该落到 chain / lane / trace / path / route / lineage / bridge / seam /
handoff / loop / link / surface / boundary 中的哪一个术语。
```

本文件不要求一次性改完所有历史文档。它只提供后续 review、patch、scanner
准备和 PR 描述时可引用的 adoption checklist。

## 2. 非目标 / Non-goals

本检查清单不做以下事情：

```text
- 不修改 aiant-contracts schema surface；
- 不修改 aiant-governance scanner；
- 不修改 aiant-pant runtime route 或 scheduler admission；
- 不修改 aiant-core topology object；
- 不修改 aiant-vant / aiant-zant / aiant-mmn runtime behavior；
- 不创建 formal registry；
- 不激活自动术语替换；
- 不授权 memory write；
- 不授权 runtime activation。
```

## 3. 上游术语基线

本文件承接：

```text
AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0
```

核心口径：

```text
chain 管顺序；
lane 管归类；
trace 管复盘；
path 管可达；
route 管准入选择；
flow 管信息流动；
pipeline 管阶段化处理；
lineage 管来源继承；
provenance 管来源证明；
audit trail 管审计记录；
bridge 管跨层连接；
seam 管薄接口；
handoff 管移交；
loop 管反馈回流；
link 管对象关联；
surface 管暴露面；
boundary 管禁止越界。
```

## 4. 跨仓采用原则

### 4.1 先判断文档意图，再选择术语

不要因为中文里都能说“链路”，就把英文都写成 `chain` 或 `link`。

采用术语前先问：

```text
- 文档是在描述不可跳跃的阶段顺序吗？如果是，用 chain。
- 文档是在给一批工作归类吗？如果是，用 lane。
- 文档是在复盘对象如何演化到当前状态吗？如果是，用 trace。
- 文档是在说明拓扑上是否可达吗？如果是，用 path。
- 文档是在说明被选择、被预览、被准入或被拒绝的处理路线吗？如果是，用 route。
- 文档是在说明证据、对象或 receipt 从哪里派生吗？如果是，用 lineage。
- 文档是在说明来源可信度或出处证明吗？如果是，用 provenance。
- 文档是在说明跨层安全连接吗？如果是，用 bridge。
- 文档是在说明模块之间的薄接口吗？如果是，用 seam。
- 文档是在说明上游把 envelope 或上下文交给下游吗？如果是，用 handoff。
- 文档是在说明反馈回流吗？如果是，用 loop。
- 文档是在说明单个对象关联吗？如果是，用 link。
- 文档是在说明可被消费的对象集合吗？如果是，用 surface。
- 文档是在说明允许和禁止范围吗？如果是，用 boundary。
```

### 4.2 禁止把 adoption checklist 当成自动替换规则

本文件不是 search-and-replace 规则。很多历史上下文需要人工判断。

例如：

```text
route preview
```

应保留为路由预览，不应因为中文“路线”而改成 `lane preview`。

又如：

```text
attribution_link_ref
```

是归因关联引用，不应改成 `attribution_chain_ref`，除非对象真的表示多个有序阶段。

## 5. 仓库采用检查清单

### 5.1 aiant-governance

`aiant-governance` 主要负责治理扫描、检查、拒绝、准入前审查和政策性边界。

优先采用：

```text
lane       = 治理路线 / 工作路线 / 归类通道
trace      = 可追溯轨迹 / 审计轨迹 / 修正轨迹
audit trail = 审计轨迹
boundary   = 边界
scanner    = 扫描器
waiver     = 豁免
policy     = 策略 / 政策
```

适用场景：

```text
- downstream adoption lane
- scanner preparation lane
- governance boundary
- denial trace
- waiver audit trail
- policy check trace
```

不建议：

```text
- 把 scanner preparation lane 写成 scanner preparation chain；
- 把 governance boundary 写成 governance route；
- 把 waiver audit trail 写成 waiver chain；
- 把 policy check trace 写成 policy path。
```

采用检查：

```text
[ ] PR / docs 中的 lane 是否用于工作归类，而不是阶段顺序？
[ ] trace 是否用于可复盘历史，而不是路线分类？
[ ] boundary 是否明确表示允许 / 禁止范围？
[ ] scanner 相关文档是否避免暗示 runtime authorization？
[ ] waiver 是否带有 receipt / audit trail / reviewer boundary？
```

### 5.2 aiant-contracts

`aiant-contracts` 主要负责共享对象、accepted schema surface、contract boundary
和跨仓稳定字段。

优先采用：

```text
surface    = 暴露面 / 合同表面
boundary   = 边界
lineage    = 血缘 / 来源谱系
provenance = 来源证明 / 出处 / 来源元信息
link       = 关联 / 链接
receipt    = 回执
schema     = 模式 / schema
```

适用场景：

```text
- accepted schema surface
- contract surface
- field registry boundary
- canonical hash lineage
- evidence provenance
- attribution link ref
- receipt lineage
```

不建议：

```text
- 把 accepted schema surface 写成 accepted schema chain；
- 把 contract boundary 写成 contract lane；
- 把 attribution_link_ref 翻成完整归因链；
- 把 provenance 与 trace 混用。
```

采用检查：

```text
[ ] surface 是否用于可被下游消费的对象集合？
[ ] boundary 是否说明 schema / registry / authority 的允许范围？
[ ] lineage 是否说明对象从哪里派生？
[ ] provenance 是否说明来源证明，而不是过程复盘？
[ ] link 是否只表示对象关联，而不是完整有序链？
```

### 5.3 aiant-pant

`aiant-pant` 主要负责抓取 / 处理闭环、route preview、scheduler admission、
execution handoff、read-side consumer 和 runtime boundary。

优先采用：

```text
route    = 路由
path     = 路径
handoff  = 移交 / 移交信封
loop     = 闭环 / 回路
flow     = 流 / 信息流
pipeline = 管线 / 流水线
boundary = 边界
```

适用场景：

```text
- route preview
- route admission
- runtime topology path
- execution handoff envelope
- read-side consumer flow
- feedback validation loop
- scheduler pipeline
- runtime boundary
```

不建议：

```text
- 把 route preview 写成 path preview；
- 把 execution handoff envelope 写成 execution chain envelope；
- 把 feedback loop 写成 feedback chain；
- 把 runtime boundary 写成 runtime link。
```

采用检查：

```text
[ ] route 是否用于被选择 / 预览 / 准入 / 拒绝的处理路线？
[ ] path 是否只用于拓扑可达性？
[ ] handoff 是否明确为上游向下游移交 envelope / 上下文？
[ ] loop 是否表达反馈回流，而不是单向顺序？
[ ] runtime boundary 是否保持 non-executing / non-authorizing 表达？
```

### 5.4 aiant-core

`aiant-core` 主要负责 topology、module registry、system control stub 和跨模块编排。

优先采用：

```text
path     = 路径
route    = 路由
edge     = 边 / 连接边
graph    = 图 / 关系图
boundary = 边界
surface  = 暴露面
topology = 拓扑
```

适用场景：

```text
- topology path
- module graph
- registry edge
- route intake reference
- system topology boundary
- module surface
```

不建议：

```text
- 把 topology path 写成 topology chain，除非明确表示有序阶段；
- 把 graph edge 写成 trace；
- 把 route intake 写成 lane intake；
- 把 module surface 写成 module route。
```

采用检查：

```text
[ ] path 是否表达拓扑可达？
[ ] route 是否表达被选择或可被调度的路线？
[ ] graph / edge 是否保留图结构语义？
[ ] boundary 是否表达控制边界而非执行授权？
[ ] surface 是否表示模块可被消费的接口集合？
```

### 5.5 aiant-mmn

`aiant-mmn` 主要负责 memory preview、AEM authority-source memory、field pressure
ledger、candidate field suggestion、memory writeback preview 和 future reuse boundary。

优先采用：

```text
chain    = 有序链 / 方法链
trace    = 可追溯轨迹 / 审计轨迹
lineage  = 血缘 / 来源谱系
link     = 关联 / 链接
ledger   = 账本
boundary = 边界
loop     = 闭环
```

适用场景：

```text
- AEM ordered chain
- attribution chain construction
- predecessor memory lineage
- attribution_link_ref
- field pressure ledger
- memory promotion trace
- future reuse boundary
- memory feedback loop
```

不建议：

```text
- 把 attribution_link_ref 误写成完整 attribution chain；
- 把 field pressure ledger 写成 field pressure chain；
- 把 future reuse boundary 写成 future reuse route；
- 把 predecessor lineage 与 decision trace 混用。
```

采用检查：

```text
[ ] chain 是否表示 AEM / CAGP 的不可跳跃顺序？
[ ] link 是否只表示单个归因关联？
[ ] lineage 是否用于 predecessor / evidence / receipt 来源继承？
[ ] trace 是否用于 decision / promotion / revision 的可复盘过程？
[ ] ledger 是否保持 candidate-only / non-authorizing？
```

### 5.6 aiant-zant

`aiant-zant` 主要负责 explain bundle seam、summary output、fallback policy
和结构化解释输出。

优先采用：

```text
seam     = 接缝 / 接口接缝
surface  = 暴露面
flow     = 流 / 信息流
boundary = 边界
trace    = 可追溯轨迹
policy   = 策略
```

适用场景：

```text
- explain_bundle seam
- summary output surface
- fallback policy boundary
- explanation trace
- provider flow
```

不建议：

```text
- 把 explain_bundle seam 写成 explain_bundle bridge，除非强调跨层过桥；
- 把 fallback policy boundary 写成 fallback policy chain；
- 把 summary output surface 写成 summary output route。
```

采用检查：

```text
[ ] seam 是否用于薄接口，不暗示运行接管？
[ ] surface 是否表示下游可消费输出面？
[ ] fallback policy 是否保持 policy boundary？
[ ] trace 是否用于解释输出可复盘？
```

### 5.7 aiant-vant

`aiant-vant` 主要负责 semantic preview、semantic residual hint、pant-facing adapter
和语义供给边界。

优先采用：

```text
flow     = 流 / 信息流
seam     = 接缝
bridge   = 桥接
hint     = 提示
surface  = 暴露面
boundary = 边界
```

适用场景：

```text
- semantic preview flow
- pant-facing adapter seam
- semantic residual hint
- semantic preview surface
- supply boundary
```

不建议：

```text
- 把 semantic residual hint 写成 semantic attribution；
- 把 pant-facing adapter seam 写成 runtime route；
- 把 preview surface 写成 accepted schema surface。
```

采用检查：

```text
[ ] semantic hint 是否保持 hint，不升级为 authority evidence？
[ ] seam / bridge 是否说明接口性质，而不是 runtime authority？
[ ] preview surface 是否保持 preview-only？
[ ] supply boundary 是否禁止 side-effect？
```


### 5.8 aiant-drl

`aiant-drl` 是 future downstream policy candidate consumer。当前采用边界是
policy candidate observation / offline observation candidate，而不是 action executor。
在当前阶段它应保持 not connected / not consuming / not deciding / not executing，
并且没有 runtime authority。

优先采用：

```text
surface    = 策略候选观测暴露面 / policy candidate observation surface
chain      = 策略候选审查有序链 / policy candidate review chain
trace      = 策略候选审计轨迹 / policy candidate audit trace
lineage    = 策略特征血缘 / policy feature lineage
provenance = 离线观测来源证明 / offline observation provenance
boundary   = 禁止动作执行边界 / no-action-execution boundary
route      = 策略候选路由，仅在 preview / admission / denial 明确存在时使用
```

适用场景：

```text
- policy candidate observation surface
- policy candidate review chain
- policy candidate audit trace
- policy feature lineage
- offline observation provenance
- no-action-execution boundary
- policy candidate route, only when preview / admission / denial is explicit
```

不建议：

```text
- policy execution chain
- live decision route
- action execution path
- runtime policy loop
```

采用检查：

```text
[ ] policy candidate 是否保持 candidate / observation，而不是 execution？
[ ] chain 是否用于候选策略审查顺序，而不是动作执行顺序？
[ ] trace 是否用于候选策略审计历史？
[ ] lineage / provenance 是否说明离线观测与策略特征来源？
[ ] boundary 是否明确禁止 action execution / live decision？
```

### 5.9 aiant-tft

`aiant-tft` 是 future downstream temporal preview consumer。当前采用边界是
temporal window candidate / temporal feature window，而不是 live forecast consumer。
在当前阶段它应保持 not connected / not consuming / not deciding / not executing，
并且没有 runtime authority。

优先采用：

```text
surface    = 时间预览暴露面 / temporal preview surface
chain      = 时间窗口构造有序链 / temporal window construction chain
sequence   = 时间序列 / temporal sequence
window     = 时间窗口 / temporal window
lineage    = 时间特征血缘 / temporal feature lineage
provenance = 时间序列来源证明 / time-series source provenance
trace      = 时间预览审计轨迹 / temporal preview trace
boundary   = 禁止实时预测消费边界 / no-live-forecast-consumption boundary
```

适用场景：

```text
- temporal preview surface
- temporal window construction chain
- temporal sequence
- temporal window
- temporal feature lineage
- time-series source provenance
- temporal preview trace
- no-live-forecast-consumption boundary
```

不建议：

```text
- live forecast route
- prediction execution path
- temporal action chain
- runtime forecasting pipeline
```

采用检查：

```text
[ ] sequence 是否保留时间序列语义，而不是泛译为链路？
[ ] window 是否保留时间窗口语义，而不是泛译为链路？
[ ] chain 是否只用于时间窗口构造顺序？
[ ] trace 是否用于 preview 审计轨迹？
[ ] boundary 是否明确禁止 live forecast consumption？
```

### 5.10 aiant-gant

`aiant-gant` 是 future downstream graph relation preview consumer。当前采用边界是
graph propagation candidate / graph feature candidate / node-edge relation candidate，
而不是 graph action executor。在当前阶段它应保持 not connected / not consuming /
not deciding / not executing，并且没有 runtime authority。

优先采用：

```text
graph    = 图 / 关系图
node     = 节点
edge     = 边 / 图结构连接边
link     = 节点间关联 / object-to-object relation
chain    = 图传播审查有序链 / graph propagation review chain
trace    = 图关系审计轨迹 / graph relation audit trace
lineage  = 图特征血缘 / graph feature lineage
surface  = 图关系预览暴露面 / graph relation preview surface
boundary = 禁止图动作边界 / no-graph-action boundary
```

适用场景：

```text
- graph relation preview surface
- graph propagation review chain
- graph relation audit trace
- graph feature lineage
- node-edge relation candidate
- no-graph-action boundary
```

不建议：

```text
- graph action route
- graph execution path
- node action chain
- live graph propagation loop
```

特别区分：

```text
edge  = 图中的边；
link  = 两个对象之间的一条关联；
chain = 多个阶段或关系构成的有序序列。
```

采用检查：

```text
[ ] graph / node / edge 是否保留图结构语义？
[ ] link 是否用于对象间关联，而不是完整方法链？
[ ] chain 是否用于 graph propagation review 的审查顺序？
[ ] trace 是否用于图关系审计轨迹？
[ ] boundary 是否明确禁止 graph action / live propagation？
```

### 5.11 aiant-marl

`aiant-marl` 是 future downstream multi-agent interaction consumer。当前采用边界是
multi-agent candidate interaction / interaction topology candidate，而不是 live action
system。在当前阶段它应保持 not connected / not consuming / not deciding /
not executing，并且没有 runtime authority。

优先采用：

```text
surface  = 多智能体交互预览暴露面 / multi-agent interaction preview surface
chain    = 多智能体交互审查有序链 / multi-agent interaction review chain
trace    = 智能体交互审计轨迹 / agent interaction audit trace
topology = 交互拓扑 / interaction topology
path     = 智能体交互路径，仅用于拓扑可达性 / agent interaction path
route    = 智能体协调路由，仅在 preview / admission / denial 明确存在时使用
lineage  = 交互证据血缘 / interaction evidence lineage
boundary = 禁止实时动作边界 / no-live-action boundary
loop     = 协调反馈闭环，仅在反馈回流明确存在时使用
```

适用场景：

```text
- multi-agent interaction preview surface
- multi-agent interaction review chain
- agent interaction audit trace
- interaction topology
- agent interaction path, only for reachability
- agent coordination route, only for explicit preview / admission / denial
- interaction evidence lineage
- no-live-action boundary
- coordination feedback loop, only for explicit feedback return
```

不建议：

```text
- agent action execution route
- live coordination path
- multi-agent policy execution chain
- runtime agent loop
```

采用检查：

```text
[ ] topology 是否用于交互结构，而不是执行路线？
[ ] path 是否只用于拓扑可达性？
[ ] route 是否只用于明确 preview / admission / denial 的协调选择？
[ ] loop 是否只用于明确反馈回流？
[ ] boundary 是否明确禁止 live action / runtime agent execution？
```

### 5.12 future downstream preview boundary summary

`aiant-drl / aiant-tft / aiant-gant / aiant-marl` 四个仓统一按
future downstream preview / candidate surface 处理。它们可以采用
`surface / chain / trace / lineage / provenance / boundary` 等术语，
但不得引入 execution route、live action path、runtime loop、live forecast route、
graph action route 或 policy execution chain 等授权语义。

统一约束：

```text
- not connected
- not consuming
- not deciding
- not executing
- no runtime authority
- candidate / preview surface only
```

## 6. 高风险混用场景

### 6.1 link vs chain

`link` 是单个对象关联；`chain` 是多个阶段组成的有序链。

```text
attribution_link_ref = 归因关联引用
attribution chain construction = 归因链构造
```

风险：把 `link` 翻成完整“链”，会让单个对象关系看起来像已完成整条方法链。

### 6.2 route vs path

`path` 管可达；`route` 管选择、预览、准入或拒绝。

```text
runtime topology path = 运行时拓扑路径
route preview = 路由预览
route admission = 路由准入
```

风险：把 route 写成 path，会弱化 admission / denial 语义。

### 6.3 lineage vs trace

`lineage` 管来源继承；`trace` 管过程复盘。

```text
predecessor memory lineage = 前序记忆血缘
promotion decision trace = 晋级决策轨迹
```

风险：把 lineage 写成 trace，会丢失来源继承语义；把 trace 写成 lineage，会丢失过程审计语义。

### 6.4 bridge vs seam

`bridge` 管跨层连接；`seam` 管薄接口。

```text
runtime [4] -> [5] bridge = runtime [4] 到 [5] 过桥
explain_bundle seam = explain_bundle 接缝
```

风险：把 seam 写成 bridge，可能暗示跨层执行连接；把 bridge 写成 seam，可能弱化跨层安全转换。

### 6.5 handoff vs flow

`handoff` 是移交；`flow` 是流动。

```text
execution handoff envelope = 执行移交信封
read-side consumer flow = 读侧消费流
```

风险：把 handoff 写成 flow，会丢失 envelope / responsibility transfer 语义。

### 6.6 loop vs chain

`loop` 是反馈回流；`chain` 是单向顺序。

```text
feedback validation loop = 反馈验证闭环
AEM ordered chain = AEM 有序链
```

风险：把 loop 写成 chain，会丢失反馈校正含义。

### 6.7 surface vs boundary

`surface` 是可被消费的暴露面；`boundary` 是允许 / 禁止范围。

```text
accepted schema surface = accepted schema 暴露面
runtime boundary = 运行时边界
```

风险：把 surface 写成 boundary，会丢失下游消费语义；把 boundary 写成 surface，
会弱化禁止越界语义。

## 7. PR review 使用方式

在 PR review 中，可以把本检查清单作为轻量 checklist 使用：

```text
[ ] 当前文档是否把 chain / lane / trace 混用？
[ ] 当前文档是否把 path / route 混用？
[ ] 当前文档是否把 lineage / provenance / trace 混用？
[ ] 当前文档是否把 bridge / seam / handoff 混用？
[ ] 当前文档是否把 loop 写成 chain？
[ ] 当前文档是否把 link 写成完整 chain？
[ ] 当前文档是否把 surface / boundary 混用？
[ ] 如果使用“链路”作为中文泛称，是否已经在上下文中给出精确英文术语？
```

## 8. 后续扩展建议

后续可以分三步扩展，但本文件不执行这些动作：

```text
1. downstream adoption notes:
   在 governance / contracts / pant / core / zant / vant / mmn / drl / tft / gant / marl 的相关 docs 中引用本清单。

2. terminology scanner preparation:
   将高风险混用场景转成 scanner candidate rules，但保持 report-only。

3. formal terminology registry proposal:
   若跨仓复用稳定，再进入 formal terminology registry review。
```

## 9. 验收条件

本文件满足以下条件即可视为 ready：

```text
- 给出每个仓库优先采用的链路类术语；
- 给出每个仓库的适用场景；
- 给出每个仓库的不建议用法；
- 给出 PR review checklist；
- 明确 docs-only / non-executing / non-authorizing；
- 不修改任何 runtime、schema、scanner 或 registry。
```

## 10. Sentinel

```text
AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0_READY
```
