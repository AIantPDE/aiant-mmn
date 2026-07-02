# MMN Authority Event Memory Read-Only Adapter Report Projection Fixtures V1

> 本文件是 `aiant-mmn` 的 read-only adapter report projection fixtures v1
> 检查点。本 PR 只新增 fixtures、文档与回归测试，不修改 projection source。
> 它不授权 production adapter adoption、runtime consumption、memory write、
> DRL execution、trading signal 或 future live execution。

## 目的

`MMN_AUTHORITY_EVENT_MEMORY_READ_ONLY_ADAPTER_REPORT_PROJECTION_FIXTURES_V1`
用于补强 read-only adapter report projection v0 的边界回归样例。

本 fixtures v1 的定位是：

```text
projection fixtures v1 = regression inputs
projection fixtures v1 != memory write authority
projection fixtures v1 != runtime authorization
fixtures are not authority sources
```

中文表达为：

```text
projection fixtures v1 只是回归输入；
projection fixtures v1 不等于记忆写入授权；
projection fixtures v1 不等于运行时授权；
fixture 不是授权来源。
```

## 前序依赖

本 fixtures v1 假定以下边界已经完成或正在进入合并流程：

1. `aiant-mmn`：read-only adapter fixture + stub v0；
2. `aiant-mmn`：read-only adapter denied case hardening v0；
3. `aiant-mmn`：read-only adapter report projection v0；
4. `aiant-governance`：scanner check-path preview v0；
5. `aiant-governance`：scanner check-path denied fixtures v0；
6. `aiant-core`：topology gate skeleton v0；
7. `aiant-core`：topology gate check-path preview v0。

本文件不重新定义 contracts schema / family / receipt / ledger，
不替 governance 启用 scanner enforcement，也不替 core 启用 runtime topology path。

## Fixtures V1 覆盖

新增 v1 fixtures 覆盖：

```text
duplicate fail_closed reasons are deduplicated preserving order
unexpected adapter mode fails closed
missing report kind fails closed
string fail_closed_reasons do not expand into characters
write and execute claims fail closed without leaking authority
attribute object valid report projects report-only
attribute object fail-closed report preserves reasons
```

## Projection 不变量

所有 fixture 必须保持以下不变量：

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

## Authority envelope 继承规则

本 fixtures v1 继续继承三条规则：

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

本 fixtures v1 不重新计算 production runtime canonical hash。

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

本 PR 是 fixtures + regression tests only。

它创建文档、JSON、fixture 与测试，但不改 projection source，不接 memory write、不接 runtime、不创建记录。
