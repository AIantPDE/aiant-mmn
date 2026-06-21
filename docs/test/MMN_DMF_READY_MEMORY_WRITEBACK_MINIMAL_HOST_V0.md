# MMN DMF-Ready Memory Writeback Minimal Host V0

> 日期：2026-06-21  
> 文档性质：MBI completion checkpoint / DMF-ready minimal host / documentation-only  
> 目标仓库：`AIantPDE/aiant-mmn`  
> 关联前序：
> - `aiant-pant` #597 `docs/test: add pant full-src pyright zero checkpoint v0`
> - `aiant-pant` #598 `docs/test: add pant post-zero business ownership debt ledger v0`
> - `aiant-pant` #599 `docs/test: add pant authority boundary matrix v0`
> - `aiant-pant` #600 `docs/test: add cross-repo DMF readiness minimal host matrix v0`
> - `aiant-vant` #79 `docs/test: add VANT DMF-ready semantic feature provider minimal host v0`
> - `aiant-zant` #35 `docs/test: add ZANT DMF-ready explanation consumer minimal host v0`
> 当前阶段：MBI completion，尚未进入 DMF  
> 核心判断：MMN 必须在 DMF 启动前具备 memory writeback / audit receipt / provenance record 的最小承接位，否则 DMF 的数据、模型、特征反馈与可追溯记忆会断链。

---

## 1. 一句话定位

本 checkpoint 的目标是把 `aiant-mmn` 明确为 DMF 前的记忆写回、审计回执与 provenance record 的最小承接仓。

它不是：

```text
DMF bootstrap
真实 memory writeback
真实长期记忆写入
真实 runtime feedback ingestion
operator approval
scheduler apply
schema surface expansion
```

它是：

```text
MMN_DMF_READY_MEMORY_WRITEBACK_MINIMAL_HOST_V0
= MMN 对 memory writeback / audit receipt / provenance record boundary 的最小宿主位确认
= MBI completion lane
= DMF-ready 前置检查
= documentation-only checkpoint
```

---

## 2. 本 checkpoint 的输入背景

`aiant-pant` #600 已经给出跨仓 DMF readiness 判断：

```text
CROSS_REPO_DMF_READINESS_MINIMAL_HOST_MATRIX_CREATED=True
DMF_BLOCKERS_VISIBLE=True
TARGETED_MBI_COMPLETION_REQUIRED=True

MMN readiness = partial
MMN dmf_blocker = blocked
next_mbi_completion_lane = Core-VB-mmn-dmf-ready-memory-writeback-minimal-host-v0-next
```

`aiant-vant` #79 已确认 semantic / feature / model-provider 的最小承接位。

`aiant-zant` #35 已确认 explanation / evidence / summary consumer 的最小承接位。

这说明：

```text
VANT 可以作为 semantic / feature provider；
ZANT 可以作为 explanation / evidence consumer；
但 DMF 的 provenance、feedback、audit receipt 和 memory writeback 还需要 MMN 承接。
```

本文件即对 MMN blocker 做最小收口。

---

## 3. 本文件范围

本文件只做：

```text
1. 明确 MMN 在 DMF 前的最小业务宿主位。
2. 明确 memory writeback preview boundary。
3. 明确 audit receipt record boundary。
4. 明确 provenance record path。
5. 明确 fail-closed writeback path。
6. 明确 rollback condition。
7. 明确后续代码实现与测试的最小 lane。
```

本文件不做：

```text
真实 memory writeback
真实长期记忆写入
真实反馈 ingestion
真实 provenance store 写入
真实 scheduler apply
真实 operator approval
runtime execution
source authority 迁移
business owner 迁移
schema 扩张
worker activation
DMF 启动
```

---

## 4. 当前阶段状态

本 checkpoint 前：

```text
CURRENT_STAGE=MBI
PANT_LEDGER_MERGED=True
PANT_AUTHORITY_BOUNDARY_MATRIX_CREATED=True
CROSS_REPO_DMF_READINESS_MATRIX_CREATED=True
VANT_DMF_READY_SEMANTIC_FEATURE_PROVIDER_MINIMAL_HOST_DOCUMENTED=True
ZANT_DMF_READY_EXPLANATION_CONSUMER_MINIMAL_HOST_DOCUMENTED=True

MMN_DMF_READY_MINIMAL_HOST_PRESENT=False
READY_FOR_DMF=False
DMF_STARTED=False
```

本 checkpoint 合并后，应改为：

```text
MMN_DMF_READY_MEMORY_WRITEBACK_MINIMAL_HOST_DOCUMENTED=True
MMN_DMF_READY_MINIMAL_HOST_PRESENT=partial
MMN_DMF_BLOCKER_REDUCED=True

READY_FOR_DMF=False
DMF_STARTED=False
```

注意：

```text
partial 表示 MMN 最小承接位已文档化；
并不表示真实 memory writeback / persistent memory store 已经运行。
```

---

## 5. MMN 在 DMF 前的最小职责

MMN 在 MBI → DMF 交界处至少承担以下职责：

```text
memory writeback preview host
audit receipt record host
provenance record host
feedback memory boundary
rollback-aware writeback boundary
fail-closed memory path
```

更具体地说：

| 能力 | 最小职责 | 本 checkpoint 状态 |
|---|---|---|
| Memory writeback preview | 消费 VANT / ZANT / PANT / CORE 的 preview refs，并形成 writeback preview 边界 | documented |
| Audit receipt record | 记录数据、模型、特征、解释路径产生的 audit receipt 引用 | documented |
| Provenance record | 为 DMF 的 data / model / feature pipeline 提供 provenance record 承接位 | documented |
| Fail-closed writeback | 当 authority、contract、receipt 或 rollback 条件不足时 fail closed | documented |
| Rollback condition | 写明未来真实 writeback 的回滚前置条件 | documented |

---

## 6. Memory writeback preview boundary

### 6.1 目标

MMN 必须明确自己是 memory writeback preview 的 owner，而不是让 PANT 的 runtime-facing feedback 或 ZANT 的 explanation output 默认成为 memory 写入事实。

最小边界：

```text
owner_repo=aiant-mmn
boundary_name=memory_writeback_preview_boundary
mode=preview_only
side_effects=False
persistent_write=False
runtime_authority_required=False
writeback_authority_required=False
```

### 6.2 输入

最小输入可以是：

```text
writeback_request_id
semantic_preview_ref
feature_preview_ref
explanation_preview_ref
audit_receipt_ref
provenance_ref
feedback_ref
contract_version
writeback_mode
```

其中：

```text
writeback_mode ∈ {stub, preview_only, dry_receipt_only, persistent_write_pending}
```

当前 checkpoint 只允许：

```text
stub
preview_only
dry_receipt_only
persistent_write_pending_documented_only
```

不允许：

```text
persistent_memory_write
runtime_feedback_auto_ingestion
operator_approval_auto_writeback
```

### 6.3 输出

最小输出应具有：

```text
memory_writeback_preview_id
writeback_status
audit_receipt_refs
provenance_refs
rollback_condition_ref
fail_closed_reason
writeback_trace
```

输出必须满足：

```text
read_side_only=True
side_effects=False
persistent_write=False
no_scheduler_apply=True
no_operator_apply=True
no_runtime_execution=True
```

---

## 7. Audit receipt record boundary

### 7.1 目标

DMF 的数据、模型、特征、解释链路必须留下可审计回执。MMN 需要作为 audit receipt record 的最小承接仓。

最小边界：

```text
owner_repo=aiant-mmn
boundary_name=audit_receipt_record_boundary
mode=record_boundary_only
receipt_mutation=False
persistent_store_write=False
```

### 7.2 最小 receipt 类型

本 checkpoint 不定义完整 receipt schema，但要求后续至少能表达：

```text
source_data_receipt_ref
semantic_preview_receipt_ref
feature_preview_receipt_ref
model_artifact_receipt_ref
explanation_receipt_ref
operator_review_receipt_ref
runtime_preview_receipt_ref
```

### 7.3 不允许事项

在本 checkpoint 内不允许：

```text
真实 receipt store 写入
真实 memory state mutation
真实 runtime feedback mutation
真实 operator approval 写入
schema surface expansion
```

---

## 8. Provenance record path

### 8.1 目标

DMF 的核心不是只产生 artifact，而是让 data / model / feature pipeline 可追溯。

MMN 的 provenance record path 至少应能记录：

```text
input_ref
source_ref
semantic_preview_ref
feature_preview_ref
model_artifact_ref
explanation_ref
audit_receipt_ref
created_by_boundary
contract_version
rollback_condition_ref
```

### 8.2 最小 provenance 约束

每个 memory writeback preview 都必须能回答：

```text
- 它来源于哪个 data / model / feature / explanation artifact？
- 是否只是 preview？
- 是否经过 audit receipt？
- 是否具备 writeback authority？
- 是否具备 rollback condition？
- 是否允许持久写入？
- 是否可进入 DMF？
```

### 8.3 禁止误读

不允许把 provenance record path 误读为：

```text
long_term_memory_state_mutation
runtime_memory_writeback
operator_approved_memory_update
model_feedback_training_signal
```

---

## 9. Fail-closed writeback path

MMN 的最小 writeback path 必须 fail closed。

允许输出：

```text
writeback_status=available_preview
writeback_status=dry_receipt_only
writeback_status=unavailable_fail_closed
writeback_status=blocked_by_missing_receipt
writeback_status=blocked_by_missing_provenance
writeback_status=blocked_by_missing_authority
writeback_status=blocked_by_missing_rollback_condition
```

不允许：

```text
receipt_missing_but_writeback_success=True
provenance_missing_but_memory_updated=True
authority_missing_but_persistent_write=True
rollback_missing_but_memory_mutation=True
```

最小 fail-closed 原则：

```text
如果 audit receipt 不存在，则不得写入 memory；
如果 provenance 不存在，则不得写入 memory；
如果 writeback authority 不明确，则不得持久写入；
如果 rollback condition 不存在，则不得持久写入；
如果 DMF 未开始，则不得把 writeback preview 解释为 DMF memory artifact。
```

---

## 10. Rollback condition

未来真实 memory writeback 前，至少需要：

```text
writeback_authority_grant
audit_receipt_contract
provenance_record_contract
rollback_strategy
idempotency_key
operator_review_policy
failure_replay_policy
data_retention_policy
```

本 checkpoint 只要求这些条件被明确为未来 gate，不要求实现。

最小 rollback 约束：

```text
任何 memory mutation 都必须可解释、可回滚、可重放、可审计。
```

---

## 11. 与 VANT 的边界

VANT 负责：

```text
semantic provider
feature preview
model-provider boundary
semantic provenance output
```

MMN 负责：

```text
memory writeback preview
audit receipt record
provenance memory record
feedback memory boundary
```

二者正确关系：

```text
VANT produces semantic / feature / model-provider preview.
MMN may reference VANT outputs in writeback preview.
MMN must not mutate VANT provider outputs.
MMN must not convert semantic preview into memory truth without separate writeback authority.
```

---

## 12. 与 ZANT 的边界

ZANT 负责：

```text
explanation consumer
evidence consumer
summary / explain output
fallback / fail-closed explanation
```

MMN 负责：

```text
recording audit / provenance / writeback preview references
```

二者正确关系：

```text
ZANT produces explanation / evidence / summary preview.
MMN may reference ZANT outputs for audit receipt / memory writeback preview.
MMN must not treat explanation preview as approved memory update.
```

---

## 13. 与 PANT 的边界

PANT 可以继续作为：

```text
runtime-facing bridge
guarded intake
read-side adapter
sidecar audit host
```

但 PANT 不应继续默认拥有：

```text
memory writeback ownership
persistent memory state mutation
feedback memory authority
provenance memory record ownership
```

PANT 与 MMN 的正确关系：

```text
MMN owns memory writeback / audit receipt / provenance record boundary.
PANT may pass preview refs through guarded read-side / runtime-facing adapter.
PANT must not convert memory preview into runtime execution without separate authority grant.
```

---

## 14. 与 DMF 的关系

本 checkpoint 不启动 DMF，但它减少 DMF blocker。

关系如下：

```text
MMN minimal host documented
→ MMN memory writeback preview boundary clear
→ MMN audit receipt record boundary clear
→ MMN provenance record path clear
→ MMN fail-closed and rollback path clear
→ DMF-B1 可在后续 MBI closure 后消费这些边界
```

DMF 仍需等待：

```text
CORE_DMF_ENTRY_MODULE_HOST_MAP
GOVERNANCE_DMF_ENTRY_POLICY_GATE
CONTRACTS_DMF_MINIMAL_CONTRACT_BOUNDARY
DOWNSTREAM_FUTURE_CONSUMER_BOUNDARY_MATRIX
MBI_CLOSURE_CHECKPOINT
```

---

## 15. 最小验证建议

后续若从 documentation-only 进入代码 checkpoint，建议添加：

```text
tests/test_memory_writeback_preview_boundary_v0.py
tests/test_audit_receipt_record_boundary_v0.py
tests/test_provenance_record_path_v0.py
tests/test_memory_writeback_fail_closed_path_v0.py
tests/test_memory_writeback_rollback_condition_v0.py
```

每个测试应验证：

```text
preview_only=True
side_effects=False
persistent_write=False
missing_receipt_fail_closed=True
missing_provenance_fail_closed=True
missing_authority_fail_closed=True
rollback_condition_required=True
```

---

## 16. MMN readiness 状态变化

本 checkpoint 合并后：

```text
MMN_DMF_READY_MEMORY_WRITEBACK_MINIMAL_HOST_DOCUMENTED=True
MMN_MEMORY_WRITEBACK_PREVIEW_BOUNDARY_DOCUMENTED=True
MMN_AUDIT_RECEIPT_RECORD_BOUNDARY_DOCUMENTED=True
MMN_PROVENANCE_RECORD_PATH_DOCUMENTED=True
MMN_FAIL_CLOSED_WRITEBACK_PATH_DOCUMENTED=True
MMN_ROLLBACK_CONDITION_DOCUMENTED=True
```

但仍保持：

```text
MMN_REAL_MEMORY_WRITEBACK_STARTED=False
MMN_PERSISTENT_MEMORY_MUTATION_ENABLED=False
MMN_RUNTIME_FEEDBACK_INGESTION_ENABLED=False
DMF_STARTED=False
READY_FOR_DMF=False
```

---

## 17. 后续 lane

本 checkpoint 后，建议进入：

```text
Core-VB-downstream-future-consumer-dmf-readiness-boundary-matrix-v0-next
```

用于统一登记：

```text
aiant-tft
aiant-gant
aiant-drl
aiant-marl
```

为：

```text
future_consumer_only
offline_candidate_only
not_connected
not_deciding
not_executing
```

之后再进入：

```text
Core-VB-core-cross-repo-dmf-entry-module-host-map-v0-next
Core-VB-governance-dmf-entry-policy-gate-v0-next
Core-VB-contracts-dmf-minimal-contract-boundary-readiness-v0-next
MBI closure checkpoint
```

---

## 18. 明确结论

```text
本 checkpoint 使 MMN 的 DMF-ready memory writeback / audit receipt / provenance record 最小承接位显性化。
```

它完成的是：

```text
MMN 作为 memory writeback / audit receipt / provenance record owner 的文档化确认；
PANT 不再默认代持 MMN 记忆写回与 provenance 业务意义；
DMF 启动前的 MMN blocker 被部分消解。
```

它没有完成：

```text
真实 memory writeback；
真实长期记忆写入；
真实 feedback ingestion；
真实 DMF bootstrap；
runtime authority grant；
source authority migration；
business ownership migration；
schema expansion。
```

因此，本 checkpoint 合并后的正确状态是：

```text
MMN_DMF_READY_MINIMAL_HOST_PRESENT=partial
MMN_DMF_BLOCKER_REDUCED=True
READY_FOR_DMF=False
DMF_STARTED=False
```
