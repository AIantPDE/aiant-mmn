# MMN AEM Authority-Source Seed Scenario Field Derivation Feedback Plan V0

本文定义 `MMN AEM authority-source seed scenario field derivation feedback plan v0` 的 CAGP V3 语义前端对齐修正版。

本文件承接 `MMN_AEM_AUTHORITY_SOURCE_EVENT_MEMORY_CONSTRUCTION_SEED_SCENARIOS_V0`，并根据
`AIANT_CAPABILITY_ACTIVATION_GOVERNANCE_PATTERN_CONTRACT_TO_RUNTIME_SAFETY_LAYERS_V3` 修正字段推导方法。
上一刀已经把 AEM 真实业务能力从旧的 `docs/verification` lane 中分离出来，并放入
`docs/business_capabilities/mmn_authority_event_memory/`。本文件继续保持这个边界：它不是 formal field registry，
不是 contracts schema 草案，也不是 scanner implementation plan；它只说明如何从真实 AEM seed scenario 中逐步提取
field pressure，并在压力足够清楚时形成 candidate field suggestion。

## 状态

```text
repo: aiant-mmn
scope: docs + fixtures + regression tests
path: docs/business_capabilities/mmn_authority_event_memory
mode: field-pressure-ledger-aligned / candidate-suggestion-only / non-executing / non-authorizing
formal_field_registry_update: denied
memory_write: denied
runtime_activation: denied
scanner_implementation: denied
```

## CAGP V3 alignment / GVR semantic front-end 方法论修正

CAGP V3 对本文件的核心修正是：字段不能因为设计者预先枚举出来就进入 `candidate field need`。
枚举法只能作为 discovery lens；真正的字段反馈必须来自真实场景对 AEM / ORSC 目标产生的 field pressure。当 observed signal 来自自然语言时，还必须先经过 GVR Display-level semantic front-end，防止自然语言从 Display 直接跳到 Possess、Intent、attribution 或 memory。

被降级的路径：

```text
designer enum
  -> candidate field need
```

被禁止的反向路径：

```text
candidate field registry
  -> invent scenario to justify existing field
```

本文件采用的 V3 正向路径：

```text
real scenario corpus
  -> raw scenario observation
  -> GVR Display-level semantic front-end, when the source is natural language
  -> observed signal anchor
  -> AEM sub-capability classification
  -> ORSC residual / ordered_next_step / evidence / receipt / authority-envelope witness analysis
  -> field pressure extraction
  -> field pressure ledger
  -> recurring pressure grouping
  -> candidate field suggestion
  -> candidate field need review
  -> contracts/governance review
  -> possible formal registry proposal
```

因此，本文中 AEM-1 到 AEM-6 的字段列表不再被解释为已经成立的候选字段需求，而是
`candidate field suggestions`。它们必须经过 field pressure ledger、recurrence review、naming/grouping review
以及 contracts/governance review，才可能晋级为 `candidate field need`。

## GVR semantic front-end for AEM / 自然语言进入 AEM 的前置语义层

CAGP V3 进一步澄清：`AIANT PDE GVR 投射推断规范` 不应被当成 AEM 字段来源、
field registry 草案或 attribution model。它更准确的位置，是 AEM 处理自然语言 observed signal
之前的 semantic front-end。

GVR 的核心贡献不是给出字段，而是把自然语言进入 AEM 前的推断深度拆成：

```text
Display  = 可观察、可锚定、可复核的外显表达
Possess  = 从 Display 推断出的能力、资源、状态或拥有关系假设
Intent   = 从 Display / Possess 推断出的意图、方向或行动倾向假设
```

在 AEM 中，只有 Display-level material 可以进入 observed signal anchoring。Possess 与 Intent
只能作为 inference proposal、field pressure source 或 later review object，不能直接作为
`observed_signal_ref`、authority event、attribution conclusion、candidate field need 或 memory promotion evidence。

因此，自然语言进入 AEM 的前置链路应为：

```text
raw natural language
  -> GVR Display-level semantic front-end
  -> observed signal anchor
  -> ORSC residual / evidence / receipt / authority-envelope witness
  -> field pressure ledger
  -> candidate field suggestion
  -> candidate field need review
```

AEM 最怕的不是自然语言本身，而是未锚定自然语言从 Display 直接跳到 Intent，再从 Intent
跳到 attribution 或 memory：

```text
raw natural language
  -> unanchored interpretation
  -> projected intent
  -> attribution narrative
  -> memory candidate or promotion claim

internal shortcut name:
  display_to_intent_to_attribution_without_anchor
```

这个路径会绕开 observed signal anchoring、as-of authority retrieval、anti-bias review、receipt trace
与 authority-envelope witness，因此必须 fail-closed。

GVR semantic front-end 只增加自然语言进入 AEM 前的分层防跳跃机制；它不替代 AEM ordered chain，
也不替代 ORSC 的 evidence / receipt / authority-envelope witness。


## Attribution Hypothesis Pressure Layer / 归因假设压力层

`Attribution Candidate` 不应被放入 `observed_signal_ref`，也不应被解释为已经成立的
`attribution_link_ref`。在 CAGP V3 / AEM 对齐语境中，它应被降级为 AEM-3 之前的
`Attribution Hypothesis Pressure Layer`：也就是 GVR Intent-level interpretation 进入
AEM-3 归因审查之前的压力源、假设源与反偏差审查入口。

该层级的推荐命名为：

```text
Attribution Hypothesis Pressure Layer
归因假设压力层
```

它的职责不是生成归因结论，而是把 Intent / attribution candidate 降级为可审查的归因假设压力：

```text
Intent / Attribution Candidate
  -> attribution_hypothesis_pressure_source_ref
  -> field pressure ledger entry
  -> attribution hypothesis review
  -> semantic relevance / alternative event / negative evidence review
  -> AEM-3 attribution link construction only if admissible
```

因此，以下路径必须被拒绝：

```text
Intent / Attribution Candidate
  -> attribution_link_ref

Intent / Attribution Candidate
  -> memory record

Intent / Attribution Candidate
  -> runtime activation claim
```

允许的路径是：

```text
Intent / Attribution Candidate
  -> may trigger attribution review
  -> may require alternative_event_refs
  -> may require negative_evidence_refs
  -> may require semantic_relevance_component
  -> may require attribution_hypothesis_review_receipt_ref
  -> may eventually support, revise, defer, or deny an attribution_link_ref
```

这可以防止 GVR Intent 从自然语言解释冲动直接跳成 AEM attribution / memory。

## 为什么需要这一刀

AEM 业务能力建设不能从“字段是否齐”开始。字段完整性只是下游问题，它回答候选对象是否可表达、可校验、
可对齐或可拒绝。AEM 业务能力场景先回答：

```text
AEM 为什么要构造某类 authority-source event memory？
真实场景中出现了什么拐点、扰动、异常、自然语言信号或失败信号？
哪些权威源事件在 as-of 窗口内可见？
归因链如何构造？
如何防止事后叙事、前视泄漏、选择性取证与伪因果？
候选记忆应晋级、降级、延期还是拒绝？
未来如何复用，同时保持非授权边界？
```

本文件的职责，是在这些业务问题已经由 seed scenarios 初步回答之后，把每个 seed scenario 通过 ORSC-style
residual / ordered_next_step / evidence / receipt / authority-envelope witness 结构转成 field pressure observations，
再形成可复核的 candidate field suggestions。

## 与旧 field-registry-feedback lane 的关系

从 `aiant-mmn #42` 到 `aiant-governance #84` 的旧 lane 已被重新分类为：

```text
field-registry-feedback / evidence-completeness / negative-boundary /
forbidden-interpretation / scanner-preparation lane
```

该 lane 可以保留，但不能再作为 AEM 六个业务子能力已经完成的证据。本文件不回滚旧 lane，也不复用旧 lane 的反向路径。

## Field pressure 判定规则

`field pressure` 不是“某字段看起来有用”，而是：真实场景在完成某个 AEM / ORSC 目标时，因为缺少某类
可表达、可引用、可验证、可回执、可见证或可拒绝的信息，导致流程无法安全推进、无法复盘、无法判定、
无法拒绝或容易误授权。

pressure 针对的对象不是 field registry 本身，而是：

```text
AEM sub-capability target
ORSC ordered_next_step
evidence gate
receipt trace
authority-envelope witness
anti-bias review
promotion / downgrade / deferral / denial decision
future reuse boundary
non-authorizing safety boundary
audit / replay / review
```

最小判定公式：

```text
field_pressure exists
iff
real_scenario_failure_if_missing(information) is concrete,
and the failure affects at least one AEM/ORSC target,
and existing fields cannot safely substitute it,
and the needed information is auditable.
```

缺失测试 / absence test：

```text
如果没有这类信息，真实场景会在哪里失败？
失败影响的是哪个 AEM 子能力或 ORSC target？
已有字段为什么不能安全替代？
最小可审计信息是什么？
该信息是 evidence、receipt、authority-envelope witness、boundary assertion，还是只是 discovery lens？
```

pressure strength：

| Level | Meaning | Handling |
|---|---|---|
| `P0` | no pressure；只是分类、展示或设计者想象 | discovery lens only |
| `P1` | descriptive pressure；缺失降低表达清晰度但不阻塞 gate | observation note |
| `P2` | review pressure；缺失影响人工 review 或复盘 | ledger entry, needs recurrence |
| `P3` | gate pressure；缺失导致 evidence/admissibility/promotion gate 无法判断 | candidate field suggestion |
| `P4` | safety / authority pressure；缺失导致误授权、误归因、前视泄漏或 runtime 边界混淆 | strong candidate field need review |

## Natural-language observed signal anchoring under GVR semantic front-end

`observed_signal_ref` 的对象可能来自自然语言，例如政策措辞变化、叙事集中、review comment cluster、
解释冲突或语义漂移。ORSC 投影的作用不是消灭自然语言，而是防止自然语言场景停留在未锚定叙事。
GVR semantic front-end 在这里负责先把自然语言限制在 Display 层；Possess / Intent 只能作为
inference proposal 或 field pressure source。

自然语言不能直接变成结构化信号、authority source 或 witness。它必须先经过：

```text
raw text preservation
source span anchor
baseline corpus or comparison context
extraction / comparison evidence
detection receipt
authority-envelope witness
```

因此，自然语言型 observed signal 应被处理为：

```text
raw natural language source
  -> GVR Display-level semantic front-end
  -> text/span anchor
  -> observational extraction proposal
  -> baseline comparison evidence
  -> language signal detection receipt
  -> language signal detection authority envelope witness
  -> field pressure ledger entry, if failure-if-missing is concrete
```

LLM 可以作为 extraction proposer 或 summarization assistant，但不能作为 authority source、ORSC witness 或最终 attribution judge。
LLM output 如果无法回连 raw text span、baseline corpus、comparison evidence、receipt 与 authority envelope，就不能作为强 evidence。

禁止的自然语言捷径：

```text
Display label -> authority source
Possess inference -> observed_signal_ref
Intent inference -> attribution conclusion
LLM-extracted intent -> memory promotion evidence
GVR semantic label -> candidate field need without pressure review
```

## ORSC-style 字段压力推导方法

本文件只借用 ORSC V10 的工程化方法，不打开 runtime。

| Step | 中文 | 在本文件中的含义 |
|---|---|---|
| `observe_residual` | 观察剩余差 / 未解释信号 | seed scenario 中的拐点、扰动、异常、自然语言信号、失败信号或未解决解释缺口。 |
| `select_ordered_next_step` | 选择有序下一步 | 在字段推导前先确定下一步应是检测、检索、归因、审计、处置还是复用。 |
| `hydrate_evidence` | 补水证据 / 装载证据 | 检索权威源、raw text span、baseline comparison、receipt、predecessor memory、review 或上下文材料。 |
| `evaluate_evidence_gated_admissibility` | 证据门控可采性判断 | 没有 evidence、as-of 可见性、receipt 或 authority-envelope witness 的场景不得晋级。 |
| `seal_receipt_and_authority_envelope_witness` | 封存 receipt 与 authority-envelope witness | 区分普通 evidence、步骤 receipt 与见证 ordered next step 的 authority envelope。 |
| `extract_field_pressure` | 提取字段压力 | 用 absence test 识别真实场景中缺失某类信息会导致的具体失败。 |
| `record_field_pressure_ledger_entry` | 记录字段压力账本 | 记录 target、failure-if-missing、existing-field insufficiency、minimal information needed。 |
| `derive_candidate_field_suggestion` | 推导候选字段建议 | 只输出 suggestion，不直接声明 candidate field need 或 formal registry。 |
| `classify_field_feedback` | 分类字段反馈 | 标记为 evidence ref、receipt ref、witness ref、derived summary、boundary assertion 或 discovery lens。 |

## ORSC witness 语义校准

在 ORSC V10 语境中，`witness` 不应被理解为普通证据材料。普通观测、baseline comparison、score trace、
placebo/control result、context match 都应归入 `evidence`。`witness` 应指向见证当前 ordered next step 处在
允许边界内的 authority envelope。

因此，本文件将六个 AEM 子业务能力中的 ORSC 投影统一使用：

```text
evidence: 支撑判断或比较的证据引用
receipt: 某个步骤已经发生并可追溯的回执引用
witness: 见证该步骤被允许进入 ordered next step 的 authority envelope 引用
```

## 字段反馈状态

- `discovery_lens_only`
- `field_pressure_observation`
- `candidate_field_suggestion`
- `candidate_field_need_review`
- `evidence_ref_field_suggestion`
- `receipt_ref_field_suggestion`
- `witness_ref_field_suggestion`
- `derived_summary_suggestion`
- `boundary_assertion_suggestion`
- `defer_to_contracts_review`
- `reject_as_authority_source`

这些状态不是 formal registry 状态，只是本 PR 内的 pressure / suggestion 分类。

## AEM 六个子业务能力到字段压力的推导

### AEM-1: 拐点识别能力 / turning point identification

Seed scenario ref: `scenario_1_index_turning_point_policy_shock_candidate`

Pressure target:

```text
AEM-1 target: pin the observed signal before selecting an authority event
```

ORSC 投影：

```text
residual: observed curve change cannot be explained by baseline window alone
ordered_next_step: pin observed signal before selecting authority event
evidence_gate: turning point detection receipt, comparison evidence, and detection authority envelope must exist before retrieval or attribution
evidence: observed_signal_baseline_comparison_evidence_ref
receipt: turning_point_detection_receipt_ref
witness: turning_point_detection_authority_envelope_ref
```

字段压力观察 / field pressure observations：

```text
- without an observed signal anchor, the object to be pinned before retrieval is undefined
- without a baseline comparison evidence ref, the residual cannot be reproduced or reviewed
- without a detection rule ref, the turning point can be selected narratively after the fact
- without a detection receipt, later retrieval or attribution has no auditable start point
- without a detection authority envelope, AEM-1 cannot witness that signal pinning is allowed within boundary
```

候选字段建议 / candidate field suggestions：

```text
observed_signal_ref
turning_point_window
baseline_window_ref
perturbation_kind
detection_rule_ref
observed_signal_baseline_comparison_evidence_ref
turning_point_detection_receipt_ref
turning_point_detection_authority_envelope_ref
```

字段推导边界：

```text
These are candidate field suggestions only.
They are not yet candidate field needs until field-pressure review.
They require later recurrence / pressure / naming / contracts / governance review.
They cannot authorize memory write or runtime activation.
```
### AEM-2: 权威事件检索能力 / authority event retrieval

Seed scenario ref: `scenario_2_authority_source_retrieval_as_of_visibility`

Pressure target:

```text
AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring
```

ORSC 投影：

```text
residual: turning point lacks an authority-source explanation
ordered_next_step: retrieve as-of-visible sources before attribution scoring
evidence_gate: as-of visibility evidence, retrieval audit receipt, and retrieval authority envelope must exist before attribution scoring
evidence: authority_source_visibility_evidence_ref
receipt: retrieval_audit_log_ref
witness: authority_source_retrieval_authority_envelope_ref
```

字段压力观察 / field pressure observations：

```text
- without source and event refs, retrieval cannot identify the authority-source object under review
- without published, retrieved, and as-of-visible times, post-decision visibility cannot be rejected
- without retrieval query and exclusion refs, selective retrieval cannot be audited
- without a retrieval audit receipt, the retrieval step cannot be replayed
- without a retrieval authority envelope, the retrieval step has no ORSC witness for its allowed boundary
```

候选字段建议 / candidate field suggestions：

```text
authority_source_ref
authority_event_ref
published_at_utc
retrieved_at_utc
as_of_visible_at_utc
retrieval_query_set
excluded_source_refs
authority_source_visibility_evidence_ref
retrieval_audit_log_ref
authority_source_retrieval_authority_envelope_ref
```

字段推导边界：

```text
These are candidate field suggestions only.
They are not yet candidate field needs until field-pressure review.
They require later recurrence / pressure / naming / contracts / governance review.
They cannot authorize memory write or runtime activation.
```
### AEM-3: 归因链构造能力 / attribution chain construction

Seed scenario ref: `scenario_3_statistical_revision_attribution_chain`

Pressure target:

```text
AEM-3 target: construct an auditable attribution link without overwriting predecessor memory
```

GVR / Attribution-candidate bridge：

```text
A GVR Intent-level interpretation or attribution candidate may trigger AEM-3 review,
but it is not an attribution link.
It may only become an attribution_hypothesis_pressure_source,
which must be reviewed against predecessor receipt, revision evidence,
alternative event evidence, negative evidence, semantic relevance, and
attribution authority envelope before any attribution_link_ref can be constructed.
```

ORSC 投影：

```text
residual: previous explanation no longer covers revised official data, or an attribution hypothesis remains insufficiently supported
ordered_next_step: hydrate predecessor receipt, review attribution hypothesis pressure, and construct revised link only if admissible
evidence_gate: predecessor receipt, revision evidence, attribution hypothesis review evidence, alternative/negative evidence review, and attribution authority envelope must exist before revising or constructing a memory candidate
evidence: predecessor_receipt_revision_event_evidence_ref
receipt: attribution_link_receipt_ref
witness: attribution_revision_authority_envelope_ref
```

字段压力观察 / field pressure observations：

```text
- without predecessor memory and predecessor receipt refs, revision may overwrite prior memory without lineage
- without revision event evidence, the revised attribution cannot distinguish official revision from narrative update
- without alternative and negative evidence refs, attribution may preserve a single favored explanation
- without attribution_hypothesis_pressure_source_ref and attribution_hypothesis_review_receipt_ref, a GVR Intent-level interpretation may bypass AEM-3 review and be mistaken for attribution_link_ref
- without an attribution link receipt, the revised link cannot be audited or replayed
- without an attribution authority envelope, revision attribution has no ORSC witness for scope-bound admissibility
```

候选字段建议 / candidate field suggestions：

```text
predecessor_memory_candidate_ref
predecessor_receipt_ref
revision_authority_event_ref
revision_event_evidence_ref
predecessor_receipt_revision_event_evidence_ref
attribution_hypothesis_pressure_source_ref
attribution_hypothesis_review_receipt_ref
attribution_link_ref
time_lag_component
semantic_relevance_component
alternative_event_refs
negative_evidence_refs
revision_effect_summary
attribution_link_receipt_ref
attribution_revision_authority_envelope_ref
```

字段推导边界：

```text
These are candidate field suggestions only.
They are not yet candidate field needs until field-pressure review.
They require later recurrence / pressure / naming / contracts / governance review.
They cannot authorize memory write or runtime activation.
A GVR Intent-level interpretation or attribution candidate cannot directly become attribution_link_ref.
```
### AEM-4: 反偏差能力 / anti-bias review

Seed scenario ref: `scenario_4_narrative_risk_anti_bias_audit`

Pressure target:

```text
AEM-4 target: block narrative backfitting and pseudo-causality before promotion
```

ORSC 投影：

```text
residual: candidate explanation may be an overfit narrative
ordered_next_step: apply score trace and placebo/control review before promotion
evidence_gate: anti-bias evidence, review receipt, and anti-bias authority envelope must exist before promotion
evidence: score_trace_placebo_control_review_evidence_ref
receipt: anti_bias_review_receipt_ref
witness: anti_bias_review_authority_envelope_ref
```

字段压力观察 / field pressure observations：

```text
- without score component trace, confidence cannot be decomposed or challenged
- without placebo and control-window evidence, overfit narrative risk cannot be tested
- without alternative and negative evidence penalties, selective causality cannot be penalized
- without anti-bias review receipt, promotion cannot prove bias review occurred
- without an anti-bias authority envelope, the review step has no ORSC witness for allowed review boundary
```

候选字段建议 / candidate field suggestions：

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
score_trace_placebo_control_review_evidence_ref
blind_review_receipt_ref
anti_bias_review_receipt_ref
multiplicity_adjustment_ref
unresolved_bias_risks
anti_bias_review_authority_envelope_ref
```

字段推导边界：

```text
These are candidate field suggestions only.
They are not yet candidate field needs until field-pressure review.
They require later recurrence / pressure / naming / contracts / governance review.
They cannot authorize memory write or runtime activation.
```
### AEM-5: 记忆晋级能力 / memory promotion / downgrade / deferral / denial

Seed scenario ref: `scenario_5_candidate_memory_disposition_decision`

Pressure target:

```text
AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority
```

ORSC 投影：

```text
residual: candidate memory exists but admissibility is unsettled
ordered_next_step: evaluate promotion checklist under scope-bound admissibility
evidence_gate: blocker evidence, promotion decision receipt, and disposition authority envelope are required before disposition
evidence: blocker_and_promotion_checklist_evidence_ref
receipt: promotion_decision_receipt_ref
witness: memory_disposition_authority_envelope_ref
```

字段压力观察 / field pressure observations：

```text
- without checklist and blocker evidence, promotion or denial cannot be justified
- without downgrade, deferral, and denial reasons, non-promotion decisions cannot be audited
- without decision actor and time refs, disposition lineage is incomplete
- without a promotion decision receipt, the disposition step cannot be replayed
- without a disposition authority envelope, memory promotion has no ORSC witness and may be misread as runtime authorization
```

候选字段建议 / candidate field suggestions：

```text
promotion_checklist_ref
blocker_and_promotion_checklist_evidence_ref
promotion_decision
downgrade_reason
deferral_reason
denial_reason
unresolved_blocking_conditions
decision_actor_ref
decision_time_utc
promotion_decision_receipt_ref
memory_disposition_authority_envelope_ref
```

字段推导边界：

```text
These are candidate field suggestions only.
They are not yet candidate field needs until field-pressure review.
They require later recurrence / pressure / naming / contracts / governance review.
They cannot authorize memory write or runtime activation.
```
### AEM-6: 未来复用能力 / future reuse

Seed scenario ref: `scenario_6_future_reuse_non_authorizing_boundary`

Pressure target:

```text
AEM-6 target: support future reuse while preserving non-authorizing boundaries
```

ORSC 投影：

```text
residual: new event resembles prior memory but scope may differ
ordered_next_step: hydrate prior receipt before reuse and check scope
evidence_gate: prior receipt, context match evidence, reuse receipt, and reuse authority envelope must exist before reuse
evidence: prior_receipt_current_context_match_evidence_ref
receipt: reuse_boundary_receipt_ref
witness: reuse_authority_envelope_ref
```

字段压力观察 / field pressure observations：

```text
- without prior memory and prior receipt refs, reuse cannot prove what is being reused
- without current and reuse context refs, semantic resemblance may be mistaken for scope compatibility
- without context mismatch and denied-scope fields, inadmissible reuse cannot be explained
- without a reuse boundary receipt, reuse cannot be audited as a bounded non-authorizing step
- without a reuse authority envelope and non-authorizing statement, future reuse may be misread as runtime authorization
```

候选字段建议 / candidate field suggestions：

```text
prior_memory_candidate_ref
prior_memory_receipt_ref
current_context_ref
reuse_context_ref
prior_receipt_current_context_match_evidence_ref
reuse_allowed_scope
reuse_denied_scope
context_mismatch_reason
memory_lookup_boundary
reuse_boundary_receipt_ref
reuse_authority_envelope_ref
non_authorizing_reuse_statement
```

字段推导边界：

```text
These are candidate field suggestions only.
They are not yet candidate field needs until field-pressure review.
They require later recurrence / pressure / naming / contracts / governance review.
They cannot authorize memory write or runtime activation.
```


## Candidate Field Suggestion Index

| Field suggestion | Derived from | Provisional status | Pressure target |
|---|---|---|---|
| `observed_signal_ref` | `AEM-1` | `evidence_ref_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `turning_point_window` | `AEM-1` | `candidate_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `baseline_window_ref` | `AEM-1` | `evidence_ref_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `perturbation_kind` | `AEM-1` | `candidate_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `detection_rule_ref` | `AEM-1` | `evidence_ref_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `observed_signal_baseline_comparison_evidence_ref` | `AEM-1` | `evidence_ref_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `turning_point_detection_receipt_ref` | `AEM-1` | `receipt_ref_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `turning_point_detection_authority_envelope_ref` | `AEM-1` | `witness_ref_field_suggestion` | AEM-1 target: pin the observed signal before selecting an authority event |
| `authority_source_ref` | `AEM-2` | `evidence_ref_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `authority_event_ref` | `AEM-2` | `evidence_ref_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `published_at_utc` | `AEM-2` | `candidate_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `retrieved_at_utc` | `AEM-2` | `candidate_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `as_of_visible_at_utc` | `AEM-2` | `candidate_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `retrieval_query_set` | `AEM-2` | `candidate_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `excluded_source_refs` | `AEM-2` | `evidence_ref_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `authority_source_visibility_evidence_ref` | `AEM-2` | `evidence_ref_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `retrieval_audit_log_ref` | `AEM-2` | `candidate_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `authority_source_retrieval_authority_envelope_ref` | `AEM-2` | `witness_ref_field_suggestion` | AEM-2 target: retrieve only as-of-visible authority sources before attribution scoring |
| `predecessor_memory_candidate_ref` | `AEM-3` | `evidence_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `predecessor_receipt_ref` | `AEM-3` | `receipt_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `revision_authority_event_ref` | `AEM-3` | `evidence_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `revision_event_evidence_ref` | `AEM-3` | `evidence_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `predecessor_receipt_revision_event_evidence_ref` | `AEM-3` | `evidence_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `attribution_hypothesis_pressure_source_ref` | `AEM-3` | `candidate_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `attribution_hypothesis_review_receipt_ref` | `AEM-3` | `receipt_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `attribution_link_ref` | `AEM-3` | `evidence_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `time_lag_component` | `AEM-3` | `candidate_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `semantic_relevance_component` | `AEM-3` | `candidate_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `alternative_event_refs` | `AEM-3` | `candidate_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `negative_evidence_refs` | `AEM-3` | `evidence_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `revision_effect_summary` | `AEM-3` | `derived_summary_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `attribution_link_receipt_ref` | `AEM-3` | `receipt_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `attribution_revision_authority_envelope_ref` | `AEM-3` | `witness_ref_field_suggestion` | AEM-3 target: construct an auditable attribution link without overwriting predecessor memory |
| `score_component_trace` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `base_score` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `source_tier_component` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `time_lag_component` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `semantic_relevance_component` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `alternative_event_penalty` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `negative_evidence_penalty` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `placebo_test_ref` | `AEM-4` | `evidence_ref_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `control_window_test_ref` | `AEM-4` | `evidence_ref_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `score_trace_placebo_control_review_evidence_ref` | `AEM-4` | `evidence_ref_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `blind_review_receipt_ref` | `AEM-4` | `receipt_ref_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `anti_bias_review_receipt_ref` | `AEM-4` | `receipt_ref_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `multiplicity_adjustment_ref` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `unresolved_bias_risks` | `AEM-4` | `candidate_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `anti_bias_review_authority_envelope_ref` | `AEM-4` | `witness_ref_field_suggestion` | AEM-4 target: block narrative backfitting and pseudo-causality before promotion |
| `promotion_checklist_ref` | `AEM-5` | `evidence_ref_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `blocker_and_promotion_checklist_evidence_ref` | `AEM-5` | `evidence_ref_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `promotion_decision` | `AEM-5` | `candidate_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `downgrade_reason` | `AEM-5` | `candidate_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `deferral_reason` | `AEM-5` | `candidate_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `denial_reason` | `AEM-5` | `candidate_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `unresolved_blocking_conditions` | `AEM-5` | `candidate_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `decision_actor_ref` | `AEM-5` | `evidence_ref_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `decision_time_utc` | `AEM-5` | `candidate_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `promotion_decision_receipt_ref` | `AEM-5` | `receipt_ref_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `memory_disposition_authority_envelope_ref` | `AEM-5` | `witness_ref_field_suggestion` | AEM-5 target: decide promotion, downgrade, deferral, or denial without opening memory write authority |
| `prior_memory_candidate_ref` | `AEM-6` | `evidence_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `prior_memory_receipt_ref` | `AEM-6` | `receipt_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `current_context_ref` | `AEM-6` | `evidence_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `reuse_context_ref` | `AEM-6` | `evidence_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `prior_receipt_current_context_match_evidence_ref` | `AEM-6` | `evidence_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `reuse_allowed_scope` | `AEM-6` | `candidate_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `reuse_denied_scope` | `AEM-6` | `candidate_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `context_mismatch_reason` | `AEM-6` | `candidate_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `memory_lookup_boundary` | `AEM-6` | `candidate_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `reuse_boundary_receipt_ref` | `AEM-6` | `receipt_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `reuse_authority_envelope_ref` | `AEM-6` | `witness_ref_field_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |
| `non_authorizing_reuse_statement` | `AEM-6` | `boundary_assertion_suggestion` | AEM-6 target: support future reuse while preserving non-authorizing boundaries |

## 推导结果如何进入后续 lane

本文件输出的是 field pressure aligned field derivation feedback，不是 registry delta。后续顺序应是：

```text
field pressure observations
  -> field pressure ledger
  -> recurrence / absence-test review
  -> candidate field suggestion grouping
  -> candidate field need review
  -> evidence / receipt / authority-envelope witness requirement review
  -> derived-summary and boundary-field review
  -> contracts candidate field registry feedback plan
  -> governance scanner checklist update only after taxonomy is stable
```

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

字段压力识别、候选字段建议或字段推导成功，不表示 memory write、field registry promotion、scanner implementation 或 runtime activation 就绪。

## Fixture 文件

```text
docs/business_capabilities/mmn_authority_event_memory/mmn_aem_authority_source_seed_scenario_field_derivation_feedback_plan_v0.json
tests/fixtures/business_capabilities/mmn_authority_event_memory/authority_source_seed_scenario_field_derivation_feedback_plan_v0.json
```

## Sentinel

```text
AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0_READY
```

该 sentinel 只表示本文档与 fixture 的 CAGP V3 field pressure / candidate suggestion 对齐计划已就绪。
它不表示 formal field registry、memory write、scanner implementation 或 runtime activation 已就绪。
