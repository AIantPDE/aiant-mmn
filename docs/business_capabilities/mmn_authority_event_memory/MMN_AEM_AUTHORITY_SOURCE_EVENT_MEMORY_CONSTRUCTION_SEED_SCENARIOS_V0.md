# MMN AEM Authority-Source Event Memory Construction Seed Scenarios V0

本文定义 `MMN AEM authority-source event memory construction seed scenarios v0`。

该文件是 `aiant-mmn` 中 AEM（Authority Event Memory）业务能力的
**原生 seed scenario** 文档。它不是从既有 candidate field registry 反推场景，
而是从真实业务形态中的拐点、扰动、异常、失败信号与权威源事件出发，
用 AEM 六个子业务能力逐步确定候选字段。

## 状态

```text
repo: aiant-mmn
scope: docs + fixtures + regression tests
mode: candidate-only / seed-scenario-only / non-executing / non-authorizing
runtime: denied
memory_write: denied
formal_field_registry_update: denied
scanner_implementation: denied
```

## 为什么需要这一刀

上一条从 `aiant-mmn #42` 到 `aiant-governance #84` 的 lane 已经被重新分类为：

```text
field-registry-feedback / evidence-completeness / negative-boundary /
forbidden-interpretation / scanner-preparation lane
```

它有价值，但不能代表完整的 AEM business capability scenario suite。
它主要回答：

```text
候选对象缺什么字段？
哪些 evidence ref 缺失？
哪些 derived summary 不能当 authority source？
哪些边界必须 fail-closed？
```

本文件开启新的 AEM-native seed scenario lane，先回答：

```text
AEM 为什么需要构造某类 authority-source event memory？
真实场景中出现了什么拐点、扰动、异常或失败信号？
应检索哪些当时可见的权威源事件？
如何构造 turning point 与 authority event 的候选归因链？
如何防止事后叙事、前视泄漏、选择性取证与伪因果？
候选记忆应被晋级、降级、延期还是拒绝？
未来如何复用这段记忆，同时保持非授权边界？
```

只有在这些问题回答之后，才允许反推出 candidate field registry 的字段需求。

## 与 CAGP 的关系

本文件吻合 CAGP 的治理方法论：能力不是从字段表开始，而是从业务能力、
证据链、候选对象、边界与显式 promotion 开始。字段只是下游表达结果。

```text
真实 AEM 场景
  -> AEM 六个子业务能力
  -> ORSC-style residual / evidence / receipt / witness 分解
  -> 候选字段需求
  -> field registry feedback
  -> 后续 contract / governance / scanner plan
```

该文件不声明 CAGP V1.1 的论文结论；它只在 `aiant-mmn` 中落实 AEM 原生业务能力
如何产生候选字段需求。

## ORSC V10 实施方法

本文件使用 ORSC V10 的工程思想作为实施方法，而不是打开 runtime：

```text
Observe residual
  -> select ordered next step
  -> hydrate evidence
  -> evaluate evidence-gated admissibility
  -> seal receipt / witness
  -> derive candidate fields
  -> append audit ledger note
```

对应到 AEM：

```text
Observe residual:
  观察拐点、扰动、异常或失败信号。

Hydrate evidence:
  检索当时可见的权威源、公告、receipt、review 或 predecessor memory。

Evidence-gated admissibility:
  没有 evidence envelope、as-of 可见性、检索审计或 witness 的候选，
  不能进入晋级判断。

Receipt-sealed action:
  每一步只生成文档、fixture 与测试上的 receipt-like reference，
  不生成 memory record 或 runtime side effect。

Authority decision evidence envelope as witness:
  权威源事件、as-of 可见性、归因评分、反偏差审计与处置决策共同构成 witness。

Scope-bound admissibility:
  即使候选记忆未来可复用，也只能用于解释、风险识别、治理复核或扰动理解；
  不能变成 trading signal、DRL action、memory write authority 或 runtime authorization。
```

## AEM 六个子业务能力

| ID | 中文 | English | 作用 |
|---|---|---|---|
| AEM-1 | 拐点识别能力 | turning point identification | 识别值得解释的拐点、扰动、异常或失败信号。 |
| AEM-2 | 权威事件检索能力 | authority event retrieval | 检索 as-of 可见的权威源事件并保留检索审计。 |
| AEM-3 | 归因链构造能力 | attribution chain construction | 构造 turning point 与 authority event 的候选归因链。 |
| AEM-4 | 反偏差能力 | anti-bias review | 抑制事后叙事、前视泄漏、选择性取证和伪因果。 |
| AEM-5 | 记忆晋级能力 | memory promotion / downgrade / deferral / denial | 决定候选记忆的晋级、降级、延期或拒绝。 |
| AEM-6 | 未来复用能力 | future reuse | 让事件记忆可复用但不越权。 |

## Seed Scenarios

### Scenario 1: 指数拐点与政策冲击候选

对应子能力：AEM-1 拐点识别能力。

真实场景形态：

```text
某指数或资产篮子在短窗口内出现跳空、斜率反转或波动率突变，
业务方要求解释该拐点是否值得形成 AEM 候选记忆。
```

ORSC 分解：

```text
residual:
  observed curve change cannot be explained by baseline window alone

ordered_next_step:
  identify the turning point before searching for authority events

evidence_gate:
  no authority event may be selected until the observed signal is pinned

receipt:
  turning_point_detection_receipt_ref

witness:
  observed signal and baseline comparison act as the first ORSC witness
```

逐步反推出字段：

```text
observed_signal_ref
turning_point_window
baseline_window_ref
perturbation_kind
detection_rule_ref
turning_point_detection_receipt_ref
```

边界：

```text
Turning point detection cannot authorize memory write, trading signal,
DRL execution, or runtime activation.
```

### Scenario 2: 权威源事件检索与当时可见窗口

对应子能力：AEM-2 权威事件检索能力。

真实场景形态：

```text
拐点发生后，研究者从央行、监管机构、交易所、统计机构、
公司公告或 AIANT 内部正式 receipt 中检索当时已经可见的候选事件。
```

ORSC 分解：

```text
residual:
  turning point lacks an authority-source explanation

ordered_next_step:
  retrieve sources under as-of visibility before attribution scoring

evidence_gate:
  events published or visible after the decision time are inadmissible

receipt:
  retrieval_audit_log_ref

witness:
  authority decision evidence envelope records source, publication,
  visibility, and scope
```

逐步反推出字段：

```text
authority_source_ref
authority_event_ref
published_at_utc
retrieved_at_utc
as_of_visible_at_utc
retrieval_query_set
excluded_source_refs
retrieval_audit_log_ref
```

边界：

```text
Retrieval success is evidence availability, not attribution success
and not authority to create a memory record.
```

### Scenario 3: 统计修订事件与归因链构造

对应子能力：AEM-3 归因链构造能力。

真实场景形态：

```text
统计机构发布修订数据，导致此前对某次市场或系统拐点的解释需要重新评估。
AEM 需要表达事件、拐点与修订之间的候选归因链。
```

ORSC 分解：

```text
residual:
  previous explanation no longer covers revised official data

ordered_next_step:
  hydrate predecessor receipt and construct revised attribution link

evidence_gate:
  revision cannot overwrite prior memory without predecessor receipt

receipt:
  attribution_link_receipt_ref

witness:
  canonical predecessor receipt and revision event form the witness pair
```

逐步反推出字段：

```text
predecessor_memory_candidate_ref
revision_authority_event_ref
attribution_link_ref
time_lag_component
semantic_relevance_component
alternative_event_refs
negative_evidence_refs
revision_effect_summary
attribution_link_receipt_ref
```

边界：

```text
A revised attribution candidate may downgrade or defer prior memory;
it cannot silently rewrite accepted memory.
```

### Scenario 4: 叙事风险与反偏差审计

对应子能力：AEM-4 反偏差能力。

真实场景形态：

```text
候选事件看起来能解释拐点，但同窗口内存在多个相似公告、
媒体叙事或替代事件。AEM 必须防止事后叙事与选择性取证。
```

ORSC 分解：

```text
residual:
  candidate explanation may be an overfit narrative

ordered_next_step:
  apply scoring trace, placebo/control tests, and review before promotion

evidence_gate:
  promotion is inadmissible without anti-bias receipts

receipt:
  anti_bias_review_receipt_ref

witness:
  score trace plus placebo/control receipts serve as review witnesses
```

逐步反推出字段：

```text
score_component_trace
base_score
source_tier_component
time_lag_component
semantic_relevance_component
alternative_event_penalty
negative_evidence_penalty
placebo_test_ref
control_window_test_ref
blind_review_receipt_ref
multiplicity_adjustment_ref
unresolved_bias_risks
```

边界：

```text
A compelling narrative without anti-bias review must remain candidate-only
or be downgraded.
```

### Scenario 5: 候选事件记忆的晋级、降级、延期或拒绝

对应子能力：AEM-5 记忆晋级能力。

真实场景形态：

```text
AEM 候选记忆完成初步证据链后，需要根据 evidence envelope、
归因评分、审计结果与未解决 blocker 决定其处置状态。
```

ORSC 分解：

```text
residual:
  candidate memory exists but admissibility is not yet settled

ordered_next_step:
  evaluate promotion checklist under scope-bound admissibility

evidence_gate:
  missing envelope or unresolved blocker forces deferral or denial

receipt:
  promotion_decision_receipt_ref

witness:
  authority decision evidence envelope is the ORSC v10 witness
```

逐步反推出字段：

```text
promotion_checklist_ref
promotion_decision
downgrade_reason
deferral_reason
denial_reason
unresolved_blocking_conditions
decision_actor_ref
decision_time_utc
promotion_decision_receipt_ref
```

边界：

```text
Promotion decision preview is not formal accepted memory and cannot
authorize writeback or runtime execution.
```

### Scenario 6: 未来复用与非授权边界

对应子能力：AEM-6 未来复用能力。

真实场景形态：

```text
未来出现相似扰动、类似权威源事件或类似治理失败信号时，
系统可检索既有 AEM 候选记忆帮助解释，但不能把复用解释当作授权或执行信号。
```

ORSC 分解：

```text
residual:
  new event resembles prior memory but scope and context may differ

ordered_next_step:
  hydrate prior receipt before reuse and check scope-bound admissibility

evidence_gate:
  reuse is inadmissible if prior receipt, scope, or context mismatch is missing

receipt:
  reuse_boundary_receipt_ref

witness:
  canonical prior receipt plus current context form a reuse witness pair
```

逐步反推出字段：

```text
prior_memory_candidate_ref
current_context_ref
reuse_context_ref
reuse_allowed_scope
reuse_denied_scope
context_mismatch_reason
memory_lookup_boundary
reuse_boundary_receipt_ref
non_authorizing_reuse_statement
```

边界：

```text
Memory reuse may support interpretation, risk review, or governance review;
it cannot become a trading signal, DRL action, or runtime authorization.
```

## 字段推导原则

本文件不创建 formal field registry。字段只以 candidate field feedback 的方式出现。

```text
seed scenario
  -> AEM sub-capability
  -> ORSC residual / evidence / receipt / witness
  -> candidate field need
  -> later field registry feedback
```

反向路径被禁止：

```text
candidate field registry
  -> invent scenario to justify existing field
```

## 与旧 lane 的关系

本文件不是 `aiant-mmn #42` 的补丁，而是新的 AEM-native seed scenario 起点。
旧 lane 保留为 field-registry-feedback / governance-boundary / scanner-preparation。
本文件提供未来重新派生字段需求的上游基础。

## 显式非授权边界

以下值在本文件语境中必须保持为 false：

```text
memory_write_authority_granted = false
memory_record_creation_authorized = false
writeback_request_authorized = false
runtime_topology_path_authorized = false
scheduler_route_authorized = false
execution_handoff_authorized = false
runtime_shadow_mode_authorized = false
drl_execution_authorized = false
trading_signal_authorized = false
future_live_execution_authorized = false
```

这些字段即使出现在 fixture 中，也只是边界声明或派生摘要，不是授权来源。

## Fixture 文件

```text
docs/verification/mmn_aem_authority_source_event_memory_construction_seed_scenarios_v0.json
tests/fixtures/mmn_authority_event_memory/authority_source_event_memory_construction_seed_scenarios_v0.json
```


## Business capability path boundary

This artifact is intentionally stored under:

```text
/docs/business_capabilities/mmn_authority_event_memory/
```

It is not stored under `docs/verification/`, because this lane is no longer a
mixed verification / field-registry-feedback lane. It is the first MMN-native
business capability construction lane for AEM authority-source event memory.

The corresponding test and fixture paths are also separated:

```text
tests/business_capabilities/test_mmn_aem_authority_source_event_memory_construction_seed_scenarios_v0.py
tests/fixtures/business_capabilities/mmn_authority_event_memory/authority_source_event_memory_construction_seed_scenarios_v0.json
```

This path boundary prevents the AEM six-subcapability seed scenario suite from
being confused with the earlier #42-to-#84 field-registry-feedback,
evidence-boundary, receipt-alignment, and scanner-preparation lane.

The path boundary is documentation and test organization only. It does not
authorize memory write, writeback request, scanner implementation, formal field
registry promotion, runtime topology path, scheduler route, execution handoff,
DRL execution, trading signal, or future-live execution.

## Sentinel

```text
AEM_AUTHORITY_SOURCE_EVENT_MEMORY_CONSTRUCTION_SEED_SCENARIOS_V0_READY
```

该 sentinel 只表示本文档与 fixture 的 seed-scenario 说明已就绪。
它不表示 memory write、field registry promotion、scanner implementation 或 runtime activation 已就绪。
