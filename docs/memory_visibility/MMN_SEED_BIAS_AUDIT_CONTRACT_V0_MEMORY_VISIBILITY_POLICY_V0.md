# MMN SeedBiasAuditContractV0 记忆可见性策略 V0（MMN SeedBiasAuditContractV0 Memory Visibility Policy V0）

版本：`mmn_seed_bias_audit_contract_v0_memory_visibility_policy_v0`  
状态：记忆可见性策略 / 仅预览 / 不授权记忆写入 / 不授权运行时权限  
适用范围：`aiant-mmn` / `SeedBiasAuditContractV0`  
阶段编号：MMN-VB-6

---

## 1. 文档目的

本文用于在 `aiant-mmn` 中固定 MMN 对 `SeedBiasAuditContractV0` 的记忆可见性策略（memory visibility policy）。

该策略的核心含义是：

```text
MMN 可以把 SeedBiasAuditContractV0 作为 preview-only 的记忆可见性前置条件与 recall 边界说明来引用；
但不能因为该引用而获得 memory write、persistent memory mutation、truth verification、runtime authority、
worker coupling、provider/model call、reward/action/strategy/execution 等权限。
```

本 policy 承接：

```text
C-VB-12 SeedBiasAuditContractV0 accepted contract schema
C-VB-12A SeedBiasAuditContractV0 accepted contract regression
G-VB-5 SeedBiasAuditContractV0 post-acceptance governance note
Core-VB-5 core intake support for SeedBiasAuditContractV0
Core-VB-5A core intake support regression for SeedBiasAuditContractV0
Vant-VB-6 V-ant reference policy for SeedBiasAuditContractV0
Vant-VB-6A V-ant reference policy regression for SeedBiasAuditContractV0
Pant-VB-6 Pant evidence reference policy for SeedBiasAuditContractV0
Pant-VB-6A Pant evidence reference policy regression for SeedBiasAuditContractV0
```

本阶段只创建 MMN memory visibility policy：

```text
mmn_memory_visibility_policy_only=True
```

本阶段不做：

```text
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

## 2. 引用目标

本策略约束的是 MMN 对 `SeedBiasAuditContractV0` 的引用方式：

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

MMN 可以引用：

```text
mmn_can_reference_accepted_contract_schema=True
mmn_can_reference_core_intake_support=True
mmn_can_reference_vant_reference_policy=True
mmn_can_reference_pant_evidence_policy=True
mmn_can_reference_post_acceptance_governance_note=True
mmn_can_reference_authority_invariants=True
mmn_can_reference_forbidden_field_policy=True
```

MMN 不得将引用解释为：

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

---

## 3. MMN 解释边界

MMN 对 `SeedBiasAuditContractV0` 的解释必须是：

```text
feature_only_precondition=True
memory_visibility_precondition=True
preview_only_reference=True
recall_boundary_reference=True
seed_bias_gate_memory_visibility_reference=True
downstream_visibility_memory_boundary=True
authority_invariant_memory_boundary=True
forbidden_field_policy_memory_boundary=True
```

这表示：该合同只能作为“记忆可见性前置条件”和“召回边界说明”出现，而不能转化为记忆写入、事实确认或运行时授权。

不得解释为：

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

## 4. 允许的 MMN 用途

允许用途：

```text
allowed_use_1=memory_visibility_boundary_reference
allowed_use_2=preview_recall_boundary_note
allowed_use_3=seed_bias_memory_visibility_explanation
allowed_use_4=authority_invariant_memory_explanation
allowed_use_5=forbidden_field_policy_memory_explanation
allowed_use_6=core_vant_pant_reference_chain_note
```

允许输出表面：

```text
allowed_output_surface=memory_visibility_note
allowed_output_surface=preview_recall_note
allowed_output_surface=non_persistent_memory_annotation
allowed_output_surface=read_only_memory_boundary_reason
allowed_output_surface=reference_policy_note
```

换言之，MMN 可以说明“这条内容在记忆可见性层面应如何被看见、被召回、被限制”，但不能把该说明升级为写入记忆或生成事实证明。

---

## 5. 禁止的 MMN 用途

禁止用途：

```text
forbidden_use_1=memory_write_authorization
forbidden_use_2=persistent_memory_mutation
forbidden_use_3=recall_truth_generation
forbidden_use_4=truth_verification_result
forbidden_use_5=worker_coupling_authorization
forbidden_use_6=provider_backend_call_authorization
forbidden_use_7=model_call_authorization
forbidden_use_8=runtime_authority_grant
forbidden_use_9=market_signal_generation
forbidden_use_10=reward_signal_generation
forbidden_use_11=action_candidate_generation
forbidden_use_12=strategy_decision_generation
forbidden_use_13=execution_payload_generation
```

这些禁止项用于防止 MMN 将“可见性 / 召回边界”误读为“记忆写入 / 持久化 / 事实确认 / 执行授权”。

---

## 6. 必须保留的权限不变量

任何 MMN memory visibility note / preview recall note 必须保留：

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

这些不变量说明：`SeedBiasAuditContractV0` 在 MMN 中仍然只是 feature-only 的前置约束，不是事实系统、奖励系统、行为系统或运行时系统。

---

## 7. 禁止字段

MMN memory visibility output 不得新增或转义以下字段：

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

任何出现以上字段的 MMN memory visibility output 必须视为 blocked / invalid reference：

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

## 8. 与 MMN preview / recall 的关系

MMN 可生成 preview / recall boundary note，但必须满足：

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

也就是说，MMN 可以将该合同用于“召回边界说明”，但不能把它作为“召回结果是真”的依据，也不能因此把内容写入持久记忆。

---

## 9. 与下游消费者的关系

该 policy 不自动授权任何下游消费：

```text
downstream_consumer_visibility_not_expanded=True
core_runtime_reference_not_authorized=True
vant_provider_reference_not_authorized=True
pant_runtime_reference_not_authorized=True
tft_feature_not_authorized=True
gnn_edge_not_authorized=True
drl_state_or_reward_not_authorized=True
```

任何 downstream expansion 仍需独立 review：

```text
downstream_expansion_requires_review=True
memory_write_requires_review=True
persistent_memory_requires_review=True
worker_coupling_requires_review=True
provider_call_requires_review=True
runtime_expansion_requires_review=True
```

---

## 10. 记忆可见性策略状态

```text
mmn_seed_bias_audit_contract_v0_memory_visibility_policy_status=MMN_SEED_BIAS_AUDIT_CONTRACT_V0_MEMORY_VISIBILITY_POLICY_READY
mmn_memory_visibility_policy_ready=True
accepted_contract_schema_acknowledged=True
core_intake_support_acknowledged=True
vant_reference_policy_acknowledged=True
pant_evidence_reference_policy_acknowledged=True
post_acceptance_governance_acknowledged=True
mmn_memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_granted=False
worker_coupling_enabled=False
provider_backend_call_enabled=False
model_call_enabled=False
```

---

## 11. 推荐下一阶段

建议下一阶段进入：

```text
recommended_next_stage=MMN-VB-6A
recommended_next_repo=aiant-mmn
recommended_next_action=test: add MMN memory visibility policy regression for SeedBiasAuditContractV0 v0
```

备选：

```text
option_1=MMN-VB-6A test: add MMN memory visibility policy regression for SeedBiasAuditContractV0 v0
option_2=G-VB-6 docs/test: add accepted contract downstream reference policy v0
option_3=Pant-VB-6B docs/test: add Pant runtime exclusion note for SeedBiasAuditContractV0 v0
```

---

## 12. 一句话结论

```text
MMN-VB-6 defines how MMN may reference SeedBiasAuditContractV0 as a preview-only
memory visibility precondition and recall-boundary note. It does not authorize memory
writes, persistent memory mutation, worker coupling, provider/model calls, runtime
authority, truth, signal, reward, action, strategy, scheduler, or execution semantics.
```

中文表述：

```text
MMN-VB-6 固定的是“可见性与召回边界”，不是“记忆写入与事实确认”。
SeedBiasAuditContractV0 可以被 MMN 看见、引用、解释其边界，但不能因此被写入持久记忆、
不能生成 recall truth、不能获得 worker coupling，也不能触发 provider/model/runtime。
```
