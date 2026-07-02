# MMN Authority Event Memory 业务需求场景样例 V0

本文定义 MMN Authority Event Memory（AEM）的**非执行型业务需求场景样例**。

本文件的目的，是在正式 field registry 提升之前，引入真实业务形态的需求反馈。这些样例把当前的 `draft -> draft trace` 转换为由业务需求牵引的 trace，同时保持既有的 non-authorizing 边界。

## 状态

- 仓库：`aiant-mmn`
- 范围：仅 `docs + fixtures + regression tests`
- 模式层级：`Layer 4.5`
- 模式名称：`AIANT Capability Activation Governance Pattern`
- 副标题：`Contract-to-Runtime Safety Layers`

## 核心原则

```text
业务语义是真实的。
执行路径为零。
授权能力为零。
副作用为零。
```

## 预期 Trace

```text
contracts grant envelope candidate field registry v0
  -> mmn business requirement scenario fixtures v0
  -> mmn write request candidate preview plan / alignment
  -> contracts candidate field registry promotion-or-deferral decision
  -> formal registry / schema only after explicit promotion
```

中文解释：

```text
contracts grant envelope 候选字段注册表 v0
  -> mmn 业务需求场景样例 v0
  -> mmn write request candidate preview plan / 对齐说明
  -> contracts 候选字段注册表提升或延期决策
  -> 只有在显式 promote 后，才进入正式 registry / schema
```

## 为什么需要这一层

当前 AEM 路径中已经存在：

```text
contracts candidate field registry
mmn write request candidate preview plan
```

如果没有业务需求层，这条 trace 容易表现为：

```text
draft 证明 draft
候选设计反馈候选设计
```

这会带来一个风险：field registry 的形成过度依赖抽象设计，而不是由真实业务需求反推。

本文件引入业务形态的需求样例，用于在任何正式 field registry promotion 之前，回答：

```text
未来如果 AEM 要形成 write request candidate 或 memory candidate，
真实业务场景到底需要哪些字段？
哪些 evidence ref 必须存在？
哪些 blocker / deferral / revocation / expiry 需要表达？
哪些字段只是 derived summary，不能作为 authority source？
当前 candidate field registry 缺什么？
```

这些样例不会激活 runtime 行为。

## 场景样例不是 Runtime Shadow Mode

```text
Business requirement scenario fixture
  = non-executing requirement test asset
  != runtime scenario
  != shadow traffic
  != write request
  != memory record
  != authority source
```

中文解释：

```text
业务需求场景样例
  = 非执行型需求测试资产
  != 运行时场景
  != 影子流量
  != 写请求
  != memory record
  != 授权来源
```

它和 runtime shadow mode 的区别是：

```text
业务需求场景样例：
  使用手工或测试构造的业务场景；
  不接真实 runtime；
  不进入真实运行环境；
  不产生业务副作用；
  只反馈字段需求和证据需求。

runtime shadow mode：
  可能接收真实或镜像运行流量；
  可能在真实 runtime 旁路执行；
  虽然输出不影响主路径，但已经更接近生产运行环境。
```

AEM 当前阶段只允许前者，不允许后者。

## 必须显式保持的非授权项

每个场景样例必须显式将以下值保持为 `false`：

```text
memory_write_authority_granted
memory_record_creation_authorized
writeback_request_authorized
runtime_topology_path_authorized
scheduler_route_authorized
execution_handoff_authorized
runtime_shadow_mode_authorized
drl_execution_authorized
trading_signal_authorized
future_live_execution_authorized
```

这些字段即使存在，也只是边界声明或派生摘要，不是授权来源。

## 场景集合

本 v0 样例集合覆盖 9 类业务需求场景：

1. 下游消费缺少 authority grant envelope。
2. 只读投影缺少 receipt references。
3. 缺少 grant evidence 时 topology runtime path 被拒绝。
4. grant scope mismatch denial。
5. revocation 或 expiry evidence 缺失。
6. duplicate write candidate 需要 dedupe。
7. candidate payload 含有禁止的 authority claim。
8. audit lineage 或 canonical hash 缺口。
9. DRL、trading 或 future live execution claim 被拒绝。

## 场景 1：下游消费缺少 Authority Grant Envelope

业务意图：

```text
当 governance scanner 发现某个下游仓试图消费 AEM accepted surface，
但缺少 authority grant envelope 时，未来是否需要把该事件表达为
authority-boundary memory candidate。
```

当前阶段只允许：

```text
report_requirements_only
deny_fail_closed
```

该场景反馈的字段需求包括：

```text
source_repo
target_contract_family
target_schema_version
governance_scan_report_ref
authority_grant_envelope_ref
denied_reason
blocking_conditions
created_at_utc
```

可能反馈给 candidate field registry 的缺口：

```text
source_repo
denied_reason
```

边界：

```text
A denied downstream consumption event cannot become memory write authority.
```

## 场景 2：只读投影缺少 Receipt References

业务意图：

```text
当 MMN read-only projection 发现缺少 accepted schema receipt 或
accepted family receipt 时，未来是否需要形成 fail-closed memory candidate。
```

该场景反馈的字段需求包括：

```text
read_only_projection_ref
accepted_schema_receipt_ref
accepted_family_receipt_ref
missing_evidence_refs
denied_reason
created_at_utc
```

必须强调：

```text
receipt_refs_present 是 derived summary。
required_evidence_complete 是 derived summary。
decision_basis 中的引用不能替代 payload-level receipt refs。
```

边界：

```text
Decision-basis references cannot substitute for payload-level receipt refs.
```

## 场景 3：缺少 Grant Evidence 时 Topology Runtime Path 被拒绝

业务意图：

```text
当 core topology gate 发现某个 runtime path 试图启用，
但缺少 topology grant evidence 时，未来是否需要形成 topology-boundary memory candidate。
```

该场景反馈的字段需求包括：

```text
core_topology_gate_report_ref
requested_runtime_path
authority_grant_envelope_ref
scope_constraints
blocking_conditions
denied_reason
```

可能反馈给 candidate field registry 的缺口：

```text
requested_runtime_path
scope_constraints
```

边界：

```text
Core topology reference is not runtime path enablement.
```

## 场景 4：Grant Scope Mismatch Denial

业务意图：

```text
当请求的 write operation 超出 grant scope 时，未来是否需要形成
grant_scope_mismatch memory candidate。
```

该场景反馈的字段需求包括：

```text
grant_envelope_id
requested_operation
grant_scope
scope_constraints
scope_mismatch_reason
blocking_conditions
```

必须强调：

```text
grant_decision 是 derived summary。
write_candidate_preview_decision 是 derived summary。
看起来匹配的 grant_decision 不能替代 scope evidence。
```

边界：

```text
A matching-looking grant_decision is not enough without scope evidence.
```

## 场景 5：Revocation 或 Expiry Evidence 缺失

业务意图：

```text
未来任何 grant-backed write candidate 都必须携带 revocation 与 expiry
相关证据需求，不能把“没有发现撤销证据”解释成“授权仍然有效”。
```

该场景反馈的字段需求包括：

```text
grant_envelope_id
revocation_refs
expiry_policy_ref
decision_time_utc
grant_lifecycle_status
blocking_conditions
```

可能反馈给 candidate field registry 的缺口：

```text
revocation_refs
expiry_policy_ref
grant_lifecycle_status
```

边界：

```text
Absence of revocation evidence cannot be read as active authorization.
```

## 场景 6：Duplicate Write Candidate 需要 Dedupe

业务意图：

```text
当同一个 boundary event 被重复 preview 时，未来需要避免形成重复的
memory candidate。
```

该场景反馈的字段需求包括：

```text
source_event_ref
canonical_event_hash
lineage_ref
dedupe_key
existing_candidate_ref
created_at_utc
```

可能反馈给 candidate field registry 的缺口：

```text
canonical_event_hash
dedupe_key
lineage_ref
```

边界：

```text
Dedupe success cannot authorize memory record creation.
```

## 场景 7：Candidate Payload 含有禁止的 Authority Claim

业务意图：

```text
检测 candidate payload 是否试图直接声明 runtime authority 或 memory-write authority。
```

该场景反馈的字段需求包括：

```text
candidate_payload_ref
forbidden_claims
authority_source_refs
blocking_conditions
denied_reason
```

必须强调：

```text
memory_write_authority_granted 是 derived summary。
runtime_authorization_granted 是 derived summary。
candidate payload summary 不是 authority source。
```

边界：

```text
Candidate payload summary is a derived summary, not an authority source.
```

## 场景 8：Audit Lineage 或 Canonical Hash 缺口

业务意图：

```text
未来 memory candidate 必须能够从 contracts、governance、core topology、
read-only projection 等证据链追溯来源。
```

该场景反馈的字段需求包括：

```text
trace_id
canonical_source_hash
contract_receipt_refs
governance_report_ref
topology_report_ref
projection_report_ref
```

可能反馈给 candidate field registry 的缺口：

```text
trace_id
canonical_source_hash
```

边界：

```text
A lineage-complete summary cannot substitute for canonical receipt refs.
```

## 场景 9：DRL / Trading / Future Live Claim 被拒绝

业务意图：

```text
确保 AEM scenario fixtures 不会被解释成 DRL execution、trading signal
或 future live execution authorization。
```

该场景反馈的字段需求包括：

```text
source_repo
forbidden_claims
denied_reason
blocking_conditions
cross_repo_boundary_report_ref
```

必须强调：

```text
drl_execution_authorized 是 derived summary。
trading_signal_authorized 是 derived summary。
future_live_execution_authorized 是 derived summary。
```

边界：

```text
No DRL execution, trading signal, or future live execution may be derived
from AEM scenario fixtures.
```

## Field Registry Feedback 的作用

这些场景可以识别：

```text
missing_fields
ambiguous_fields
derived_summary_fields
evidence_ref_fields
forbidden_authority_interpretations
```

但这些反馈不是正式 field registry。

它们只是后续进行以下决策的输入：

```text
promotion
revision
deferral
denial
```

换句话说：

```text
field_registry_feedback
  != formal field registry
  != docs/FIELD_REGISTRY.md update
  != accepted schema surface
  != runtime authorization
```

## 与 CAGP 的关系

本文件对应：

```text
AIANT Capability Activation Governance Pattern
Contract-to-Runtime Safety Layers
Layer 4.5: Non-Executing Business Requirement Scenario Fixtures
```

在 AEM 链路中，它的位置是：

```text
contracts candidate field registry
  -> mmn business requirement scenario fixtures
  -> mmn write request candidate preview plan / alignment
  -> contracts promotion-or-deferral decision
  -> formal field registry / schema only after explicit promotion
```

## 显式边界

本文档不授权：

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

## Fixture 文件

机器可读 fixture 存储在：

```text
docs/verification/mmn_authority_event_memory_business_requirement_scenario_fixtures_v0.json
tests/fixtures/mmn_authority_event_memory/business_requirement_scenario_fixtures_v0.json
```

## 下一步用途

本文件合并后，下一步可以支持：

```text
contracts: add MMN authority event memory candidate field registry promotion-or-deferral decision v0
```

也可以支持：

```text
mmn: add MMN authority event memory write request candidate preview plan alignment v0
```

但任何下一步都仍必须保持：

```text
candidate != accepted
preview != runtime
scenario fixture != runtime shadow mode
derived summary != authority source
```
