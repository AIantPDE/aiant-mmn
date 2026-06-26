# MMN Authority Event Memory V1.3.1 当前业务意图 V0

## 治理声明

```text
V1.3.1 defines the current MMN authority event memory intent.
Existing V0 preview/writeback/memory seams are legacy-compatible host surfaces only.
```

中文边界：

```text
V1.3.1 定义当前 MMN 权威事件记忆业务意图；
既有 V0 preview / writeback / memory seam 只作为历史兼容宿主面，
不作为当前业务语义真源。
```

## 当前业务意图

Authority Event Memory V1.3.1-Validator-Ready 定义当前 MMN 事件记忆方向。

它覆盖以下对象族：

- `MMNEventMemoryRecordV1`
- `MMNRiskMemoryRecordV1`
- `MMNOpportunityCandidateMemoryRecordV1`
- `MMNConstraintMemoryRecordV1`
- `MMNRegimeMemoryRecordV1`
- `MMNFailureMemoryRecordV1`
- `MMNNeutralObservationMemoryRecordV1`
- `EventAttributionLinkV1`
- `RetrievalAuditLogV1`
- `AsOfDataReceiptV1`
- `MarketRhythmControlReportV1`
- `AttributionScoringPolicyV1`
- `AttributionMultiplicityControlV1`
- `MemoryPromotionChecklistV1`
- `AuditEvidenceDigestV1`

## 业务含义

V1.3.1 将 MMN 权威事件记忆推进为 validator-ready 的候选记忆系统：

```text
权威事件有来源
反事后归因偏差
检索过程可审计
历史时点可见性受 as-of 约束
placebo / control 可测试
支持盲审 / 半盲审
评分策略可复盘
多重检验风险可控制
记忆晋级 checklist 可治理
审计摘要可汇总
仅允许 non-executing 使用
```

## 记忆族

| 记忆族 | 含义 | 禁止解释 |
|---|---|---|
| `risk` | 用于风险扰动与安全边界验证的风险记忆 | 卖出信号 |
| `opportunity_candidate` | 用于机会诱惑 / 机会召回 probe 的机会候选记忆 | 买入信号 |
| `constraint` | 用于收缩动作空间的约束记忆 | 执行授权 |
| `regime` | 用于市场情境标注的 regime 记忆 | 市场预测保证 |
| `failure` | 用于回归测试的失败记忆 | 未来必然重复 |
| `neutral_observation` | 用于防止过度归因的中性观察记忆 | 强行事件因果 |

## Non-executing 规则

允许输出：

```text
FLAG_RISK
FLAG_OPPORTUNITY
PREPARE_CANDIDATE_ONLY
REQUIRE_CONFIRMATION
REQUIRE_HUMAN_REVIEW
WAIT_FOR_OPEN
NO_TRADE
```

禁止输出：

```text
LIVE_BUY
LIVE_SELL
LEVERAGE_UP
QUEUE_MARKET_ORDER
BYPASS_HUMAN_REVIEW
EXECUTION_AUTHORIZED
```

## Source-of-truth 边界

V1.3.1 是当前业务意图与 validator-ready 设计 profile。

它还不是：

- 已被 `aiant-contracts` 接受的 schema；
- 持久化 MMN 记忆数据库；
- crawler；
- production ingestion connector；
- DRL execution lane；
- 交易信号生成器；
- OOS alpha 或收入证明。

Schema truth 由 `aiant-contracts` 决定。`aiant-mmn` 在 contracts skeleton 引入之后，承接 non-executing preview、fixture、validator-consumer 与 projector 行为。

## Regression marker

`	ext
non-executing only
`

