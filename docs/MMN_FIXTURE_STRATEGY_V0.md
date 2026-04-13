# MMN_FIXTURE_STRATEGY_V0

## 1. 目的

本文档用于说明当前 `aiant-mmn` 在阶段性 checkpoint 下的 fixture / golden test 策略。

它的目标不是为当前仓引入更重的测试基础设施，
也不是提前冻结尚未成熟的 richer MMN semantics，
而是用于明确：

- 当前为什么优先冻结 preview output 与最小 MMN 对象链
- 当前 golden fixtures 在仓内属于什么层级
- 当前 golden tests 主要防止哪些边界漂移
- 为什么当前阶段默认不继续无边界扩 object shell
- 为什么 richer semantics 应在后续更清楚的 contract 需求下再进入冻结面

---

## 2. 当前前提

当前 `aiant-mmn` 的整体边界仍保持为：

- preview-only
- non-executing
- no worker coupling
- no formal execution payload
- deterministic output shape
- fail-closed integration

因此，当前阶段的 fixture strategy，
不应围绕完整运行时、完整执行流或完整持久化系统展开，
而应围绕：

> 当前已经稳定存在的最小 contract surface  
> 与最小可回归 payload surface

展开。

---

## 3. 为什么当前要优先引入 golden fixtures

当前 `aiant-mmn` 已经不只是一个模糊的概念仓。

它至少已经具备以下两类稳定面：

### 3.1 preview output / record 层

当前最小 preview output 已成立：

```text id="c9annh"
MemoryPreviewOutputV0
    └─ records
        └─ MemoryRecordV0
```

其中：

* `MemoryPreviewOutputV0` 表达当前最小 memory preview output
* `MemoryRecordV0` 表达其中的最小记录级单元

`MemoryRecordV0` 当前明确只表达最小 preview record semantics，
不表达 execution payload，也不承担完整 MMN governance。

这意味着：

> preview output / record 层已经具备被 fixture 冻结的条件。

---

### 3.2 最小 MMN 本体对象链层

当前最小 MMN 本体对象链也已成立：

```text id="ubhbk9"
HistoricalComparisonObjectV0
    -> PosteriorCorrectionObjectV0
    -> MemoryWriteBackRequestV0
    -> MemoryWriteBackRecordV0
```

这条链当前表达的是：

* 历史对照
* posterior correction
* write-back request
* write-back record

而从当前 MMN 设计理解看，
MMN 的关键不只是 recall，
还包括历史对照、后验修正与写回纪律。

这意味着：

> 最小 MMN 本体对象链也已经具备被 fixture 冻结的条件。

---

## 4. 当前 fixture strategy 的核心判断

本阶段的核心判断是：

> 当前最值得冻结的，
> 不是所有可能的未来 MMN 语义，
> 而是已经稳定落地、且已经有明确 contract 边界的最小 payload surface。

因此，当前优先冻结两组内容：

### A. memory preview output fixtures

用于冻结：

* `MemoryPreviewOutputV0` 的最小输出形状
* `MemoryRecordV0` 作为 `records` 成员的最小 payload 形状
* 最小 `reason_codes` / `trace` / `id` / `record_kind` 结构

### B. mmn object chain fixtures

用于冻结：

* `HistoricalComparisonObjectV0`
* `PosteriorCorrectionObjectV0`
* `MemoryWriteBackRequestV0`
* `MemoryWriteBackRecordV0`

以及它们在最小对象链中的 canonical payload shape

---

## 5. 当前为什么先冻结这两组 fixtures

### 5.1 因为这两组已经具备明确边界

当前这两组对象/输出已经有：

* object contract
* payload projection
* smoke / golden tests
* fail-closed posture
* deterministic shape

因此，冻结它们的回归价值很高。

---

### 5.2 因为它们刚好覆盖当前仓最重要的两个层级

当前 `aiant-mmn` 至少有两个层级必须区分：

#### A. preview output / record 层

* `MemoryPreviewOutputV0`
* `MemoryRecordV0`

#### B. MMN 本体语义对象层

* `HistoricalComparisonObjectV0`
* `PosteriorCorrectionObjectV0`
* `MemoryWriteBackRequestV0`
* `MemoryWriteBackRecordV0`

当前 fixtures 正好分别覆盖了这两个层级。

这样做的价值是：

* 防止 preview record layer 漂移
* 防止 MMN object layer 漂移
* 防止后续把两层语义重新混在一起

---

### 5.3 因为当前最稀缺的是“冻结边界”，而不是“继续发明对象”

从当前 MMN 设计理解看，
最重要的不是立刻把所有 richer semantics 全都 materialize，
而是先把：

* 什么已经 landed
* 什么只是 preview-only shell
* 什么属于 record 层
* 什么属于 MMN 本体对象层
* 哪些 payload 已经应当保持稳定

这些边界固定下来。

所以：

> 当前 fixture strategy 的重点是“冻结已成立的边界”，
> 而不是“为未来所有语义提前建测试壳”。

---

## 6. 当前 golden fixtures 在仓内属于什么层级

当前这批 golden fixtures 应被理解为：

> 阶段性 contract freeze surface

它们不是：

* 完整端到端集成测试
* 完整运行时行为测试
* 完整 memory governance test suite
* 完整 write-back policy engine test suite

它们当前只负责：

* 冻结 canonical payload
* 冻结最小对象/输出形状
* 防止字段、枚举、trace、id shape 漂移
* 防止 execution-like fields 渗入本阶段 preview-only surface

---

## 7. 当前 golden tests 主要防止什么

当前 golden tests 最主要防止以下几类问题。

### 7.1 payload shape 漂移

例如：

* 字段名改动
* 枚举值漂移
* trace 结构变化
* reason_codes 结构变化
* id 规则漂移

### 7.2 层级混淆

例如：

* 把 `MemoryRecordV0` 塞入 richer MMN semantics
* 把 write-back semantics 误塞回 preview record layer
* 把 preview output object 与 MMN 本体对象层混在一起

### 7.3 execution-like 字段渗入

例如：

* queue / worker / dispatch / execution payload 等字段不小心进入当前 payload surface

当前阶段这是明确不允许的。

### 7.4 builder / payload projection 意外回归

例如：

* builder 默认值变化
* payload projection 丢字段
* trace 不再 canonical
* fixture 与实际输出脱节

---

## 8. 当前 fixture 目录设计的含义

当前 fixture 目录之所以设计为：

```text id="c8m7x4"
tests/fixtures/
├─ memory_preview_output_v0/
└─ mmn_object_chain_v0/
```

并不是单纯为了整理文件，
而是为了显式表达两类冻结面：

### 8.1 `memory_preview_output_v0/`

这一组表示：

> preview output / record 层的冻结面

### 8.2 `mmn_object_chain_v0/`

这一组表示：

> MMN 本体对象链层的冻结面

这个目录结构本身就是一种架构表达：

* preview output layer
* MMN object chain layer

分开冻结，避免语义混淆。

---

## 9. 当前为什么不继续冻结更重的 richer MMN semantics

这是当前 fixture strategy 中必须显式写清楚的一点。

### 9.1 因为 richer semantics 还没有足够稳定的 contract surface

虽然当前方向已经清楚：

* MMN 不只是 recall
* MMN 应是历史对照层
* MMN 应是 posterior correction engine
* MMN 应承担写回纪律

但这些 richer semantics 的更重层次，例如：

* 更复杂 recall governance
* 更复杂 posterior policy
* 更复杂 memory layering policy
* 更复杂 write-back acceptance rule
* 更复杂 retention / decay / demotion logic

当前都还没有形成足够稳定、清楚、低歧义的 contract surface。

此时如果过早引入大量 fixtures，
风险反而更高：

* 会冻结尚未成熟的语义
* 会提高后续重构成本
* 会造成“测试很多，但边界其实还没想清楚”的假稳定

---

### 9.2 因为当前阶段最应该冻结的是“最小 landed surface”

当前更适合被冻结的是：

* 已 landed 的 preview output surface
* 已 landed 的 record-level surface
* 已 landed 的 MMN object chain surface

而不是：

* 尚未真正 landed 的 richer policy surface

换句话说：

> 当前 fixture strategy 默认只冻结“已经成立的最小表面”，
> 暂不冻结“尚在演化中的更重语义表面”。

---

## 10. 当前 fixture strategy 与 write-back 时间序列纪律的关系

当前 `MemoryWriteBackRequestV0` / `MemoryWriteBackRecordV0`
虽然已经进入 fixture 冻结面，
但这并不意味着：

* write-back policy 已完整落地
* 时间序列治理已完整编码
* “再次出现”的时间定义已数值化固定

当前被冻结的，
只是它们的最小 object / payload shape。

至于它们在时间序列中的最小治理解释，
应由 `MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0.md` 单独负责说明。

因此：

* fixture strategy 冻结的是 “对象形状”
* write-back discipline 文档解释的是 “对象何时与为何适用”

两者互补，但不应混同。

---

## 11. 当前阶段推荐冻结的具体内容

本阶段推荐冻结的最小内容如下：

### 11.1 preview output fixtures

建议冻结：

* default preview output
* richer preview output

用于覆盖：

* 最小 record shape
* richer preview hint
* reason_codes / trace / id canonicality

### 11.2 object chain fixtures

建议冻结：

* `historical_comparison_alpha`
* `posterior_correction_alpha`
* `memory_writeback_request_alpha`
* `memory_writeback_record_alpha`
* `mmn_object_chain_light_beta`

用于覆盖：

* richer alpha path
* lighter beta path
* 最小 object chain linkage
* canonical payload shape
* execution-like field absence

---

## 12. 当前 fixture strategy 的一句话结论

可以用下面这句话概括当前策略：

> 当前 `aiant-mmn` 的 fixture strategy，
> 不是为了提前冻结所有未来 MMN semantics，
> 而是为了先冻结已经 landed 的最小 preview output / record surface
> 与最小 MMN object chain surface，
> 从而把当前阶段真正成立的结构边界固定下来。

---

## 13. 当前阶段最终总结

可以用下面这段话作为本文档总结：

> 当前 `aiant-mmn` 已经具备引入阶段性 golden fixtures 的条件，
> 但这些 fixtures 应优先覆盖：
>
> * preview output / record 层
> * 最小 MMN 本体对象链层
>
> 它们当前的作用是冻结 canonical payload、保持层级清晰、阻止 execution-like 字段渗入，
> 并为后续 checkpoint、handoff 与回归验证提供稳定基线。
>
> 当前阶段默认不继续无边界冻结 richer MMN semantics，
> 而应在更明确的 contract 需求、对象稳定性与治理边界出现后，再逐步扩大 fixture surface。

```

这份文档补上后，你这次 PR 的叙事就会完整很多：

- 为什么先 checkpoint
- 为什么先写 write-back 时间序列纪律
- 为什么先补这两组 golden fixtures
- 为什么现在不继续扩 object shell / richer semantics
