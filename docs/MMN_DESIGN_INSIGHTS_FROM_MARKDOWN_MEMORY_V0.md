# MMN_DESIGN_INSIGHTS_FROM_MARKDOWN_MEMORY_V0

## 1. 目的

本文档用于说明：

- Markdown-style memory 对 AIant PDE 中 `MMN` 模块的设计启发
- 为什么这些启发不应被简单理解为“把 MMN 做成 Markdown 文件”
- 为什么真正重要的是：
  - 记忆分层
  - recall 治理
  - 历史对照
  - 后验修正
  - 记忆写回纪律
- 这些启发如何与 AIant PDE 当前 `[1]`～`[6]` 总体分层对齐

---

## 2. 当前结论

一句话概括：

> Markdown-style memory 对 `MMN` 的最大启发，
> 不是“文件格式优先”，
> 而是：
> **记忆应先被设计成可分层、可外显、可回写、可校正的主层，
> 再在其上叠加检索、加速与压缩机制。**

也就是说：

- `MMN` 不应只被理解为 memory bank
- `MMN` 不应只被理解为 recall / RAG
- `MMN` 更应被理解为：
  - 系统经验中枢
  - 历史对照层
  - posterior correction engine

---

## 3. 为什么 Markdown-style memory 对 MMN 有启发

当前一些成熟 Agent 系统之所以大量使用 Markdown 文件，
并不只是因为文本文件“容易写”，
而是因为它们天然具备以下特征：

- 人类可读
- 可直接版本管理
- 可直接审查与调试
- 容易形成“主层 + 派生层”的结构
- 可将长期信息外部化，而不必始终占据热上下文

这说明：

> 一个成熟记忆系统最先需要的，
> 往往不是更重的基础设施，
> 而是一个清楚的、可外显的、可被系统与人共同理解的记忆主层。

对 `MMN` 来说，这一点非常重要。

---

## 4. 与 AIant PDE 当前 MMN 定位的关系

在 AIant PDE 当前总体分层中，
`MMN` 的核心职责已被明确描述为：

- 记忆
- 历史对照
- recall
- 上下文支撑
- 后验修正

并且其主战场位于 `[5] 执行与策略层`，
同时又与 `[6] 外部行为与市场作用层` 的反馈回流强相关。

也就是说：

- 在 `[5]` 中，`MMN` 负责为当前候选提供历史支撑
- 在 `[6]` 中，外部结果会重新沉淀成未来 posterior

因此，`MMN` 天然不是一个纯检索模块，
而是一个：

> 既面向当前决策，
> 又面向未来修正的系统经验中枢。

---

## 5. 核心启发一：MMN 应先被设计成“记忆分层系统”

Markdown-style memory 最值得吸收的一个思想是：

> 上下文窗口与外部文件系统并不是同一层存储。

若把这种思路映射到 `MMN`，
则 `MMN` 最合理的第一步不是“统一记忆池”，
而是显式区分不同温度的记忆层。

### 当前建议的最小分层

#### 5.1 热记忆（hot memory）
指当前候选最相关、最该处于热上下文中的支撑内容。

例如：

- 当前对象最相近的近期历史
- 当前 source 的最近可信度提示
- 当前策略最需要看到的 recent posterior

#### 5.2 温记忆（warm memory）
指近期常用、但不必始终贴在当前上下文尾部的背景记忆。

例如：

- 最近一段时间的 pattern summary
- 某类对象近期表现摘要
- 当前市场阶段相关的中期支撑

#### 5.3 冷记忆（cold memory）
指长期持久化、仅在需要时 recall 的历史材料。

例如：

- 长期历史样本
- 旧事件中的结构相似案例
- 长期来源可靠性记录

#### 5.4 后验记忆（posterior memory）
指由外部行为结果、反馈、attribution、post-action diagnosis 回写形成的修正层。

例如：

- 某类扩散叙事历史上经常被高估
- 某类 source 长期存在乐观偏差
- 某类事件窗口通常兑现滞后

一句话概括：

> `MMN` 不是“一块统一 memory”，
> 而应至少是一个有温度、有分层的经验系统。

---

## 6. 核心启发二：recall 不应等同于相似检索

如果仅从通用 AI 工具角度出发，
很容易把 `MMN` 中的 recall 理解为：

- embedding search
- semantic retrieval
- 从记忆库找最相似内容

但在 AIant PDE 语境里，这个理解明显不够。

因为 `MMN` 当前职责不仅包括 recall，
还包括：

- 历史对照
- 上下文支撑
- 后验修正

因此，当前更合理的理解应是：

> `recall` = 受当前对象约束的历史支撑回忆提取

### 当前建议区分的 recall 类型

#### 6.1 相似结构 recall
过去是否出现过相似输入、相似候选、相似传播结构。

#### 6.2 结果对照 recall
过去类似结构最终是兑现、落空、延迟兑现，还是被高估。

#### 6.3 来源可靠性 recall
过去哪些 source / provider / signal family 更可靠。

#### 6.4 修正性 recall
过去系统在哪些地方经常发生：

- 过度乐观
- 传播半径高估
- 风险低估
- 时间窗口判断偏差

因此：

> `MMN` 的 recall 更接近“把当前对象放进历史结果链里比较”，
> 而不只是“搜几段像的话”。

---

## 7. 核心启发三：MMN 不只是 memory bank，而应是 posterior correction engine

这是最重要的一点。

若仅将 `MMN` 理解为：

- memory bank
- context augmenter
- recall helper

则其价值会被严重低估。

更准确的理解应是：

> `MMN` 的真正核心，不在于“记住过去”，
> 而在于“把过去结果转化为当前修正力”。

也就是说，`MMN` 不应只回答：

- 过去有过类似情况吗？

更应回答：

- 过去类似情况通常怎样兑现？
- 过去哪些传播叙事常常被高估？
- 过去哪些风险总是在事后才显现？
- 过去哪些 source 的正面信号兑现率并不高？
- 过去哪些市场阶段对相同信号的反应不同？

一句话概括：

> `MMN` 不只是 memory bank，
> 而应是一个 posterior correction engine。

---

## 8. 核心启发四：MMN 的价值在于“历史对照”，而不仅是“上下文增强”

Markdown-style memory 让人很容易注意到 context augmentation，
即：

- 把旧信息补回当前上下文
- 让当前推理不只看眼前输入

这当然也是 `MMN` 的职责之一，
但不应成为唯一理解。

对 AIant PDE 来说，
`MMN` 更关键的是：

> 历史不是拿来“塞回上下文”而已，
> 历史是拿来“与当前对象做对照”的。

所以 `historical comparison` 应视为 `MMN` 的显式职责，
而不只是 recall 的副产物。

这意味着未来 `MMN` 输出不应只有：

- recalled items
- support text

还应包含类似：

- historical comparison object
- posterior correction object
- memory support object

---

## 9. 核心启发五：MMN 需要写回纪律，而不是只会取不会写

Markdown-style memory 另一个重要启发是：

> 记忆不是自动长出来的，
> 而是通过明确的写入纪律、更新纪律与压缩纪律被维护出来的。

对 `MMN` 同样成立。

如果没有写回纪律，`MMN` 很容易走向两种失败模式：

### 9.1 什么都记
导致：

- 记忆膨胀
- 信号污染
- recall 失真
- 后验难以区分轻重

### 9.2 什么都不真正沉淀
导致：

- 当前上下文里临时补了很多东西
- 但外部结果没有稳定回写
- 系统没有形成真正经验

因此，`MMN` 至少应回答以下问题：

- 哪些 outcome 值得写入长期后验？
- 哪些失败样例值得沉淀？
- 哪些 source reliability 变化需要更新？
- 哪些传播/节律/时间窗口偏差值得进入 correction memory？
- 哪些旧记忆应降权或淘汰？

一句话概括：

> `MMN` 不只是 recall 模块，
> 还必须是记忆写回治理模块。

---

## 10. 核心启发六：MMN 更适合“主层 + 派生层”结构，而不是直接等于向量检索

Markdown-style memory 的一个非常有价值的工程启发是：

> 主层负责保存“真相来源”，
> 派生层负责检索优化。

如果把这个结构映射到 `MMN`，
当前更合理的设计不是：

```text
MMN = vector retrieval system
```

而是：

```text
MMN
  = 可解释记忆主层
  + recall / ranking / retrieval 派生层
```

### 10.1 主层：可解释记忆对象层

例如：

* historical pattern refs
* posterior notes
* source trust notes
* failure exemplars
* memory support summaries

### 10.2 派生层：检索与排序层

例如：

* embedding retrieval
* temporal weighting
* graph-conditioned recall
* similarity ranking
* freshness / decay logic

这样做的价值在于：

* 主层可解释
* recall 层可扩展
* 派生层可以换实现
* 不会让 `MMN` 从一开始就变成黑箱 memory store

---

## 11. MMN 在 `[5]` 与 `[6]` 中的双重角色，应被更清楚地区分

### 11.1 在 `[5] 执行与策略层`

`MMN` 提供：

* 热记忆支撑
* 历史对照
* recall
* context augmentation
* 初步 posterior correction

这一层回答的是：

> 当前对象在历史经验中应该如何被看待？

### 11.2 在 `[6] 外部行为与市场作用层`

`MMN` 通过回写吸收：

* outcome
* attribution
* feedback
* post-action diagnosis
* 市场是否兑现
* 用户是否接受
* 联动是否真实发生

这一层回答的是：

> 外部世界实际发生了什么，这些结果应如何修改未来判断？

所以：

> `[5]` 中的 `MMN` 更偏支撑当前，
> `[6]` 回流后的 `MMN` 更偏修正未来。

---

## 12. 一个金融文本场景下的直观例子

假设输入为：

> “A 公司发布公告称，一季度净利润同比增长 68%，同时披露新增大客户订单。多家券商认为，公司全年业绩指引存在上修可能，产业链设备商与原材料供应商或同步受益。”

在这个场景里：

### `V-ant`

先看懂：

* 哪部分是事实
* 哪部分是推测
* 哪部分是扩散叙事

### `G-ant`

识别：

* 设备商与原材料商可能构成传播扩散路径

### `TFT`

识别：

* 盈利改善与上修预期处于什么时间窗口

### `MMN`

则进一步回答：

* 过去类似“公告事实 + 券商上修预期”组合，通常兑现吗？
* 哪类券商来源历史上更可靠？
* “产业链同步受益”这种叙事过去是否常被高估？
* 当前市场阶段下，这类利好通常立即定价，还是滞后定价？
* 过去哪些类似对象最后形成了正向 posterior，哪些形成了反向修正？

如果后续 `[6]` 发生的结果是：

* A 公司大涨但设备商并未同步
* 原材料商反而走弱
* 券商上修预期后来未兑现

那么这些结果都应回写进 `MMN`，
形成下一次面对此类结构时的 posterior correction。

---

## 13. 当前阶段对 MMN 的设计建议

### 13.1 不要把 MMN 直接等同于 RAG

`RAG` 可以是 recall 的一部分实现路径，
但 `MMN` 还包括：

* 历史对照
* 上下文支撑
* 后验修正
* 记忆写回纪律

### 13.2 不要只做 latent memory，不留显式对象层

若 `MMN` 完全黑箱化，
将来会很难解释：

* 系统到底记住了什么
* 为什么 recall 这个而不是那个
* 为什么形成这样的 posterior 修正

### 13.3 应优先明确 memory objects，而不是先堆更重基础设施

当前最重要的不是“先选哪种 memory database”，
而是先明确：

* 什么值得记住
* 什么值得被回忆提取
* 什么值得成为 posterior
* 什么值得被写回

### 13.4 先把写回纪律写清楚

如果不先定义写回纪律，
`MMN` 很容易只剩下 recall，而没有真正的经验沉淀。

---

## 14. 当前阶段的一句话总结

可以用下面这句话概括本文件的结论：

> Markdown-style memory 对 `MMN` 的最大启发，
> 不是“记忆应当存成 Markdown 文件”，
> 而是：
> **记忆应先作为一个可分层、可外显、可回写、可修正的系统主层存在，
> 再在其上叠加 recall、RAG、排序与加速机制。**

对于 AIant PDE 来说，
这意味着：

> `MMN` 不应只是 memory bank，
> 而应成为系统的历史对照层、上下文支撑层与 posterior correction engine。
