# MMN Authority Event Memory Validator-Consumer Read-Only Adapter Stub V0

> 本文件是 `aiant-mmn` 的 docs/test-only validator-consumer read-only adapter fixture + stub 说明。
> 它在前序 adapter plan 基础上新增一个最小只读验证 stub 与 fixture。
> 本文件不授权 runtime consumption、memory write、DRL execution、trading signal 或 future live execution。

## 目的

`MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_STUB_V0`
用于把 plan 阶段推进到最小 stub 阶段：

```text
plan -> fixture -> read-only validation stub -> denied cases -> future production adapter
```

本 stub 固定一条规则：

```text
MMN read-only validation report is not memory write authority.
```

中文表达为：

```text
MMN 只读验证报告不等于记忆写入授权。
```

## Stub 范围

新增 stub：

```text
src/aiant_mmn/mmn_authority_event_memory_validator_consumer_read_only_adapter_v0.py
```

该 stub 只做只读验证并返回 validation report。

允许验证：

- schema identity；
- family identity；
- canonical hash equality；
- accepted schema / family receipt refs；
- downstream policy presence；
- Authority Grant Decision Evidence Envelope consistency；
- grant scope match；
- forbidden operation request detection；
- fail-closed reason collection。

禁止执行：

- memory write；
- memory record creation；
- writeback request / record；
- runtime consumption；
- DRL execution；
- trading signal；
- future live execution。

## Fixture

新增 fixture：

```text
tests/fixtures/mmn_authority_event_memory/validator_consumer_read_only_adapter_stub_v0.json
```

fixture 覆盖：

- valid read-only payload；
- missing receipt denied case；
- canonical hash mismatch denied case；
- scope mismatch denied case；
- memory write requested denied case。

## Fail-closed 规则

任何以下条件出现时，stub 必须 fail-closed：

```text
schema_identity_mismatch
family_identity_mismatch
canonical_hash_mismatch
missing_receipt_refs
missing_downstream_policy
authority_envelope_inconsistent
authority_envelope_scope_mismatch
memory_write_requested
memory_record_creation_requested
memory_writeback_requested
runtime_consumption_requested
drl_execution_requested
trading_signal_requested
future_live_execution_requested
```

## Authority envelope 继承规则

继续继承：

```text
Boolean authority fields are derived summaries, not authority sources.
```

中文表达为：

```text
布尔型 authority 字段只能是派生摘要，不能是授权来源。
```

## Golden canonical hash

前序 golden fixture canonical SHA256 保持：

```text
dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90
```

本 stub 不创建 production runtime canonical hash。

## Explicit non-authorizations

本 PR 不授权：

- production adapter adoption；
- runtime consumption；
- memory write；
- memory record creation；
- writeback request / record；
- DRL execution；
- trading signal；
- future live execution；
- runtime canonicalizer；
- production runtime canonical hash。

## Boundary

本 PR 是最小 read-only stub。

它可以返回 validation report，但 report 本身不是 authority source，不允许被用来写 memory 或执行策略。
