# MMN AEM Candidate Field Need Decision Ledger Plan V0

```text
MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0_READY
```

## 1. 定位

本计划承接：

```text
MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0
```

以及其前置来源：

```text
MMN_AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0
```

上一刀把 AEM seed scenario 的 `candidate field suggestion` 放入
field pressure ledger review checkpoint。本刀不把这些建议写入 formal field
registry，也不创建 contracts schema；它只定义一个 candidate field need decision
ledger 的计划形态，用来说明 reviewed pressure 如何在后续被记录为
candidate-only decision。

本刀的链条是：

```text
candidate field suggestion
  -> field pressure ledger review checkpoint
  -> candidate field need decision ledger plan
  -> candidate field need decision record, candidate-only
  -> later contracts/governance review
  -> possible formal registry proposal later
```

当前产物仍然是：

```text
docs + manifest + fixture + regression test only
non-executing / non-authorizing / candidate-only / no memory write
```

## 2. 为什么需要 decision ledger plan

`candidate field suggestion` 不是 `candidate field need`。即使上一刀 review
认为某些 suggestion 具备 P3/P4 pressure，也还需要一个单独的 decision ledger
来记录：

- pressure 是否有 concrete failure-if-missing；
- recurrence 是否足够，或者是否属于 single high-risk P4；
- existing field 是否可以安全替代；
- proposed name / grouping 是否稳定；
- evidence、receipt、authority-envelope witness 要求是否明确；
- derived summary 是否被误当成 authority source；
- 该 decision 是否仍保持 non-authorizing。

因此，本文件只规划 decision ledger，不执行 promotion。

## 3. 明确非目标

本计划不是：

```text
formal field registry update
contracts schema creation
scanner implementation
runtime activation
memory write
candidate field need automatic promotion
```

即使 decision outcome 是
`candidate_need_ready_for_later_contracts_governance_review`，也只表示该字段需求候选
可以进入后续 contracts/governance review。它仍不是 formal registry、accepted schema、
memory record 或 runtime authorization。

## 4. Decision outcome taxonomy

允许的 decision outcome 为：

| Outcome | Meaning |
|---|---|
| `candidate_need_ready_for_later_contracts_governance_review` | 压力已足够进入后续 contracts/governance 复核，但仍非正式字段 |
| `defer_need_until_more_recurrence` | 缺少跨场景复现或重复压力 |
| `defer_need_due_to_naming_or_grouping_ambiguity` | 命名、分组或边界不稳定 |
| `defer_need_due_to_existing_field_substitution_review` | 现有字段可能安全替代，需继续审查 |
| `reject_need_due_to_no_concrete_failure_if_missing` | 无具体 failure-if-missing，拒绝升级 |
| `reject_need_due_to_authority_or_runtime_risk` | 存在 authority/runtime shortcut 风险，拒绝升级 |
| `route_to_contracts_governance_review_without_need_promotion` | action-adjacent 或 schema-adjacent 对象只路由后续复核，不在本刀提升 |

## 5. Minimum decision ledger entry

每个 planned decision row 至少包含：

```text
candidate_need_decision_id
source_checkpoint_ref
source_field_pressure_id
candidate_field_suggestion
proposed_candidate_field_need_name
decision_outcome
decision_basis
pressure_strength
review_disposition
recurrence_requirement
absence_test_gate
existing_field_substitution_gate
orsc_slot
required_evidence_refs
required_receipt_refs
required_authority_envelope_refs
gvr_layer_boundary
derived_summary_boundary
non_authorizing_boundary
later_review_route
must_not_authorize
```

这些字段只是 plan / fixture / test 的决策账本形态，不是 formal schema。

## 6. Decision gates

本 plan 要求 candidate field need decision 至少经过以下 gate：

| Gate | Required question |
|---|---|
| absence_test_gate | 缺少该信息是否造成具体、可复核 failure？ |
| recurrence_or_single_high_risk_p4_gate | 是否跨场景复现，或属于 single high-risk P4？ |
| existing_field_substitution_gate | 现有字段是否可以安全替代？ |
| naming_grouping_gate | 名称、分组、边界是否稳定？ |
| evidence_receipt_authority_envelope_requirement_gate | evidence、receipt、witness 要求是否分离？ |
| derived_summary_boundary_gate | derived summary 是否被误当成 authority source？ |
| non_authorizing_boundary_gate | 是否仍不授权 memory / runtime / scanner / registry？ |

## 7. ORSC witness / authority envelope boundary

本 plan 继续保持：

```text
evidence = 普通证据材料
receipt = 步骤发生的可追溯回执
witness = authority envelope
```

因此，decision row 可以要求 `required_authority_envelope_refs`，但不能把普通
baseline comparison、score trace、review note、semantic summary 或 derived boolean
写成 witness。

任何裸布尔 authority 字段只能是 derived summary：

```text
memory_write_authority_granted = false
runtime_topology_path_authorized = false
drl_execution_authorized = false
trading_signal_authorized = false
```

这些值不能成为 authority source，也不能替代 authority envelope。

## 8. GVR / AEM-3 boundary

必须保持：

```text
GVR Display may enter observed signal anchoring.
GVR Possess / Intent remain inference candidates only.
Intent / Attribution Candidate is attribution_hypothesis_pressure_source_ref,
not attribution_link_ref.
ORSC witness = authority envelope.
Candidate field suggestions are not candidate field needs until reviewed.
```

AEM-3 的正确路径仍是：

```text
Intent / Attribution Candidate
  -> attribution_hypothesis_pressure_source_ref
  -> field pressure ledger entry
  -> attribution hypothesis review
  -> semantic relevance / alternative event / negative evidence review
  -> possible attribution_link_ref only after admissible later review
```

本 plan 明确拒绝：

```text
GVR Intent -> attribution_link_ref
GVR Intent -> memory record
GVR Intent -> runtime activation claim
```

## 9. Planned decision rows

| Decision id | Candidate suggestion | Outcome | Boundary |
|---|---|---|---|
| `aem-cfndl-v0-001` | `authority_envelope_ref` | `candidate_need_ready_for_later_contracts_governance_review` | witness must be authority envelope |
| `aem-cfndl-v0-002` | `attribution_hypothesis_pressure_source_ref` | `candidate_need_ready_for_later_contracts_governance_review` | Intent is pressure source, not link |
| `aem-cfndl-v0-003` | `negative_evidence_refs` | `candidate_need_ready_for_later_contracts_governance_review` | anti-bias evidence, not authority |
| `aem-cfndl-v0-004` | `observed_signal_anchor_ref` | `defer_need_until_more_recurrence` | Display anchor needs recurrence |
| `aem-cfndl-v0-005` | `query_visibility_scope_ref` | `defer_need_due_to_naming_or_grouping_ambiguity` | future reuse naming not stable |
| `aem-cfndl-v0-006` | `promotion_deferral_receipt_ref` | `defer_need_due_to_existing_field_substitution_review` | review_receipt_ref may substitute |
| `aem-cfndl-v0-007` | `attribution_link_ref` | `route_to_contracts_governance_review_without_need_promotion` | not promoted here |
| `aem-cfndl-v0-008` | `designer_enum_placeholder_field` | `reject_need_due_to_no_concrete_failure_if_missing` | designer enum is discovery lens only |
| `aem-cfndl-v0-009` | `gvr_intent_to_attribution_link_ref` | `reject_need_due_to_authority_or_runtime_risk` | forbidden shortcut |

## 10. Explicit denied surfaces

This plan denies the following surfaces:

```text
formal_field_registry_update = false
contracts_schema_created = false
scanner_implemented = false
runtime_activation = denied
memory_write = denied
memory_record_creation_authorized = false
runtime_authorizing = false
drl_execution_authorized = false
trading_signal_authorized = false
candidate_need_decisions_default_to_formal_fields = false
candidate_need_decision_ledger_is_authority_source = false
```

## 11. READY marker

本文件与配套 manifest / fixture / regression test 同时满足时，视为：

```text
MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0_READY
```
