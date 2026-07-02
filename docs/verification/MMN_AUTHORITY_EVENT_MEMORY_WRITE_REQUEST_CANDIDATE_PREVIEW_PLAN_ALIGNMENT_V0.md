# MMN Authority Event Memory Write Request Candidate Preview Plan Alignment V0

本文定义 MMN Authority Event Memory（AEM）`write request candidate preview plan v0` 的 alignment v0。

本文件的作用，是把此前的 preview plan v0 与以下材料显式对齐：

```text
MMN_AUTHORITY_EVENT_MEMORY_WRITE_REQUEST_CANDIDATE_PREVIEW_PLAN_V0
MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_REQUIREMENT_SCENARIO_FIXTURES_V0
MMN_AUTHORITY_EVENT_MEMORY_CANDIDATE_FIELD_REGISTRY_PROMOTION_OR_DEFERRAL_DECISION_V0
AIANT Capability Activation Governance Pattern Layer 4.5
```

本 alignment 的结论是：

```text
keep_preview_plan_candidate_only
```

也就是说，`write request candidate preview plan v0` 仍然有效，但只作为 candidate-only / preview-only 计划存在。它不能被解释成 write request schema、writeback request、memory record schema、runtime authorization 或 memory write authority。

## 背景

当前 AEM trace 已从原先的：

```text
contracts candidate field registry
  -> mmn draft write request candidate preview plan
```

被补强为：

```text
contracts grant envelope candidate field registry v0
  -> mmn write request candidate preview plan v0
  -> mmn business requirement scenario fixtures v0
  -> contracts candidate field registry promotion-or-deferral decision v0
  -> mmn write request candidate preview plan alignment v0
```

这说明当前 trace 已不再是单纯的 `draft -> draft`，而是经过了业务需求场景反馈和 contracts-side deferral decision 的 candidate-only alignment trace。

## Alignment Decision

```text
preview_plan_v0_remains_valid_as_candidate_only: true
preview_plan_v0_requires_alignment_before_v1: true
formal_field_registry_promotion_allowed: false
runtime_authorization_allowed: false
memory_write_authority_allowed: false
default_on_unresolved_alignment_gap: deny_fail_closed
```

## 为什么需要 Alignment

`write request candidate preview plan v0` 是在正式 field registry promotion 之前创建的。随后补充的业务需求场景样例发现了若干字段和语义缺口，例如：

```text
source_repo
denied_reason
missing_evidence_refs
requested_runtime_path
scope_constraints
scope_mismatch_reason
revocation_refs
expiry_policy_ref
grant_lifecycle_status
canonical_event_hash
dedupe_key
lineage_ref
trace_id
canonical_source_hash
forbidden_claims
cross_repo_boundary_report_ref
```

contracts-side decision v0 已经明确：

```text
defer_formal_field_registry_promotion
```

因此，MMN 侧需要显式说明 preview plan v0 如何继续保持 candidate-only，以及哪些 alignment gap 必须在 v1 或后续 fixtures 前解决。

## Required Alignment Updates Before V1

进入 `write request candidate preview plan v1` 或更具体 fixtures 前，至少需要解决：

```text
1. business_scenario_trace_refs
2. field_feedback_resolution_refs
3. requested_operation_and_scope_semantics
4. revocation_and_expiry_evidence_refs
5. trace_lineage_and_dedupe_fields
6. forbidden_authority_claim_detection
7. core_topology_grant_envelope_preview_dependency
8. grant_decision_receipt_candidate_dependency
```

## Scenario-to-Preview Alignment

本 alignment 将 9 个 business requirement scenario fixtures 映射到 preview plan 的 alignment gap：

```text
missing_authority_grant_envelope_for_downstream_consumption
  -> requires governance report and grant ref gap

read_only_projection_missing_receipts
  -> requires payload-level receipt refs

topology_runtime_path_denied_without_grant
  -> requires topology report and scope constraints

grant_scope_mismatch_denial
  -> requires scope mismatch semantics

revocation_or_expiry_evidence_required
  -> requires grant lifecycle evidence

duplicate_write_candidate_dedupe_required
  -> requires trace lineage and dedupe

candidate_payload_authorization_claim_denied
  -> requires forbidden claim detection

audit_lineage_gap_denied
  -> requires canonical audit lineage

drl_trading_or_future_live_claim_denied
  -> requires cross-repo forbidden claim boundary
```

## Blocked Interpretations

本 alignment 明确阻断以下误读：

```text
write request candidate preview plan v0 treated as write request schema
business scenario fixture treated as runtime shadow mode
contracts deferral decision treated as formal field registry update
candidate field registry treated as authoritative field registry
read-only projection treated as memory write authority
candidate payload summary treated as authority source
grant_decision treated as sufficient authority source
core topology reference treated as runtime path enablement
absence of revocation evidence treated as active authorization
preview alignment treated as runtime implementation
```

## 本次不授权

本文档不授权：

- write request schema；
- writeback request schema；
- memory record schema；
- formal field registry update；
- accepted schema surface expansion；
- grant decision receipt；
- memory write；
- memory record creation；
- writeback request 或 writeback record；
- runtime topology path；
- scheduler route；
- execution handoff；
- runtime shadow mode；
- production scanner enforcement；
- DRL execution；
- trading signal；
- future live execution。

## 下一步

本 alignment 合并后，更合理的下一步是：

```text
core: add MMN authority event memory topology gate grant-envelope preview plan v0
```

随后再进行：

```text
contracts: draft MMN authority event memory grant decision receipt candidate plan v0
```

再之后，MMN 才适合进入更具体的 `write request candidate preview fixtures v1`。
