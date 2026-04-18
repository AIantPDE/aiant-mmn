# MMN_WRITEBACK_TIME_SERIES_DISCIPLINE_V0

时间：2026年4月13日

## 1. 目的

本文档用于单独说明当前 `aiant-mmn` 中 `write-back` 相关对象的时间序列语义边界。

它的目标不是把当前仓解释成完整的 write-back governance system，
也不是把 `MemoryWriteBackRequestV0` / `MemoryWriteBackRecordV0` 提前扩张成完整持久化基础设施，
而是用于明确：

- 当前 `MemoryWriteBackRequestV0` 与 `MemoryWriteBackRecordV0` 分别表达什么
- 为什么 `write-back` 不应按固定日历时间定义
- 在时间序列中，什么才算“再次出现”
- 在什么情况下，当前事件值得提出 write-back request
- 在什么情况下，当前 request 更适合形成 write-back record

---

## 2. 当前前提

当前 `aiant-mmn` 的整体边界仍保持为：

- preview-only
- non-executing
- no worker coupling
- no formal execution payload
- deterministic output shape
- fail-closed integration

因此，本文讨论的 `write-back`，
当前只应理解为：

> 一种最小 memory-semantic write-back discipline，
> 而不是 backend mutation pipeline。

这点必须继续保持清楚，
否则后续很容易把当前对象误解成已经拥有正式数据库写入、异步执行、任务调度与完整生命周期治理能力。

---

## 3. 当前 `MMN` 语境下为什么必须单独讨论 write-back

当前对 `MMN` 的理解，
不应停留在：

- memory bank
- RAG
- recall helper
- context augmenter

更准确地说，`MMN` 当前被理解为：

- 历史对照层
- 上下文支撑层
- posterior correction engine
- 写回纪律承载层

这意味着：

> `MMN` 的核心价值不只是“记住过去”，
> 而在于“把过去结果转化为当前修正力”，
> 并把当前结果继续沉淀成未来可被 recall、对照与修正的经验。

因此，`write-back` 在 `aiant-mmn` 中不是附属问题，
而是 MMN 语义能否真正形成经验闭环的关键问题。

---

## 4. 当前 `MemoryWriteBackRequestV0` 的最小定位

当前 `MemoryWriteBackRequestV0` 不应被理解为：

- 数据库写入命令
- worker-facing execution payload
- queue task
- mutation job
- persistence API request

更准确地说，它当前表达的是：

> 一个已经到达可评估时点、且具有记忆增量价值的写回申请语义。

换句话说：

- 当前事件已经走到足以判断 outcome 的阶段
- 当前 outcome 对已有记忆体系可能具有强化、修正或细化价值
- 因此系统提出一个“是否值得写回”的申请

所以，`Request` 当前的重点不是“已经写入”，
而是：

> 当前 case 已经成熟到值得进入 write-back judgment。

---

## 5. 当前 `MemoryWriteBackRecordV0` 的最小定位

当前 `MemoryWriteBackRecordV0` 也不应被高估为：

- 完整 persistence ledger
- 数据库审计总账
- 长期记忆主存的正式实现
- backend write receipt

更准确地说，它当前表达的是：

> 一次 write-back request 通过最小治理后，
> 最终形成的记忆记录语义。

也就是说：

- `MemoryWriteBackRequestV0` 回答  
  “这次有没有东西值得申请写回？”

- `MemoryWriteBackRecordV0` 回答  
  “这次写回申请最终形成了怎样的记忆记录？”

因此，当前应始终显式保持：

```text
MemoryWriteBackRequestV0
    != backend mutation command

MemoryWriteBackRecordV0
    != full persistence ledger
```

---

## 6. 为什么 `write-back` 不应以固定日历时间定义

在时间序列语境里，
最容易出现的误解是把“再次出现”理解成：

* 隔几天
* 隔几周
* 到某个固定日数就写
* 同类信号一重复就自动写回

这种理解在静态文档系统里也许勉强可用，
但在金融、行为链条、传播链条或多阶段反馈系统里，通常会失真。

### 6.1 同一事件尾波不等于新样本

一个事件今天触发，
明天产业链又动一下，
后天主线再拉一段，
这通常仍可能属于同一事件的扩散尾波。

如果把这些都理解成“再次出现”，
就会把同一轮事件误计为多个独立经验样本。

### 6.2 不同事件类型的 outcome horizon 不同

不同 pattern family 的验证窗口并不一致。

例如：

* 公告 + 产业链扩散
* 财报 + 券商上修预期
* 订单兑现 + 供应链传导
* 政策主题 + 板块联动

它们的 outcome horizon 可能相差很大。

因此，不存在一个统一的：
“过 N 天就算可以 write-back”的全局规则。

### 6.3 regime 改变会破坏可比性

即便自然日距离很近，
如果当前市场阶段、流动性状态、风险偏好或主题周期已经明显变化，
那么这次事件未必还能与上次按同一模式直接归并。

因此：

> 在时间序列里，
> “再次出现”不应先按自然日理解，
> 而应先按“新的独立事件实例 + 可比较结构模式 + outcome horizon 已闭合”来理解。

---

## 7. 在时间序列里，什么才算“再次出现”

当前更合理的定义不是：

> “距离上次 X 天”

而是：

> 在新的事件锚点下，
> 出现了一个新的、可比较的结构模式，
> 且该模式已经完成其 outcome horizon 的观察。

也就是说，
“再次出现”至少需要同时满足以下条件：

### 7.1 它是新的事件实例

不是旧事件的尾波，
不是旧事件在市场中的残余传播，
而是一个新的、可以独立编号的事件锚点。

例如：

* 新公告
* 新财报
* 新政策
* 新订单确认
* 新主题扩散触发点

### 7.2 它与已有样本可比较

当前模式与先前样本之间，
在结构上具有足够可比性。

例如：

* 都属于“主营利好 + 产业链同步受益叙事”
* 都属于“公告事实 + 券商上修预期”
* 都属于“强事实主线 + 外溢扩散链条”

### 7.3 它已经走完最小可观察窗口

也就是 outcome horizon 已闭合，
当前结果已经成熟到足以进行判断。

若还没走到 outcome 可判断的时点，
则只能算“正在发生”，
还不能算“再次观察到某种结果模式”。

因此，当前更严谨的说法应当是：

> “再次出现”不是指“隔多久又动了一次”，
> 而是指“又出现了一个新的、可比较的、已完成观察窗口的独立事件实例”。

---

## 8. 为什么应引入三个时钟

为了更准确地处理时间序列中的 write-back 语义，
建议显式区分三个时钟。

### 8.1 event clock

从事件自身的锚点开始计时。

例如：

* 公告发布时间
* 财报发布时间
* 券商一致上修开始扩散的时点
* 政策落地时点

它回答的是：

> 这次事件自己的观察窗口是否已经闭合？

### 8.2 market clock

从市场反应与交易窗口角度计时。

例如：

* 1 日、3 日、5 日、10 日交易窗口
* 扩散、兑现、回落、分化窗口

它回答的是：

> 市场是否已经走完足以判断 outcome 的反应周期？

### 8.3 regime clock

从阶段和环境角度计时。

例如：

* 风险偏好高 / 低
* 主题扩散期 / 退潮期
* 财报季前 / 财报季后
* 流动性宽松 / 收缩

它回答的是：

> 这次事件和上次事件是否仍处于可比较环境？

因此，
当前更合理的判断不是：

```text
距离上次 30 天 -> 再次出现
```

而是：

```text
新的 event anchor
+ 可比较 pattern family
+ outcome horizon 已闭合
+ regime 仍具备可比性
-> 再次出现同类可比较样本
```

---

## 9. 什么情况下值得提出 `MemoryWriteBackRequestV0`

当前更合理的最小判断条件，应至少包含以下三点。

### 9.1 事件已到可评估时点

当前事件必须已经完成一个最小 observation horizon，
否则 outcome 尚未成熟。

也就是说：

> 当前 case 已至少到达一个可判断结果的 horizon closure。

### 9.2 当前 outcome 具有记忆增量

不是所有 outcome 都值得写回。

更值得提出 request 的情况包括：

#### A. 强化已有经验

当前样本再次支持某条已存在的经验判断。

#### B. 修正已有经验

当前样本与原有经验冲突，需要形成新的 posterior correction。

#### C. 细化已有经验

当前样本说明某条经验只在特定 regime / event family / diffusion phase 下成立。

因此，当前 request 的提出应围绕：

> 这次结果是否改变、强化或细化了现有记忆。

### 9.3 当前样本是新的独立实例

它必须不是旧事件的尾部噪声，
而是一个新的、可比较、已经闭合 outcome horizon 的事件样本。

这才构成真正意义上的“又一个值得比较与写回的 case”。

---

## 10. 什么情况下更适合形成 `MemoryWriteBackRecordV0`

当前阶段，更稳妥的理解是：

* `Request` 可以由单次强样本提出
* `Record` 更适合在最小治理通过后形成

也就是说，`Record` 通常更适合在以下情况下形成：

### 10.1 样本属于新的独立事件实例

不是旧事件尾波，不是同一轮行情中的重复扰动。

### 10.2 当前样本与已有记忆关系清楚

例如：

* 与已有记忆一致，形成强化
* 与已有记忆冲突，但能形成合理修正
* 对已有模式形成更细粒度条件限定

### 10.3 当前样本具有足够支持力度

例如：

* 重复出现
* 单次但结果极强
* 与 historical comparison 结果高度一致
* 在当前 regime 下具有高解释力

因此：

> `MemoryWriteBackRequestV0` 更像“申请进入写回判断”，
> `MemoryWriteBackRecordV0` 更像“写回申请通过最小治理后形成的正式记录”。

---

## 11. 一个直观例子

假设第一次出现如下事件：

### 事件 A

* 时间：4 月 1 日
* 事实：A 公司利润大增，新增订单
* 叙事：主营公司受益，产业链设备商与原材料商同步受益
* 观察窗口：5 个交易日

5 个交易日后观察到：

* 主营公司显著上涨
* 设备商反应有限
* 原材料商回落

这时可以形成：

* `HistoricalComparisonObjectV0`
* `PosteriorCorrectionObjectV0`
* `MemoryWriteBackRequestV0`

但此时仍应注意：

若 4 月 3 日或 4 月 4 日产业链个股又动一下，
这通常仍可能属于事件 A 的尾波，
不应自动被理解为“再次出现”。

真正更适合被称为“再次出现”的，是例如：

### 事件 B

* 时间：5 月 12 日
* 新公司 B 发布强订单公告
* 市场再次出现“主营利好 + 产业链同步受益”的扩散叙事
* 在对应 observation horizon 闭合后，
  又一次观察到“主营兑现、链条未兑现”

这时才更适合说：

> 再次出现了同类可比较样本。

因为这里成立的不是“距离上次 41 天”，
而是：

* 有新的事件锚点
* 结构可比较
* outcome horizon 已闭合
* 结果模式再次出现

---

## 12. 当前阶段推荐的最严谨表述

为了避免后续误把 `write-back` 理解成“固定周期自动写入”，
建议在当前阶段使用如下表述：

> `MemoryWriteBackRequestV0` 当前表达的是：
> 一个 outcome 已到可评估时点、且具有记忆增量价值的写回申请语义。
>
> `MemoryWriteBackRecordV0` 当前表达的是：
> 该写回申请通过最小治理后，最终形成的记忆记录语义。
>
> 在时间序列语境中，
> “再次出现”不应以固定日历时间定义，
> 而应以“新的独立事件实例 + 可比较结构模式 + outcome horizon 已闭合”来定义。

---

## 13. 当前阶段明确不做的事

本文档当前不试图定义：

* 完整 write-back policy engine
* 全局统一 horizon 数值
* 完整 regime taxonomy
* 完整 persistence / storage architecture
* backend mutation ownership
* worker-coupled writeback execution flow

这些都属于后续 richer MMN governance 或跨仓协同时才应展开的问题。

当前阶段仅做最小边界澄清与时间序列纪律定义。

---

## 14. 一句话总结

可以用下面这句话概括当前文档结论：

> 当前 `aiant-mmn` 中的 write-back，
> 不应被理解为“到某个固定天数自动写入”，
> 而应被理解为：
> 针对已经走到可评估时点、并对系统经验具有增量价值的独立事件实例，
> 提出 `MemoryWriteBackRequestV0`；
> 再在最小治理通过后形成 `MemoryWriteBackRecordV0`。
>
> 在时间序列中，
> “再次出现”不以固定日历时间定义，
> 而以“新的独立事件实例 + 可比较结构模式 + outcome horizon 已闭合”来定义。
