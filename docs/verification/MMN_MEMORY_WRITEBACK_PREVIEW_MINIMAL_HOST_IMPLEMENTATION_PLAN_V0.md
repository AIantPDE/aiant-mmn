# MMN Memory Writeback Preview Minimal Host Implementation Plan V0

- 阶段标记：`STAGE-MBI-26`
- 段落标记：`MMN-MBI-B2-P1`
- 来源段落：`MBI-B2-R3`
- Lane：`MBI-BI-B2`
- 仓库：`aiant-mmn`
- 阶段：`Mmn-VB-memory-writeback-preview-minimal-host-implementation-plan-next`
- 状态：`MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_IMPLEMENTATION_PLAN_READY`

## 1. 本轮目的

本轮只在 `aiant-mmn` 中建立 memory-writeback preview 最小宿主位的实施计划。

上游 Core `MBI-B2-R3` 已经完成 ZANT realization review，并正式选择 exactly one following host：

```text
work_item_id=MBI-BI-B2-WI-003-MMN-MEMORY-WRITEBACK-PREVIEW-MINIMAL-HOST
host_repo=aiant-mmn
scope=memory_writeback_preview_minimal_host_implementation_plan
business_surface=memory_writeback_preview
role=FUTURE_MEMORY_WRITEBACK_PREVIEW_HOST_NOT_CONNECTED
```

本计划只定义下一轮允许落地的局部宿主 seam，不创建 production code，不授权 memory write，
不授予 runtime authority。

## 2. 实施计划结论

```text
plan_class=MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_IMPLEMENTATION_PLAN
decision=ENTER_MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_IMPLEMENTATION
implementation_plan_started=True
implementation_plan_completed=True
docs_test_only=True
production_code_changed=False
production_implementation_started=False
minimal_host_implementation_started=False
```

## 3. 下一轮允许实现的最小形状

下一轮只允许实现 repo-local、read-side、reference-only 的 memory-writeback preview 最小宿主位：

```text
host_role=LOCAL_READ_SIDE_REFERENCE_ONLY_MEMORY_WRITEBACK_PREVIEW_HOST
input_posture=repo_local_preview_reference_only
output_posture=memory_writeback_preview_only
memory_write_authorized=False
runtime_authority_granted=False
side_effecting_execution_authorized=False
```

预期候选文件：

```text
src/mmn/contracts/memory_writeback_preview_v0.py
docs/verification/MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_V0.md
tests/test_mmn_memory_writeback_preview_minimal_host_v0.py
```

候选路径用于锁定下一轮范围，不表示本轮已经创建这些文件。

## 4. 计划行为

```text
local_read_side_reference_only_preview_shape
local_mmn_host_seam_only
fail_closed_on_forbidden_execution_fields
no_cross_repo_schema_expansion
no_implicit_fanout
```

## 5. 持续关闭边界

```text
selected_following_work_item_implementation_started=False
mmn_memory_writeback_preview_host_created=False
mmn_memory_writeback_preview_contract_created=False
mmn_memory_writeback_preview_adapter_created=False
mmn_consumption_enabled=False
memory_write_authorized=False
persistent_memory_mutation_authorized=False
pant_runtime_facing_semantic_intake_preview_host_created=False
zant_model_call_enabled=False
provider_dispatch_enabled=False
mbi_implementation_fanout_started=False
mbi_implementation_fanout_authorized=False
dmf_bootstrap_started=False
shared_contract_expansion_started=False
runtime_loader_changed=False
worker_activation_started=False
side_effecting_execution_authorized=False
runtime_authority_granted=False
```

## 6. 明确禁止字段

```text
memory_write_authorized_true
persistent_memory_mutation_authorized_true
runtime_authority_granted_true
route_decision
fetch_command
scheduler_apply
queue_mutation
worker_dispatch
execution_payload
provider_backend_call
model_call
shared_contract_expansion
dmf_bootstrap
```

## 7. 下一阶段

只有本计划 PR 合并、`aiant-mmn/main` 回读和 QRSC receipt 生成完成后，才允许进入：

```text
Mmn-VB-memory-writeback-preview-minimal-host-implementation-next
aiant-mmn
feat/test: add memory writeback preview minimal host v0
```

下一阶段仍然只允许 repo-local、read-side、reference-only 最小宿主位实现；不得启用真实
memory write、下游消费、worker、scheduler、DMF、fanout 或 runtime authority。
