# MMN Authority Event Memory 业务能力场景分类与 Field Registry Feedback 边界 V0

本文是对 `MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_REQUIREMENT_SCENARIO_FIXTURES_V0` 的语义校准文件。

本次修正的重点不是使用 `CAGP V1.1` 论文来反向指导本 PR，也不是把当前问题改写成跨仓 CAGP 方法论问题。
本次修正的重点是：**重新定义 AEM 业务能力本身，并明确 AEM 的业务能力至少包含六个子能力。**

本文也作为从 `aiant-mmn #42` 到 `aiant-governance #84` 这一条 AEM 相关 lane 的纸质技术留档说明。
该 lane 不是危险 runtime lane，也不需要 revert；但它确实由 `aiant-mmn #42` 对“业务需求场景样例”的过宽命名和错误层级理解触发。
因此，本文将该 lane 保留并重新分类为 AEM 下游的 field-registry-feedback / evidence-boundary / receipt-alignment / scanner-preparation lane，
而不是完整的 AEM business capability scenario lane。

## 状态

```text
asset_id: mmn_authority_event_memory_business_capability_scenario_taxonomy_and_field_registry_feedback_boundary_v0
status: candidate-only / clarification-only / non-executing
scope: docs + fixtures + regression tests only
primary_correction_focus: AEM_six_business_subcapabilities_first
cagp_role_in_this_pr: background_context_only_not_the_governing_source
ready_for_scanner_implementation_skeleton: false
trace_handling: reclassify_not_revert
```

## 核心结论

AEM 的业务能力，不应先从 `field registry`、`write request` 或 scanner implementation skeleton 出发。
更准确的定义是：

```text
AEM 的业务能力，是在关键拐点或异常信号出现后，能够系统化地发现、筛选、归因、审计、降级、晋级权威事件，并将其转化为 MMN 可复用记忆的能力。
```

因此，当前 `mmn: clarify AEM business capability scenario taxonomy and field registry feedback boundary v0` 的修正重点应是 AEM 的六个业务子能力，而不是 CAGP V1.1 论文。

更短地说：

```text
字段完整性 = AEM 记忆候选能否被表达。
业务能力场景 = AEM 为什么要构造这类记忆。
```

## “字段是否齐”与“AEM 业务能力场景”的差别

“字段是否齐”问的是：

```text
这个 candidate payload 有没有 source_repo？
有没有 authority_event_ref？
有没有 evidence_ref？
有没有 attribution_score？
有没有 dedupe_key？
有没有 downgrade_reason？
有没有 promotion_checklist_ref？
```

这是 schema / registry completeness 视角。
它检查的是：某个候选对象是否具备足够字段来被表达、校验、对齐、拒绝或延期。

但“AEM 业务能力场景”不是先问字段。
它先问的是：

```text
1. 是否出现了值得解释的拐点、扰动、异常或失败信号？
2. 是否存在可检索的权威源事件？
3. 这个权威事件与拐点之间能否构造归因链？
4. 如何防止事后叙事、前视泄漏、选择性取证和伪因果？
5. 这个候选事件记忆应被晋级、降级、延期还是拒绝？
6. 这段记忆未来能否被 MMN 复用，用于解释、风险识别、机会诱惑识别、治理复核或策略扰动理解？
```

这是 AEM business capability 视角。
它关心的是：AEM 为什么需要构造这类 authority event memory，而不是某个字段当前是否填写完整。

因此，正确方向是：

```text
拐点 / 扰动 / 异常 / 失败信号
  -> 权威源事件检索
  -> 归因链构造
  -> 反偏差审计
  -> 记忆晋级 / 降级 / 延期 / 拒绝
  -> 未来复用边界
  -> 反推出 candidate field registry 需要哪些字段
```

错误方向是：

```text
已有 candidate field registry
  -> 找一些场景检查字段是否齐全
  -> 误称为完整 AEM business capability scenario suite
```

字段完整性不是错误目标，但它是下游目标。
它应该发生在 AEM 六个业务子能力已经定义之后，而不是发生在定义 AEM 业务能力之前。

## 原 V0 的错误

原 `MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_REQUIREMENT_SCENARIO_FIXTURES_V0` 使用了“业务需求场景样例”的名称，但其 9 个场景实际主要覆盖：

```text
field registry feedback
evidence completeness
negative boundary
forbidden interpretation
```

这造成了语义定位错误：

```text
legacy business requirement scenario fixtures
  != complete AEM business capability scenario suite
  != AEM six-subcapability seed scenario suite
  != authority-source event memory construction seed scenarios
```

原 V0 并非没有价值。它应被保留为 AEM 下游的 field-registry-feedback / negative-boundary fixture，
但不能被当作完整 AEM 业务能力场景集。

## AEM 业务能力的六个子能力

### 1. 拐点识别能力

AEM 不是从字段开始，也不是从 write request 开始，而是从可观测变化开始。

典型输入包括：

```text
指数拐点
资产价格异常
波动率突变
跨资产联动异常
系统治理状态突变
contract surface promotion / deferral 的关键转折
runtime safety signal 的突变
```

AEM 先问：

```text
发生了什么值得解释的变化？
这个变化是否足够重要，值得构造 event memory？
```

### 2. 权威事件检索能力

接着不是问“字段是否齐”，而是问：

```text
哪些权威源在该时点附近发布过可能相关的事件？
```

权威源可以包括：

```text
央行
政府
监管机构
交易所
统计机构
上市公司公告
权威新闻源
contracts receipt
governance decision
core topology report
accepted schema / registry artifact
```

在 AIANT 内部工程场景中，contracts / governance / core / projection 的正式 artifact 可以作为权威源的一类，但这不是 AEM authority source 的全部含义。

### 3. 归因链构造能力

AEM 不是把事件直接写成结论，而是构造：

```text
turning point <-> candidate authority event
```

之间的 attribution link。

它必须追问：

```text
这个事件与拐点之间时间上是否合理？
语义上是否相关？
是否存在替代解释？
是否有负证据？
是否可能只是巧合？
是否只是 narrative backfitting？
```

所以 AEM 的能力不是“记录事件”，而是构造可审计的归因候选。

### 4. 反偏差能力

AEM 的思想核心之一，是防止事后编故事。

它必须控制：

```text
hindsight bias
narrative backfitting
spurious causality
cherry-picking
look-ahead leakage
multiplicity problem
```

所以 AEM 的业务能力里必须包含：

```text
检索审计
as-of data receipt
placebo test
control window test
blind / semi-blind review
multiplicity control
downgrade reason
score component trace
```

这些不是附属字段，而是 AEM 理论完整性的核心。

### 5. 记忆晋级能力

AEM 不是一开始就生成正式 memory record。它应该有分层：

```text
candidate event
  -> attribution-supported candidate
  -> high-confidence candidate
  -> promoted memory record
  -> risk memory / opportunity candidate memory / perturbation preview
```

并且每一步都需要明确：

```text
为什么晋级？
为什么不晋级？
为什么降级？
什么证据不足？
哪些替代解释仍存在？
```

### 6. 未来复用能力

AEM 的最终目标不是保存一条日志，而是让未来系统在遇到类似拐点、类似扰动、类似政策/治理事件时，可以调用这段 memory。

复用目标包括：

```text
用于解释
用于风险识别
用于机会诱惑警惕
用于 DRL 稳定性扰动测试
用于 governance scanner 的边界校验
用于 contracts / registry promotion 的审计证据
```

因此，AEM 是：

```text
memory construction for future reasoning
```

不是普通记录系统。

## Field Registry Feedback 的正确位置

field registry feedback 不是 AEM business capability 的起点。
它是六个子能力之后的下游产物。

正确方向是：

```text
AEM six business subcapabilities
  -> authority-source event memory construction seed scenarios
  -> required evidence / audit / attribution / promotion semantics
  -> field registry feedback
  -> write request candidate preview
  -> alignment / receipt / scanner planning
```

错误方向是：

```text
candidate field registry
  -> 9 个字段缺失 / 证据缺失 / 边界拒绝场景
  -> scanner implementation skeleton
```

## #42 到 #84 lane 的受影响 trace

本节用于纸质技术留档。
从 `aiant-mmn #42` 到 `aiant-governance #84` 的 lane 由原 V0 对“业务需求场景样例”的过宽命名触发。
该 lane 后续持续保持了 candidate-only、preview-only、non-executing、non-authorizing 边界，因此不应回滚；
但它不能继续被解释为 AEM 业务能力场景已完成。

受影响 trace 包括：

```text
aiant-mmn #42
aiant-contracts #201
aiant-mmn #43
aiant-core #220
aiant-contracts #202
aiant-mmn #44
aiant-contracts #203
aiant-governance #83
aiant-governance #84
```

### 逐项重分类

| PR | 原可能误解 | 修正后分类 |
|---|---|---|
| `aiant-mmn #42` | AEM business requirement scenario fixtures | 错误命名的 field-registry-feedback / negative-boundary fixture 起点 |
| `aiant-contracts #201` | AEM 业务能力需要的正式字段范围 | candidate field registry / grant-envelope feedback support，不代表完整 AEM 能力 |
| `aiant-mmn #43` | write request candidate preview 与 AEM 业务能力对齐 | write request preview alignment for field-feedback lane |
| `aiant-core #220` | core 也承载 AEM capability | core topology / intake / runtime-boundary reference，不承载 AEM theory |
| `aiant-contracts #202` | grant decision receipt 是 AEM 业务能力 receipt | grant-decision candidate plan for boundary / receipt trace |
| `aiant-mmn #44` | write request preview fixture 覆盖 AEM 业务场景 | write-request candidate preview fixtures for feedback lane |
| `aiant-contracts #203` | fixture alignment receipt 对齐了 AEM business scenario | fixture-alignment receipt candidate plan for downstream feedback |
| `aiant-governance #83` | scanner checklist 已可服务 AEM capability | scanner preview checklist for reclassified feedback lane |
| `aiant-governance #84` | scanner source plan 可进入 implementation | scanner source plan only；必须等待 AEM 六子能力 seed suite |

### Trace reclassification decision

```text
AEM_TRACE_RECLASSIFIED_NOT_REVERTED
```

含义：

```text
merged artifacts are retained;
semantic scope is corrected;
runtime activation remains denied;
scanner implementation is blocked until AEM six-subcapability seed scenarios exist.
```

中文解释：

```text
已合并 artifact 保留；
语义范围被修正；
runtime activation 继续拒绝；
在 AEM 六子能力 seed scenarios 完成前，scanner implementation 不得继续。
```

这条 lane 的正确名称应是：

```text
AEM field-registry-feedback / evidence-boundary / receipt-alignment / scanner-preparation lane
```

而不是：

```text
AEM business capability scenario completion lane
```

## 对 aiant-governance #84 的特别约束

`aiant-governance #84` 已靠近 scanner source plan，因此必须设置额外阻断条件：

```text
#84 remains source-plan-only.
No scanner implementation may be derived from #84 until the AEM six-subcapability seed scenario suite is merged.
```

中文解释：

```text
#84 保持 source-plan-only。
在 AEM 六子能力 seed scenario suite 合并前，不得从 #84 推进 scanner implementation。
```

因此，下列任务应暂停：

```text
governance: draft MMN authority event memory write request alignment scanner implementation skeleton v0
```

恢复条件是：

```text
mmn: draft AEM authority-source event memory construction seed scenarios v0
```

已经合并，并明确覆盖 AEM 六个业务子能力。

## 本 PR 对 CAGP V1.1 的处理

CAGP V1.1 可以作为背景关系存在，但不是本 PR 的主要修正依据。
本 PR 不用 CAGP V1.1 反向规定 AEM 业务能力。

本 PR 的主要依据是 AEM 自身的六个业务子能力：

```text
turning_point_detection_capability
authority_event_retrieval_capability
attribution_link_construction_capability
anti_bias_review_capability
memory_promotion_capability
future_reuse_capability
```

后续若要讨论 CAGP 跨仓适用性，应另起 CAGP/repo-specific capability taxonomy 文档，不能替代本 PR 对 AEM 业务能力的校准。

## 后续处理方案

1. 保留原 `MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_REQUIREMENT_SCENARIO_FIXTURES_V0`，不在本 PR 中删除或改名。
2. 将原 V0 降格解释为 field-registry-feedback / negative-boundary fixture。
3. 将 `aiant-mmn #42` 到 `aiant-governance #84` 重新分类为 field-registry-feedback / evidence-boundary / receipt-alignment / scanner-preparation lane。
4. 在 scanner implementation skeleton 之前，先补 AEM 六个子能力驱动的 seed scenarios。
5. 下一步应是：

```text
mmn: draft AEM authority-source event memory construction seed scenarios v0
```

6. scanner implementation skeleton 只能在 AEM 六个子能力的 seed suite 存在之后再推进。

## 显式边界

本文档不授权：

```text
memory write
memory record creation
writeback request
runtime topology path
scheduler route
execution handoff
runtime shadow mode
scanner runtime invocation
formal FIELD_REGISTRY update
accepted schema surface expansion
DRL execution
trading signal
future live execution
```

## Sentinel

```text
AEM_BUSINESS_CAPABILITY_SCENARIO_TAXONOMY_FIELD_REGISTRY_FEEDBACK_BOUNDARY_V0_READY
```
