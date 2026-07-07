# MMN AEM Field Suggestion Maturity Boundary V0

```text
MMN_AEM_FIELD_SUGGESTION_MATURITY_BOUNDARY_V0_READY
```

## 1. 定位

本文件用于澄清 AEM 字段建议在 `aiant-mmn` 中的成熟度边界，尤其是对以下两刀的语义补正：

```text
MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0
MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0
```

本文件不回滚这两刀，也不把它们解释为 runtime、memory、scanner、contracts schema 或 formal field registry 变化。
它只修正术语读取方式：在 AEM-1 至 AEM-6 的真实子场景尚未完成 pressure review、absence test、
evidence / receipt / authority-envelope witness 分离审查之前，从 seed scenario 或 designer discovery lens 得到的字段，
不得被成熟地称为 reviewed candidate field suggestion。

当前应采用的名称是：

```text
provisional_field_suggestion_input
field_suggestion_review_target
seed_scenario_derived_provisional_suggestion
```

只有在经过对应 AEM 子能力的真实场景压力审查之后，才允许晋级为：

```text
reviewed_candidate_field_suggestion
```

## 2. 为什么需要这一刀

上一阶段使用了较宽松的工程命名：

```text
candidate field suggestion
  -> field pressure ledger review checkpoint
  -> candidate field need decision ledger plan
```

该表达容易被误读为：AEM-1 至 AEM-6 的字段已经经过真实子场景验证，并且已经具备进入 need decision record 的资格。
这不是当前事实。

更严格的成熟度链条应改为：

```text
seed-scenario-derived provisional field suggestion inputs
  -> AEM-1..AEM-6 sub-capability pressure reviews
  -> field pressure ledger entries
  -> reviewed candidate field suggestions
  -> candidate field need decision ledger plan
  -> candidate field need decision records, candidate-only
  -> later contracts/governance review
  -> possible formal registry proposal later
```

因此，`candidate field suggestion` 在后续文档中应优先拆成两个阶段：

```text
provisional_field_suggestion_input
reviewed_candidate_field_suggestion
```

## 3. 成熟度层级

| Level | Name | Meaning | May advance to next step? |
|---|---|---|---|
| L0 | `designer_enum_or_discovery_lens` | 设计者枚举或发现镜头，只能作为线索 | no |
| L1 | `provisional_field_suggestion_input` | seed scenario 派生的临时字段建议输入 | only to review |
| L2 | `field_suggestion_review_target` | 被选入某个 AEM 子能力 pressure review 的审查对象 | only after absence test |
| L3 | `field_pressure_ledger_entry` | 已有具体 failure-if-missing、目标影响和最小可审计信息 | may become reviewed suggestion |
| L4 | `reviewed_candidate_field_suggestion` | 经过 AEM 子场景 pressure review 的候选字段建议 | may enter need review |
| L5 | `candidate_field_need_review_entry` | 进入候选字段需求审查，但仍非 registry / schema | may get candidate-only decision |
| L6 | `candidate_field_need_decision_record_candidate_only` | 候选需求决策记录，仍不授权 registry / runtime / memory | may be handed off later |
| L7 | `later_contracts_governance_review_handoff` | 后续 contracts/governance review handoff | not started here |
| L8 | `possible_formal_registry_proposal_later` | 可能的 formal registry proposal | explicitly out of scope |

## 4. 对 #52 / #53 的正确读取

#52 / `MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0` 的正确读取：

```text
field_pressure_ledger_review_checkpoint_scaffold = ready
AEM_1_to_AEM_6_field_validation_completed = false
reviewed_candidate_field_suggestions_available = false
```

#53 / `MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0` 的正确读取：

```text
candidate_field_need_decision_ledger_plan = ready
candidate_field_need_decision_records_created = false
contracts_governance_review_handoff_started = false
```

换言之，#53 只是说明以后怎样做 decision ledger，不表示现在已经生成 candidate need decision records。

## 5. AEM-1 至 AEM-6 的必要审查入口

任何 provisional input 若要晋级为 reviewed candidate field suggestion，必须先进入对应 AEM 子能力的审查入口：

```text
AEM-1 observed_signal_anchoring_pressure_review
AEM-2 authority_source_retrieval_pressure_review
AEM-3 attribution_hypothesis_pressure_review
AEM-4 anti_bias_review_pressure_review
AEM-5 memory_disposition_pressure_review
AEM-6 future_reuse_boundary_pressure_review

AEM_1_observed_signal_anchoring_pressure_review
AEM_2_authority_source_retrieval_pressure_review
AEM_3_attribution_hypothesis_pressure_review
AEM_4_anti_bias_review_pressure_review
AEM_5_memory_disposition_pressure_review
AEM_6_future_reuse_boundary_pressure_review
```

每个审查入口至少要回答：

```text
failure_if_missing_is_concrete
AEM_or_ORSC_target_is_affected
existing_field_substitution_is_not_safe_or_is_explicitly_selected
minimum_auditable_information_is_identified
evidence_receipt_witness_slots_are_separated
authority_envelope_witness_is_required_when admissibility is claimed
```

## 6. AEM-1 的立即后继位置

当前推荐的下一步不是继续 AEM-wide contracts/governance handoff，而是压实第一个子能力：

```text
mmn: add AEM-1 observed signal anchoring pressure review v0
```

这表示：

```text
AEM-wide candidate need decision layer = ready as plan
AEM-wide contracts/governance handoff = deferred
selected bounded delta = AEM-1-specific pressure review
```

## 7. 禁止解释

以下解释必须被拒绝：

```text
unreviewed provisional input -> reviewed_candidate_field_suggestion
seed field list -> candidate_field_need
field pressure checkpoint scaffold -> completed AEM-1..AEM-6 validation
candidate need decision ledger plan -> candidate need decision records created
candidate need decision record -> formal registry entry
candidate need decision record -> contracts schema
candidate need decision record -> scanner implementation
candidate need decision record -> runtime activation
candidate need decision record -> memory write
GVR Intent -> observed_signal_ref
GVR Intent -> attribution_link_ref
Intent / Attribution Candidate -> attribution_link_ref
ordinary evidence -> ORSC witness
receipt -> ORSC witness
authority boolean -> authority source
```

## 8. 保持的理论边界

```text
GVR Display may enter observed signal anchoring.
GVR Possess / Intent remain inference candidates only.
Intent / Attribution Candidate is attribution_hypothesis_pressure_source_ref,
not attribution_link_ref.
ORSC witness = authority envelope.
Candidate field suggestions are not candidate field needs until reviewed.
Unreviewed provisional inputs are not reviewed candidate field suggestions.
Authority booleans are derived summaries only.
```

## 9. 非授权边界

```text
formal_field_registry_update = false
contracts_schema_created = false
scanner_implemented = false
runtime_activation = denied
memory_write = denied
drl_execution_authorized = false
trading_signal_authorized = false
non_executing = true
non_authorizing = true
candidate_only = true
```

## 10. 后续顺序

推荐顺序：

```text
#54 clarify AEM field suggestion maturity boundary
  -> AEM-1 observed signal anchoring pressure review
  -> AEM-1 observed signal anchoring candidate suggestion review checkpoint
  -> AEM-2..AEM-6 pressure reviews
  -> reviewed candidate field suggestions
  -> candidate field need decision records, candidate-only
  -> later contracts/governance review handoff
```
