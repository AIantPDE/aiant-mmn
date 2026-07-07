# MMN AEM Field Pressure Ledger Review Checkpoint V0

```text
MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0_READY
```

## 1. 定位

本检查点承接：

```text
MMN_AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0
```

它只把上一轮 AEM seed scenario 中出现的 `candidate field suggestion`
放入 field pressure ledger review。它不会把建议字段直接升级为
`candidate field need`，更不会更新 formal field registry 或 contracts schema。

本检查点的链条是：

```text
candidate field suggestion
  -> field pressure ledger review
  -> candidate field need / defer / reject / substitute decision
  -> later governance / contracts readiness
```

当前产物是 docs + manifest + fixture + regression test only，保持：

```text
non-executing / non-authorizing / candidate-only / no memory write
```

## 2. Review checkpoint scope

本检查点只审查以下压力项：

| Review item | Meaning |
|---|---|
| field pressure ledger entry | 场景压力账本条目 |
| candidate field suggestion | 仍是候选字段建议，不是字段需求 |
| absence test | 缺失该字段时是否能复现失败 |
| failure-if-missing | 字段缺失导致的具体失败 |
| existing field substitution | 是否可由已有字段替代 |
| recurrence / pressure / naming readiness | 复现性、压力强度、命名成熟度 |
| review disposition | review 后的非终局处置 |

本检查点不是：

```text
formal field registry
contracts schema
scanner implementation
runtime activation
memory write
```

## 3. Review input

Review input 来自 AEM seed scenario field derivation feedback plan 的六个子能力：

| AEM sub-capability | Review input role |
|---|---|
| AEM-1 turning point identification | 识别转折点候选字段压力 |
| AEM-2 authority-source retrieval | 识别权威来源检索字段压力 |
| AEM-3 attribution chain construction | 识别归因候选与归因链接边界压力 |
| AEM-4 anti-bias review | 识别负证据、替代事件、反偏差字段压力 |
| AEM-5 memory promotion / downgrade / deferral | 识别晋升/降级/延迟字段压力 |
| AEM-6 future reuse / query-time visibility | 识别未来复用与查询可见性压力 |

## 4. Review output dispositions

允许的 review disposition 为：

| Disposition | Meaning |
|---|---|
| ready_for_candidate_need_review | 可进入候选字段需求复核，但仍非正式字段 |
| defer_until_more_recurrence | 等待更多复现场景 |
| defer_due_to_naming_ambiguity | 命名边界仍不稳定 |
| defer_due_to_existing_field_substitution | 可能由已有字段替代 |
| reject_due_to_no_concrete_failure_if_missing | 缺失失败不具体，拒绝升级 |
| reject_due_to_authority_or_runtime_risk | 存在 authority/runtime 风险，拒绝升级 |
| needs_contracts_governance_review_later | 需要后续 contracts/governance 复核 |

任何 disposition 都不是 formal registry update，也不是 runtime 准入。

## 5. Pressure strength scale

| Strength | Meaning |
|---|---|
| P0 no pressure | 没有可复现字段压力 |
| P1 descriptive pressure | 仅能描述便利性或可读性压力 |
| P2 review pressure | 已有 review 需要，但不具 gate 能力 |
| P3 gate pressure | 缺失字段会影响候选准入/复核 gate |
| P4 safety / authority pressure | 缺失字段会造成 safety 或 authority 风险 |

## 6. Minimum ledger entry fields

每个 field pressure ledger entry 至少包含：

```text
field_pressure_id
source_plan_ref
seed_scenario_ref
aem_sub_capability
candidate_field_suggestion
pressure_target
failure_if_missing
absence_test_result
existing_field_substitution_review
recurrence_observation
pressure_strength
orsc_slot
gvr_layer_if_applicable
review_disposition
review_receipt_ref
non_authorizing_boundary
```

这些字段只用于 review artifact 与 fixture，不形成 formal schema。

## 7. GVR / CAGP V3 boundary

必须保持：

```text
GVR Display may enter observed signal anchoring.
GVR Possess / Intent remain inference candidates only.
GVR is semantic front-end, not replacement of AEM ordered chain.
CAGP field pressure ledger reviews scenario-driven pressure,
not designer-invented fields.
```

因此：

- `Display` 可以进入 observed signal anchoring。
- `Possess` 与 `Intent` 只能作为 inference candidate。
- `Intent / Attribution Candidate` 不能直接成为 `attribution_link_ref`。
- GVR 不能替代 AEM-1 到 AEM-6 的有序 review 链条。

## 8. AEM-3 attribution boundary

AEM-3 必须特别处理：

```text
Intent / Attribution Candidate
  != observed_signal_ref
  != attribution_link_ref
  != attribution_link_receipt_ref
  != memory record
  != runtime activation claim
```

正确路径是：

```text
Intent / Attribution Candidate
  -> attribution_hypothesis_pressure_source_ref
  -> field pressure ledger entry
  -> attribution hypothesis review
  -> semantic relevance / alternative event / negative evidence review
  -> AEM-3 attribution link construction only if admissible
```

本检查点对 AEM-3 相关候选字段只给出非终局 review：

| Candidate field suggestion | Review disposition | Boundary note |
|---|---|---|
| attribution_hypothesis_pressure_source_ref | ready_for_candidate_need_review | GVR Intent 的正确压力入口 |
| attribution_hypothesis_review_receipt_ref | ready_for_candidate_need_review | 记录 review 发生，不是 attribution link |
| alternative_event_refs | ready_for_candidate_need_review | anti-bias review pressure |
| negative_evidence_refs | ready_for_candidate_need_review | anti-bias review pressure |
| semantic_relevance_component | defer_due_to_naming_ambiguity | 评分拆解名需后续治理 |
| attribution_link_ref | needs_contracts_governance_review_later | 只能在 admissible 后构造 |
| attribution_link_receipt_ref | needs_contracts_governance_review_later | 只能作为已构造链接的回执 |
| attribution_revision_authority_envelope_ref | needs_contracts_governance_review_later | ORSC witness 必须是 authority envelope |

## 9. ORSC witness semantics

ORSC 语义必须保持：

```text
evidence = 普通证据材料
receipt = 步骤发生的可追溯回执
witness = authority envelope
```

不能把 baseline comparison、revision evidence、semantic relevance、negative evidence
等普通 evidence 写成 witness。`witness` 只能指 authority envelope。

## 10. Review ledger checkpoint sample

| Field pressure id | Candidate suggestion | AEM | Strength | Disposition |
|---|---|---|---|---|
| aem-fplr-v0-001 | observed_signal_anchor_ref | AEM-1 | P2 | defer_until_more_recurrence |
| aem-fplr-v0-002 | authority_envelope_ref | AEM-2 | P4 | ready_for_candidate_need_review |
| aem-fplr-v0-003 | attribution_hypothesis_pressure_source_ref | AEM-3 | P3 | ready_for_candidate_need_review |
| aem-fplr-v0-004 | attribution_link_ref | AEM-3 | P4 | needs_contracts_governance_review_later |
| aem-fplr-v0-005 | negative_evidence_refs | AEM-4 | P3 | ready_for_candidate_need_review |
| aem-fplr-v0-006 | promotion_deferral_receipt_ref | AEM-5 | P2 | defer_due_to_existing_field_substitution |
| aem-fplr-v0-007 | query_visibility_scope_ref | AEM-6 | P1 | defer_due_to_naming_ambiguity |

## 11. Explicit denied surfaces

This checkpoint denies the following surfaces:

```text
formal_field_registry_update = false
contracts_schema_created = false
scanner_implemented = false
runtime_activation = denied
memory_write = denied
candidate_field_suggestions_default_to_candidate_needs = false
```

## 12. READY marker

本文件与配套 manifest / fixture / regression test 同时满足时，视为：

```text
MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0_READY
```
