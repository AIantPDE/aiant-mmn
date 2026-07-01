# MMN Authority Event Memory Validator-Consumer Read-Only Adapter Plan V0

> 本文件是 `aiant-mmn` 的 docs/test-only validator-consumer read-only adapter plan。
> 它只定义 MMN 如何以只读验证者身份消费 `MMNAuthorityEventMemoryAcceptedV1` 的计划边界。
> 本文件不实现生产 adapter、不写 memory、不创建 memory record、不启用 runtime consumption、
> 不授权 DRL execution、trading signal 或 future live execution。

## 目的

`MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_PLAN_V0`
用于把 contracts / governance / core 已完成的边界，转换成 `aiant-mmn` 侧的只读消费计划。

本计划固定一条规则：

```text
MMN validator-consumer is read-only validation, not memory write authority.
```

中文表达为：

```text
MMN validator-consumer 只代表只读验证，不代表记忆写入授权。
```

同时继续继承前序边界规则：

```text
Accepted contract surface is not downstream runtime authorization.
Core topology reference is not runtime path enablement.
Boolean authority fields are derived summaries, not authority sources.
```

中文表达为：

```text
accepted 合同表面成立，不等于下游运行时消费已经授权。
core 拓扑引用成立，不等于运行时路径已经启用。
布尔型 authority 字段只能是派生摘要，不能是授权来源。
```

## 前序依赖

本计划假定以下前序 PR 已经完成或正在进入合并流程：

1. `aiant-contracts`：MMN Authority Event Memory accepted schema promotion execution v0；
2. `aiant-contracts`：downstream adoption boundary plan v0；
3. `aiant-governance`：downstream consumption scanner boundary v0；
4. `aiant-core`：downstream topology boundary v0。

本文件不重新定义 contracts schema / family / receipt / ledger，也不替 core 启用 runtime topology path。

## Adapter mode

本计划只允许以下 adapter mode：

```text
validator_consumer_read_only_candidate
```

该 mode 的含义是：

- 可以读取 contracts public export；
- 可以读取 accepted schema / family metadata；
- 可以验证 fixture / payload 是否满足 accepted schema identity；
- 可以验证 canonical hash 是否等于前序 golden fixture hash；
- 可以检查 downstream policy / authority envelope 是否完整；
- 可以输出只读 validation report；
- 不能写 memory；
- 不能创建 memory record；
- 不能触发 writeback；
- 不能生成 DRL action；
- 不能生成 trading signal；
- 不能启用 live execution。

## 允许的只读操作

本计划只允许以下操作：

```text
public_contract_import_check
accepted_schema_identity_check
accepted_family_identity_check
receipt_reference_presence_check
canonical_hash_equality_check
downstream_policy_presence_check
authority_envelope_consistency_check
scope_match_check
fail_closed_reason_collection
read_only_validation_report
```

这些操作只产生 validation / diagnosis / report，不产生 runtime state mutation。

## 禁止的操作

本计划明确禁止：

```text
memory_write
memory_record_creation
memory_writeback_request
memory_writeback_record
runtime_consumption
scheduler_route
execution_handoff
drl_execution
trading_signal_generation
future_live_execution
production_runtime_canonical_hash_creation
```

## Fail-closed 条件

未来 adapter stub / implementation 必须在以下条件下 fail-closed：

1. contracts public export 不存在；
2. schema 不是 `MMNAuthorityEventMemoryAcceptedV1`；
3. family 不是 `MMNAuthorityEventMemoryAcceptedFamilyV1`；
4. accepted schema receipt 缺失；
5. accepted family receipt 缺失；
6. receipt ledger entry 缺失；
7. `docs/FIELD_REGISTRY.md` entry 缺失；
8. downstream policy 缺失；
9. core topology boundary 缺失；
10. governance scanner boundary 缺失；
11. authority envelope 缺失；
12. authority envelope scope 不匹配；
13. `missing_evidence` 非空；
14. `blocking_conditions` 非空；
15. `deferral_refs` 非空；
16. `revocation_refs` 非空；
17. canonical hash 与 golden hash 不一致；
18. 任何 memory write / DRL / trading / live execution 请求出现。

## Authority envelope 规则

本计划继承 Authority Grant Decision Evidence Envelope 原则：

```text
Boolean authority fields are derived summaries, not authority sources.
```

因此 MMN adapter 不能因为看到以下字段为 true 就执行写入或消费：

```text
mmn_validator_consumer_authorized
memory_write_authority_granted
downstream_runtime_consumption_authorized
drl_execution_authority_granted
trading_signal_authorized
future_live_execution_authorized
```

任何授权都必须由完整 envelope 的 evidence / scope / receipt / policy / scan / adapter validation 派生。

## Golden canonical hash

前序 golden fixture canonical SHA256 保持：

```text
dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90
```

本计划不重新计算 production runtime canonical hash。

## Explicit non-authorizations

本 PR 不授权：

- production adapter implementation；
- runtime consumption；
- MMN validator-consumer production adoption；
- memory write；
- memory record creation；
- writeback request；
- writeback record；
- DRL execution；
- trading signal；
- future live execution；
- PANT runtime execution；
- ZANT authority expansion；
- VANT accepted semantic authority expansion；
- runtime canonicalizer；
- production runtime canonical hash。

## Boundary

本 PR 是 docs/test-only。

它创建 MMN validator-consumer read-only adapter plan 的文档、JSON 与 fixture 测试，但不修改生产 adapter、不接 runtime、不写 memory。
