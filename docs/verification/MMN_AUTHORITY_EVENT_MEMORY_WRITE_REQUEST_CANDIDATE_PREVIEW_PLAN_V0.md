# MMN Authority Event Memory Write Request Candidate Preview Plan V0

> 本文件是 `aiant-mmn` 的 write request candidate preview plan v0。
> 本 PR 只创建计划、JSON、fixture 与回归测试；不创建 write request schema，
> 不创建 writeback request / record，不创建 memory record，也不授权 memory write。

## 当前定位

```text
write request candidate preview plan = preview design plan
write request candidate preview plan != write request schema
write request candidate preview plan != writeback request
write request candidate preview plan != memory record
write request candidate preview plan != memory write authority
write request candidate preview plan != runtime authorization
```

中文表达为：

```text
write request candidate preview plan 是预览设计计划；
它不等于写入请求 schema；
它不等于 writeback request；
它不等于 memory record；
它不等于记忆写入授权；
它不等于运行时授权。
```

## 依赖链路

```text
aiant-mmn:
  read-only adapter report projection v0
  read-only adapter report projection fixtures v1

aiant-contracts:
  write authority grant envelope plan v0
  grant envelope candidate field registry v0

aiant-governance:
  scanner check-path preview CLI skeleton v0

aiant-core:
  topology gate denied fixtures v1
```

## Candidate field categories

```text
identity_and_lineage
read_only_source_refs
grant_candidate_refs
operation_request
payload_boundary
evidence_refs
decision_summary
blocking_and_lifecycle
audit_and_trace
```

## Candidate field table

| Field | Category | Value kind | Authority role |
| --- | --- | --- | --- |
| `write_request_candidate_id` | `identity_and_lineage` | `string` | `identifier_only` |
| `write_request_candidate_version` | `identity_and_lineage` | `string` | `version_marker` |
| `source_read_only_projection_ref` | `read_only_source_refs` | `string` | `mmn_read_only_projection_reference` |
| `grant_envelope_candidate_ref` | `grant_candidate_refs` | `string` | `grant_candidate_reference` |
| `grant_envelope_candidate_field_registry_ref` | `grant_candidate_refs` | `string` | `candidate_registry_reference` |
| `requested_memory_operation` | `operation_request` | `enum` | `operation_descriptor` |
| `candidate_payload_digest` | `payload_boundary` | `sha256` | `payload_digest_descriptor` |
| `candidate_payload_summary` | `payload_boundary` | `object` | `derived_summary_not_authority_source` |
| `required_evidence_refs` | `evidence_refs` | `array` | `required_evidence_manifest` |
| `receipt_refs` | `evidence_refs` | `object` | `receipt_reference_manifest` |
| `governance_scanner_preview_ref` | `evidence_refs` | `string` | `governance_preview_reference` |
| `core_topology_gate_preview_ref` | `evidence_refs` | `string` | `topology_preview_reference` |
| `write_candidate_preview_decision` | `decision_summary` | `enum` | `derived_summary_not_authority_source` |
| `write_candidate_preview_basis` | `decision_summary` | `object` | `evidence_trace_summary` |
| `blocking_conditions` | `blocking_and_lifecycle` | `array` | `deny_condition_manifest` |
| `deferral_refs` | `blocking_and_lifecycle` | `array` | `deferral_reference_manifest` |
| `revocation_refs` | `blocking_and_lifecycle` | `array` | `revocation_reference_manifest` |
| `expiry_policy` | `blocking_and_lifecycle` | `object` | `expiry_scope_limiter` |
| `preview_output_ref` | `audit_and_trace` | `string` | `preview_report_reference` |
| `created_at_utc` | `audit_and_trace` | `datetime_utc` | `audit_timestamp` |

## Preview phases

```text
phase_0_read_only_projection_input
phase_1_grant_candidate_reference
phase_2_preview_request_assembly
phase_3_governance_and_topology_evidence
phase_4_preview_output_report
```

## Negative cases

```text
missing read-only projection
missing grant envelope candidate
missing candidate field registry
missing governance scanner preview
missing core topology preview
non-empty blockers
memory write authority claim
writeback record claim
DRL / trading / future live execution claim
```

## Authority rules

```text
Read-only projection is not memory write authority.
Candidate payload summary is a derived summary, not an authority source.
Boolean authority fields are derived summaries, not authority sources.
Accepted contract surface is not downstream runtime authorization.
Core topology reference is not runtime path enablement.
Missing evidence defaults to deny fail-closed.
```

## Explicit non-authorizations

本 PR 不授权：

- write request schema creation；
- writeback request schema creation；
- memory record schema creation；
- production adapter adoption；
- downstream runtime consumption；
- memory write；
- memory record creation；
- writeback request / record；
- runtime topology path；
- scheduler route；
- execution handoff；
- writeback route；
- DRL execution；
- trading signal；
- future live execution；
- runtime canonicalizer；
- production runtime canonical hash。

## Golden canonical hash

```text
dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90
```

## Boundary

本 PR 是 docs + fixtures + regression tests only。
它只把 MMN 从 read-only projection 推进到 write request candidate preview 的计划层，
不进入实际 memory write。
