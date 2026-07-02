# MMN Authority Event Memory Read-Only Adapter Report Projection V0

> 本文件是 `aiant-mmn` 的 read-only adapter report projection v0 检查点。
> 本 PR 新增的是非授权、非 runtime、非 memory-write 的 report projection。
> 它只把 read-only adapter validation report 投影成可被下游引用的 report-only summary，
> 不授权 production adapter adoption、runtime consumption、memory write、DRL execution、
> trading signal 或 future live execution。

## 目的

`MMN_AUTHORITY_EVENT_MEMORY_READ_ONLY_ADAPTER_REPORT_PROJECTION_V0`
用于把 read-only adapter 的 validation report 转成稳定的 projection object。

本 projection 的定位是：

```text
read-only adapter report projection = non-authorizing summary
read-only validation report != memory write authority
report projection != runtime authorization
```

中文表达为：

```text
read-only adapter report projection 只是非授权摘要；
只读验证报告不等于记忆写入授权；
report projection 不等于运行时授权。
```

## 前序依赖

本 projection 假定以下边界已经完成或正在进入合并流程：

1. `aiant-contracts`：accepted schema promotion execution v0；
2. `aiant-contracts`：downstream adoption boundary plan v0；
3. `aiant-governance`：downstream scanner skeleton v0；
4. `aiant-governance`：scanner check-path preview v0；
5. `aiant-core`：topology gate skeleton v0；
6. `aiant-mmn`：validator-consumer read-only adapter fixture and stub v0；
7. `aiant-mmn`：read-only adapter denied case hardening v0。

本文件不重新定义 contracts schema / family / receipt / ledger，
不替 governance 启用 scanner enforcement，也不替 core 启用 runtime topology path。

## Projection 行为

新增 projection 只提供一个入口：

```text
project_mmn_authority_event_memory_read_only_adapter_report_v0(...)
```

该入口接受 read-only adapter validation report 或同形 mapping，返回：

```text
MMNAuthorityEventMemoryReadOnlyAdapterReportProjectionV0
```

projection 必须保持：

```text
report_projection_is_memory_write_authority = false
report_projection_is_runtime_authorization = false
allowed_to_write_memory = false
allowed_to_execute = false
downstream_runtime_consumption_authorized = false
memory_write_authority_granted = false
drl_execution_authority_granted = false
trading_signal_authorized = false
future_live_execution_authorized = false
```

## Valid report-only projection

当 source report 满足：

```text
report_kind = mmn_authority_event_memory_read_only_validation_report_v0
adapter_mode = validator_consumer_read_only
fail_closed = false
allowed_to_write_memory = false
allowed_to_execute = false
```

projection 只能输出：

```text
projection_decision = project_read_only_report
projection_action = no_runtime_authorization
projected_status = read_only_validated_report_only
```

## Fail-closed preservation

若 source report 已经 `fail_closed = true`，或 source report 出现写入 / 执行 claim，
projection 必须输出：

```text
projection_decision = project_fail_closed_report
projection_action = preserve_fail_closed
projected_status = fail_closed_report_only
```

并保留 source report 的 fail_closed reasons。

## Authority envelope 继承规则

本 projection 继续继承三条规则：

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

## Golden canonical hash

前序 golden fixture canonical SHA256 保持：

```text
dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90
```

本 projection 不重新计算 production runtime canonical hash。

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

## Boundary

本 PR 是 read-only adapter report projection。

它创建 projection source、文档、JSON、fixture 与测试，但不接 memory write、不接 runtime、不创建记录。
