# MMN SeedBiasAuditContractV0 记忆可见性策略回归 V0（Memory Visibility Policy Regression V0）

- 版本：`mmn_seed_bias_audit_contract_v0_memory_visibility_policy_regression_v0`
- 状态：memory visibility policy regression / preview-only / no memory write / no runtime authority
- 适用范围：`aiant-mmn` / `SeedBiasAuditContractV0`
- 阶段编号：MMN-VB-6A

---

## 1. 文档目的

本文用于为 `MMN_SEED_BIAS_AUDIT_CONTRACT_V0_MEMORY_VISIBILITY_POLICY_V0.md`
增加回归保护。

本 regression 承接：

```text
MMN-VB-6 docs/test: add MMN memory visibility policy for SeedBiasAuditContractV0 v0
Pant-VB-6 Pant evidence reference policy for SeedBiasAuditContractV0
Pant-VB-6A Pant evidence reference policy regression for SeedBiasAuditContractV0
Vant-VB-6 V-ant reference policy for SeedBiasAuditContractV0
Vant-VB-6A V-ant reference policy regression for SeedBiasAuditContractV0
Core-VB-5 core intake support for SeedBiasAuditContractV0
Core-VB-5A core intake support regression for SeedBiasAuditContractV0
G-VB-5 SeedBiasAuditContractV0 post-acceptance governance note
C-VB-12 SeedBiasAuditContractV0 accepted contract schema
C-VB-12A SeedBiasAuditContractV0 accepted contract regression
```

本阶段只增加 MMN memory visibility policy regression：

```text
mmn_memory_visibility_policy_regression_only=True
```

本阶段不做：

```text
memory_visibility_policy_expanded=False
mmn_memory_write_authorized=False
persistent_memory_mutation_authorized=False
memory_persistence_authorized=False
recall_truth_authorized=False
truth_verification_authorized=False
semantic_truth_authorized=False
runtime_enabled=False
runtime_authority_granted=False
worker_coupling_enabled=False
provider_backend_call_enabled=False
model_call_enabled=False
market_signal_authorized=False
reward_authorized=False
action_candidate_authorized=False
strategy_decision_authorized=False
execution_payload_authorized=False
```

---

## 2. Regression target

```text
regression_target=MMNSeedBiasAuditContractV0MemoryVisibilityPolicyV0
regression_target_repo=aiant-mmn
regression_target_stage=MMN-VB-6A
regression_scope=mmn_memory_visibility_policy_regression
memory_visibility_policy_path=docs/memory_visibility/MMN_SEED_BIAS_AUDIT_CONTRACT_V0_MEMORY_VISIBILITY_POLICY_V0.md
```

---

## 3. Regression dimensions

```text
regression_dimension_1=memory_visibility_policy_identity_stable
regression_dimension_2=source_contract_identity_stable
regression_dimension_3=core_vant_pant_reference_chain_stable
regression_dimension_4=preview_only_boundary_preserved
regression_dimension_5=recall_boundary_preserved
regression_dimension_6=authority_invariants_preserved
regression_dimension_7=forbidden_fields_preserved
regression_dimension_8=memory_write_forbidden_preserved
regression_dimension_9=worker_provider_model_forbidden_preserved
regression_dimension_10=no_runtime_authority_preserved
```

---

## 4. Identity invariants

Regression must preserve:

```text
reference_policy_target=SeedBiasAuditContractV0
reference_policy_repo=aiant-mmn
reference_policy_stage=MMN-VB-6
reference_policy_scope=mmn_memory_visibility_policy
source_contract_name=SeedBiasAuditContractV0
source_contract_version=seed_bias_audit_contract_v0
core_intake_name=CoreSeedBiasAuditContractV0IntakeSupportV0
vant_reference_policy=VANT_SEED_BIAS_AUDIT_CONTRACT_V0_REFERENCE_POLICY_V0
pant_evidence_reference_policy=PANT_SEED_BIAS_AUDIT_CONTRACT_V0_EVIDENCE_REFERENCE_POLICY_V0
```

---

## 5. Allowed memory-visibility invariants

MMN may reference the contract only as:

```text
mmn_can_reference_accepted_contract_schema=True
mmn_can_reference_core_intake_support=True
mmn_can_reference_vant_reference_policy=True
mmn_can_reference_pant_evidence_policy=True
mmn_can_reference_post_acceptance_governance_note=True
mmn_can_reference_authority_invariants=True
mmn_can_reference_forbidden_field_policy=True
```

Allowed usage remains:

```text
allowed_use_1=memory_visibility_boundary_reference
allowed_use_2=preview_recall_boundary_note
allowed_use_3=seed_bias_memory_visibility_explanation
allowed_use_4=authority_invariant_memory_explanation
allowed_use_5=forbidden_field_policy_memory_explanation
allowed_use_6=core_vant_pant_reference_chain_note
allowed_output_surface=memory_visibility_note
allowed_output_surface=preview_recall_note
allowed_output_surface=non_persistent_memory_annotation
allowed_output_surface=read_only_memory_boundary_reason
allowed_output_surface=reference_policy_note
```

---

## 6. Forbidden interpretation invariants

Regression must preserve that MMN cannot reference the contract as:

```text
mmn_cannot_reference_as_memory_write_authority=True
mmn_cannot_reference_as_persistent_memory_mutation=True
mmn_cannot_reference_as_recall_truth=True
mmn_cannot_reference_as_truth_verification=True
mmn_cannot_reference_as_runtime_authority=True
mmn_cannot_reference_as_worker_coupling=True
mmn_cannot_reference_as_provider_call=True
mmn_cannot_reference_as_model_call=True
mmn_cannot_reference_as_reward_or_action=True
mmn_cannot_reference_as_strategy_or_execution=True
```

And must preserve:

```text
memory_write_authority=False
persistent_memory_authority=False
recall_truth_authority=False
truth_verification_authority=False
runtime_execution_authority=False
worker_coupling_authority=False
provider_backend_authority=False
model_call_authority=False
reward_action_authority=False
strategy_execution_authority=False
```

---

## 7. Authority invariants

Regression must preserve:

```text
not_execution_authority=True
not_truth_verification=True
not_route_decision=True
not_scheduler_apply=True
not_trade_signal=True
not_market_signal=True
not_reward=True
not_action_candidate=True
not_strategy_decision=True
not_execution_payload=True
feature_only=True
runtime_authority_granted=False
```

---

## 8. Forbidden fields regression

Regression must keep the following fields forbidden in MMN memory visibility output:

```text
truth_verified
truth_verification_certificate
claim_verified
semantic_truth
recall_truth
market_signal
trade_signal
reward_signal
action_candidate
action_prior
strategy_decision
scheduler_apply
execution_payload
production_executor
runtime_authority_granted
memory_write_authorized
persistent_memory_mutation_authorized
memory_persistence_authorized
worker_coupling_enabled
provider_backend_call_enabled
model_call_enabled
canonical_contract_promoted
governance_approval
```

Any future change that permits these fields must fail the regression:

```text
forbidden_truth_field_blocks=True
forbidden_recall_truth_field_blocks=True
forbidden_signal_field_blocks=True
forbidden_reward_action_field_blocks=True
forbidden_strategy_execution_field_blocks=True
forbidden_runtime_authority_field_blocks=True
forbidden_memory_write_field_blocks=True
forbidden_worker_coupling_field_blocks=True
forbidden_provider_model_call_field_blocks=True
forbidden_contract_promotion_field_blocks=True
```

---

## 9. Preview / recall regression

MMN preview / recall boundary note must remain preview-only:

```text
mmn_preview_can_reference_seed_bias_contract=True
mmn_preview_must_remain_preview_only=True
mmn_preview_must_preserve_feature_only=True
mmn_preview_must_not_create_truth=True
mmn_preview_must_not_write_memory=True
mmn_preview_must_not_create_persistent_memory=True
mmn_preview_must_not_create_runtime_authority=True
mmn_preview_must_not_enable_worker_coupling=True
mmn_preview_must_not_call_provider_backend=True
mmn_preview_must_not_call_model=True
```

---

## 10. Downstream non-expansion regression

Regression must preserve:

```text
downstream_consumer_visibility_not_expanded=True
core_runtime_reference_not_authorized=True
vant_provider_reference_not_authorized=True
pant_runtime_reference_not_authorized=True
tft_feature_not_authorized=True
gnn_edge_not_authorized=True
drl_state_or_reward_not_authorized=True
downstream_expansion_requires_review=True
memory_write_requires_review=True
persistent_memory_requires_review=True
worker_coupling_requires_review=True
provider_call_requires_review=True
runtime_expansion_requires_review=True
```

---

## 11. Regression status

```text
mmn_seed_bias_audit_contract_v0_memory_visibility_policy_regression_status=MMN_SEED_BIAS_AUDIT_CONTRACT_V0_MEMORY_VISIBILITY_POLICY_REGRESSION_READY
mmn_memory_visibility_policy_regression_ready=True
memory_visibility_policy_expanded=False
mmn_memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_granted=False
worker_coupling_enabled=False
provider_backend_call_enabled=False
model_call_enabled=False
```

---

## 12. Recommended next stage

```text
recommended_next_stage=G-VB-6
recommended_next_repo=aiant-governance
recommended_next_action=docs/test: add accepted contract downstream reference policy v0
```

备选：

```text
option_1=G-VB-6 docs/test: add accepted contract downstream reference policy v0
option_2=MMN-VB-6B docs/test: add MMN memory write exclusion note for SeedBiasAuditContractV0 v0
option_3=Pant-VB-6B docs/test: add Pant runtime exclusion note for SeedBiasAuditContractV0 v0
```

---

## 13. 一句话结论

```text
MMN-VB-6A adds regression protection for MMN's SeedBiasAuditContractV0 memory visibility
policy. It freezes preview-only memory visibility semantics, recall-boundary semantics,
authority invariants, forbidden fields, memory-write exclusion, persistent-memory exclusion,
worker-coupling exclusion, provider/model-call exclusion, downstream non-expansion, and
no-runtime-authority boundaries.
```
