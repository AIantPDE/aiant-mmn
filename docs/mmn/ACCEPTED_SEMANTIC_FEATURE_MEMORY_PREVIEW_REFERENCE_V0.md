# Accepted Semantic Feature Memory Preview Reference V0

- 版本：`accepted_semantic_feature_memory_preview_reference_v0`
- 状态：MMN memory preview reference / accepted semantic feature surface / no memory write authority
- 适用仓库：`aiant-mmn`
- 阶段编号：Mmn-VB-next
- 当前基准：after `Pant-VB-next` merged
- 关联 accepted contract：`BiasAuditedSemanticFeatureViewContractV0`
- 上游治理来源：`G-VB-8 downstream adoption decision ledger v0`
- 下一计划阶段：`Zant-VB-next`

---

## 1. 文档目的

本文用于在 `aiant-mmn` 中新增 accepted semantic feature memory preview reference v0。

C-VB-14Q 已经将 `BiasAuditedSemanticFeatureViewContractV0` 提升为 accepted
contract family。G-VB-8 对 `aiant-mmn` 的初始结论是：

```text
target_repo=aiant-mmn
decision_status=approved_for_preview_only
adoption_boundary=memory_preview_reference_without_write
memory_write_authorized=False
```

因此，本阶段在 `aiant-mmn` 中只做 memory preview reference，不做 persistent
memory mutation，不做 memory write，不做 worker coupling，不创建 formal execution
payload。

本阶段只新增：

```text
accepted_semantic_feature_memory_preview_reference_only=True
accepted_semantic_feature_memory_preview_reference_created=True
target_contract=BiasAuditedSemanticFeatureViewContractV0
```

本阶段不做：

```text
mmn_memory_preview_adapter_created=False
mmn_runtime_memory_write_enabled=False
mmn_persistent_memory_mutation_authorized=False
runtime_authority_granted=False
memory_write_authorized=False
persistent_memory_mutation_authorized=False
formal_execution_payload_enabled=False
execution_payload_enabled=False
worker_coupling_enabled=False
provider_backend_call_enabled=False
model_call_enabled=False
```

---

## 2. Reference target

```text
reference_target=BiasAuditedSemanticFeatureViewContractV0
reference_target_repo=aiant-mmn
reference_target_stage=Mmn-VB-next
reference_scope=accepted_semantic_feature_memory_preview_reference
reference_payload_path=mmn/references/accepted_semantic_feature_memory_preview_reference_v0.json
source_contract_stage=C-VB-14Q
source_governance_stage=G-VB-8
source_governance_decision_status=approved_for_preview_only
```

该 reference 不要求 `aiant-mmn` 本地存在 `aiant-contracts`、`aiant-governance`、
`aiant-core`、`aiant-vant` 或 `aiant-pant` 仓的文件副本。它只记录跨仓 accepted
surface 的引用目标与 MMN memory preview 边界。

---

## 3. Memory preview reference boundary

`aiant-mmn` 可以引用 accepted semantic feature surface，但只能作为 memory preview
reference：

```text
mmn_memory_preview_reference_allowed=True
mmn_preview_mapping_planned=True
mmn_memory_preview_adapter_created=False
mmn_runtime_memory_write_enabled=False
mmn_persistent_memory_mutation_authorized=False
mmn_execution_payload_enabled=False
```

该 reference 不能被解释为：

```text
memory_write_authorized=True
persistent_memory_mutation_authorized=True
formal_execution_payload_enabled=True
execution_payload_enabled=True
worker_coupling_enabled=True
runtime_authority_granted=True
```

---

## 4. Accepted contract reference

```text
accepted_contract_name=BiasAuditedSemanticFeatureViewContractV0
accepted_contract_version=v0
accepted_contract_family=bias_audited_semantic_feature_view
accepted_contract_registry_status=accepted_contract_family_registered
accepted_contract_runtime_authority_granted=False
stable_cross_repo_contract_surface=True
mmn_reference_allowed=True
mmn_memory_preview_reference_allowed=True
mmn_reference_grants_memory_write=False
mmn_reference_grants_persistent_mutation=False
mmn_reference_grants_execution_payload=False
```

---

## 5. Memory preview review dimensions

```text
review_dimension_1=contract_identity
review_dimension_2=schema_surface_reference
review_dimension_3=memory_preview_boundary
review_dimension_4=preview_mapping_boundary
review_dimension_5=memory_write_boundary
review_dimension_6=persistent_mutation_boundary
review_dimension_7=execution_payload_boundary
review_dimension_8=rollback_or_deferral_path
```

All future memory preview mapping work should explicitly bind these dimensions.

---

## 6. Minimum memory preview reference fields

```text
required_reference_field_1=reference_id
required_reference_field_2=reference_version
required_reference_field_3=target_contract
required_reference_field_4=target_contract_family
required_reference_field_5=source_contract_stage
required_reference_field_6=source_governance_stage
required_reference_field_7=mmn_adoption_boundary
required_reference_field_8=memory_preview_reference_dimensions
required_reference_field_9=authority_flags
required_reference_field_10=next_memory_preview_mapping_review_required
required_reference_field_11=reason_codes
```

---

## 7. Memory preview mapping review requirement

Because G-VB-8 approves MMN only for preview reference, MMN must not skip memory preview
mapping review before write or persistent mutation use.

```text
next_memory_preview_mapping_review_required=True
memory_preview_mapping_review_required_before_write=True
memory_preview_mapping_review_required_before_persistent_mutation=True
memory_preview_mapping_review_required_before_execution_payload=True
allowed_next_work_1=docs/test accepted semantic feature memory preview mapping reference v0
allowed_next_work_2=docs/test mmn accepted semantic feature preview fixture v0
allowed_next_work_3=docs/test mmn memory-write denial fixture v0
blocked_until_review_1=memory_write
blocked_until_review_2=persistent_memory_mutation
blocked_until_review_3=formal_execution_payload
blocked_until_review_4=runtime_execution
blocked_until_review_5=worker_coupling
```

---

## 8. Authority flags

```text
runtime_authority_granted=False
memory_write_authorized=False
persistent_memory_mutation_authorized=False
preview_only=True
formal_execution_payload_enabled=False
runtime_execution_enabled=False
provider_backend_call_enabled=False
model_call_enabled=False
worker_coupling_enabled=False
scheduler_apply_enabled=False
execution_payload_enabled=False
```

---

## 9. MMN-specific notes

This accepted semantic feature contract may eventually support:

```text
future_use_1=MMN memory preview mapping
future_use_2=MMN preview-only citation or recall reference
future_use_3=MMN memory-write denial regression
future_use_4=MMN downstream preview boundary validation
```

But this PR only creates reference metadata:

```text
mmn_memory_preview_adapter_created=False
memory_write_path_created=False
persistent_mutation_path_created=False
execution_path_created=False
worker_coupling_created=False
```

---

## 10. Reference status

```text
accepted_semantic_feature_memory_preview_reference_status=ACCEPTED_SEMANTIC_FEATURE_MEMORY_PREVIEW_REFERENCE_READY
accepted_semantic_feature_memory_preview_reference_ready=True
accepted_semantic_feature_memory_preview_reference_created=True
mmn_adoption_boundary=memory_preview_reference_without_write
next_memory_preview_mapping_review_required=True
memory_write_authorized=False
persistent_memory_mutation_authorized=False
execution_payload_enabled=False
worker_coupling_enabled=False
```

---

## 11. Targeted pytest smoke output

When running targeted pytest with `-s`, the test suite prints:

```text
MMN_VB_NEXT_ACCEPTED_SEMANTIC_FEATURE_MEMORY_PREVIEW_REFERENCE_READY
target_contract=BiasAuditedSemanticFeatureViewContractV0
mmn_adoption_boundary=memory_preview_reference_without_write
next_memory_preview_mapping_review_required=True
memory_write_authorized=False
persistent_memory_mutation_authorized=False
execution_payload_enabled=False
```

This print marker is for local review visibility only. It is not runtime behavior.

---

## 12. Recommended next stage

```text
recommended_next_stage=Zant-VB-next
recommended_next_repo=aiant-zant
recommended_next_action=docs/test: add accepted semantic feature explanation reference v0
```

备选：

```text
option_1=Zant-VB-next docs/test: add accepted semantic feature explanation reference v0
option_2=Mmn-VB-mapping-next docs/test: add accepted semantic feature memory preview mapping reference v0
option_3=Pant-VB-boundary-next docs/test: add accepted semantic feature local runtime boundary review v0
```

---

## 13. 一句话结论

```text
Mmn-VB-next adds an accepted semantic feature memory preview reference for
BiasAuditedSemanticFeatureViewContractV0 in aiant-mmn. It records the accepted
contract surface and MMN preview-only boundary while preserving no-memory-write,
no-persistent-mutation, no-formal-execution-payload, and no-worker-coupling semantics.
```
