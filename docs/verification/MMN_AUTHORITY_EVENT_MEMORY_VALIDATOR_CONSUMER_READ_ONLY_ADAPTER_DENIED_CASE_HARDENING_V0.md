# MMN Authority Event Memory Validator-Consumer Read-Only Adapter Denied Case Hardening V0

> 本文件是 `aiant-mmn` 的 read-only adapter denied case hardening checkpoint。
> 本 PR 会增强现有 read-only adapter stub 的 fail-closed 诊断粒度，
> 但不会把 validator-consumer 提升为 production adapter，也不会授权 memory write、
> runtime consumption、DRL execution、trading signal 或 future live execution。

## 目的

`MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_DENIED_CASE_HARDENING_V0`
用于把前序最小 adapter stub 从少量 denied cases 扩展为更细的 fail-closed 诊断矩阵。

本 hardening 固定三条规则：

```text
MMN validator-consumer read-only validation report is not memory write authority.
Accepted contract surface is not downstream runtime authorization.
Boolean authority fields are derived summaries, not authority sources.
```

中文表达为：

```text
MMN 只读验证报告不等于记忆写入授权。
accepted 合同表面成立，不等于下游运行时消费已经授权。
布尔型 authority 字段只能是派生摘要，不能是授权来源。
```

## Hardened denied reasons

本 PR 要求 adapter stub 显式识别以下 fail-closed reasons：

```text
schema_identity_mismatch
family_identity_mismatch
canonical_hash_mismatch
missing_accepted_schema_receipt
missing_accepted_family_receipt
missing_receipt_refs
missing_receipt_ledger_entry
missing_field_registry_entry
missing_public_export
missing_downstream_policy
missing_core_topology_boundary
missing_governance_scanner_boundary
missing_authority_envelope
authority_envelope_inconsistent
authority_envelope_scope_mismatch
non_empty_missing_evidence
non_empty_blocking_conditions
non_empty_deferral_refs
non_empty_revocation_refs
requested_memory_write_or_execution
memory_write_requested
memory_record_creation_requested
memory_writeback_requested
runtime_consumption_requested
drl_execution_requested
trading_signal_requested
future_live_execution_requested
```

其中 `missing_receipt_refs` 保留为兼容旧测试和旧 fixture 的聚合 reason；
新增的 granular reasons 用于解释具体缺失项。

## Hardened fixture cases

新增 fixture 覆盖：

```text
valid_read_only_payload_still_report_only
missing_public_export_denied
missing_receipt_ledger_entry_denied
missing_field_registry_entry_denied
missing_core_topology_boundary_denied
missing_governance_scanner_boundary_denied
missing_authority_envelope_denied
non_empty_missing_evidence_denied
non_empty_blocking_conditions_denied
non_empty_deferral_refs_denied
non_empty_revocation_refs_denied
authority_summary_true_denied
runtime_consumption_requested_denied
drl_execution_requested_denied
```

所有 denied cases 都必须保持：

```text
allowed_to_write_memory = false
allowed_to_execute = false
fail_closed = true
```

有效的 read-only case 只能产生 report，不能授权写入或执行。

## Source behavior

本 PR 更新：

```text
src/aiant_mmn/mmn_authority_event_memory_validator_consumer_read_only_adapter_v0.py
```

新增或强化：

```text
EXPECTED_FAIL_CLOSED_REASONS
receipt_ledger_entry_present
field_registry_entry_present
public_export_present
core_topology_boundary_present
governance_scanner_boundary_present
required_evidence_complete
```

这些字段只能用于诊断，不是 authority source。

## Explicit non-authorizations

本 PR 不授权：

- production adapter adoption；
- downstream runtime consumption；
- memory write；
- memory record creation；
- writeback request / record；
- DRL execution；
- trading signal；
- future live execution；
- runtime canonicalizer；
- production runtime canonical hash。

## Golden canonical hash

前序 golden fixture canonical SHA256 保持：

```text
dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90
```

本 hardening 不重新计算 production runtime canonical hash。

## Boundary

本 PR 是 read-only adapter denied case hardening。

它更新 source stub、增加 hardening 文档、JSON、fixture 与测试，但不接 memory write、不接 runtime、不创建记录。
