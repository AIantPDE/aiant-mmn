# MMN Authority Event Memory V1.3.1 Legacy Seam Alignment V0

## 兼容声明

```text
Existing V0 preview/writeback/memory seams are legacy-compatible host surfaces only.
They do not define the current Authority Event Memory V1.3.1 business semantics.
```

中文边界：

```text
既有 V0 preview / writeback / memory seam 只作为 legacy-compatible host surface；
它们不定义当前 Authority Event Memory V1.3.1 的业务语义。
```

## 既有可复用宿主面

| 既有 surface | 可复用价值 | 不作为 V1.3.1 source-of-truth |
|---|---|---|
| `MEMORY_PREVIEW_OUTPUT_V0` | preview-only 输出纪律 | 不是 event memory family schema |
| `MEMORY_RECORD_V0` | generic memory record 先例 | 不是 V1.3.1 的父 schema |
| `MEMORY_WRITEBACK_REQUEST_V0` | writeback request 边界先例 | 不是 V1.3.1 的持久化授权 |
| `MEMORY_WRITEBACK_RECORD_V0` | writeback record trace 先例 | 不是事件归因审计真源 |
| `MMN_OBJECT_FAMILY_V0` | 对象族文档模式 | 不是最终 Authority Event Memory schema |
| `MMN_FIXTURE_STRATEGY_V0` | golden / negative fixture 先例 | 不是 V1.3.1 fixture coverage |
| Minimal host / recall / adapter tests | low-surface host 纪律 | 不是生产级事件记忆 runtime |

## 可以复用的内容

V1.3.1 可以复用 V0 的工程纪律：

- preview-only 边界；
- non-executing 语义；
- fail-closed 处理；
- payload projection 测试；
- golden / negative fixture 风格；
- public export 纪律；
- low-surface host 模式；
- writeback 不等于 persistent authority；
- visibility policy 不授予 mutation authority。

## 不得隐式继承的内容

V1.3.1 不得从 V0 隐式继承：

- 当前事件记忆业务语义；
- 权威事件归因 schema；
- anti-hindsight-bias protocol；
- opportunity-candidate memory 语义；
- attribution scoring policy；
- multiplicity control；
- audit digest；
- execution authority。

## 正确对齐原则

```text
V0 provides host-seam compatibility.
V1.3.1 provides current authority event memory intent.
aiant-contracts will provide schema truth.
aiant-mmn will host non-executing preview / fixture / validator-consumer behavior.
```

中文表达：

```text
V0 提供宿主 seam 兼容性；
V1.3.1 提供当前权威事件记忆业务意图；
aiant-contracts 提供 schema truth；
aiant-mmn 承接 non-executing preview / fixture / validator-consumer 行为。
```
