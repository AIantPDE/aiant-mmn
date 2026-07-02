# MMN Authority Event Memory — Write Request Candidate Preview Fixtures V1

## 定位

本文件定义 `aiant-mmn` 中 MMN Authority Event Memory 的 write request candidate preview fixtures v1。

这一刀只把业务需求场景推进到可回归的 preview fixture 层：

```text
non-executing business requirement fixture
  -> candidate write request preview fixture
  -> fail-closed denial cases
```

它不是正式 write request schema，不是 memory write，不是 runtime shadow mode，也不是 accepted schema surface promotion。

## 范围

本 PR 只允许新增：

```text
docs/verification/MMN_AUTHORITY_EVENT_MEMORY_WRITE_REQUEST_CANDIDATE_PREVIEW_FIXTURES_V1.md
docs/verification/mmn_authority_event_memory_write_request_candidate_preview_fixtures_v1.json
tests/fixtures/mmn_authority_event_memory/write_request_candidate_preview_fixtures_v1.json
tests/docs/test_mmn_authority_event_memory_write_request_candidate_preview_fixtures_v1.py
```

## 上游引用

这些引用只作为 candidate planning / preview planning trace：

```text
contracts: grant decision receipt candidate plan v0
core: topology gate grant-envelope preview plan v0
mmn: write request candidate preview plan v0
```

它们不是 authority source，也就是 not authority source；不授予 runtime path，也不授予 memory write authority。

## V1 fixture family

`fixture_family_version == v1` 表示：

```text
- 明确 candidate write preview 的最小正例 fixture。
- 明确 negative evidence / missing receipt 的 fail-closed fixture。
- 明确 formal schema promotion / persisted memory record / runtime shadow mode 请求全部 deny_fail_closed。
- 明确 boolean authority fields 只是 derived summaries，不是 authority source。
```

## Explicit non-authorizations

本 fixture family 不授权：

```text
formal grant decision receipt
formal write request schema
accepted schema surface expansion
formal FIELD_REGISTRY update
writeback request
memory write authority
memory record creation
runtime topology path
runtime path enablement
scheduler route
execution handoff
runtime shadow mode
DRL execution
trading signal
future-live execution
```

## Fail-closed 默认

任何缺失 `grant_decision_receipt_candidate_ref`、请求 runtime shadow mode、请求 formal write request schema promotion、请求 persisted memory record materialization 的 case，必须得到：

```text
expected_decision == deny_fail_closed
```

## 结论

`write_request_candidate_preview_fixtures_v1` 是 preview-only / fixture-only / report-only 测试资产。

它保留真实业务语义，但执行路径为零、授权能力为零、副作用为零。
