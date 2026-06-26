# MMN Authority Event Memory V1.3.1 Engineering Entry Plan V0

## 入口名称

```text
MMN Authority Event Memory V1.3.1 Current Intent and Legacy Seam Alignment V0
```

## 推荐 PR 标题

```text
docs/test: add MMN authority event memory v1.3.1 current intent and legacy seam alignment v0
```

## 范围

第一刀 PR 是 docs/test-only。

引入：

- `MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_CURRENT_BUSINESS_INTENT_V0.md`
- `MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_LEGACY_SEAM_ALIGNMENT_V0.md`
- `MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_COMPATIBILITY_BOUNDARY_V0.md`
- `MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_ENGINEERING_ENTRY_PLAN_V0.md`
- marker coverage 文档回归测试

## 非目标

第一刀 PR 不引入：

- `src/mmn/contracts/authority_event_memory_v1.py`
- 真实 validators；
- persistence layer；
- event crawler；
- live ingestion；
- DRL bridge；
- HFEG bridge；
- TRACE-HIX bridge；
- production replay harness；
- trading signal。

## 后续 PR 顺序

### PR 1: current intent 与 legacy seam alignment

```text
aiant-mmn docs/test-only
```

目的：

```text
声明 V1.3.1 是当前 MMN authority event memory intent；
声明既有 V0 preview/writeback/memory seam 只是 legacy-compatible host surface。
```

### PR 2: contracts object skeleton

```text
aiant-contracts
```

建议对象：

```text
MMNEventMemoryRecordV1
EventAttributionLinkV1
RetrievalAuditLogV1
AsOfDataReceiptV1
AttributionScoringPolicyV1
AttributionMultiplicityControlV1
MemoryPromotionChecklistV1
AuditEvidenceDigestV1
```

### PR 3: MMN fixture scaffold

```text
aiant-mmn
```

建议 fixture 类型：

```text
golden fixtures
negative fixtures
edge-case fixtures
waiver fixtures
digest consistency fixtures
```

### PR 4: MMN validator consumer stub

```text
aiant-mmn
```

边界：

```text
non-executing validator-consumer behavior
fail-closed negative coverage
no execution authority
```

### PR 5: governance scan expansion

```text
aiant-governance
```

覆盖：

```text
forbidden wording
field drift
execution leakage
schema authority bypass
```

## Readiness markers

docs-only 入口应包含以下 marker：

```text
V1.3.1-Validator-Ready
current business intent
legacy-compatible host surfaces only
MMNEventMemoryRecordV1
AuditEvidenceDigestV1
MemoryPromotionChecklistV1
AttributionScoringPolicyV1
AttributionMultiplicityControlV1
non_executing_only
no_live_execution
no_trading_signal
no_schema_authority
```

## 停止条件

本 PR 合并后，不应继续在 `aiant-mmn` 直接添加 runtime code。

下一步应先确认 `aiant-contracts` object skeleton 方向，再由 `aiant-mmn` 消费 contracts skeleton 做 fixtures 与 validator-consumer stub。

## Regression marker

`	ext
does not introduce runtime validators, persistence layer, event crawler, live ingestion, DRL bridge, or trading signal.
`


## Regression markers

The first PR is docs/test-only.

It does not introduce:
- real validators
- persistence layer
- event crawler
- live ingestion
- DRL bridge
- trading signal
- contracts object skeleton implementation
