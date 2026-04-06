# MMN_OBJECT_FAMILY_V0

## 1. 目的

本文档用于为 AIant PDE 中的 `MMN` 模块定义当前阶段的最小对象族。

目标不是一次性冻结最终实现，
而是先把以下问题对象化：

- 哪些记忆对象属于热记忆
- 哪些记忆对象属于温记忆
- 哪些记忆对象属于冷记忆
- 哪些对象承载 posterior / correction
- recall 应产出什么对象
- historical comparison 应产出什么对象
- post-action diagnosis 之后应写回什么对象

一句话概括：

> 本文档尝试把 `MMN` 从“抽象记忆模块”压缩成“可讨论、可交换、可验证的对象族”。

---

## 2. 背景与定位

在 AIant PDE 当前总体分层中，`MMN` 的核心职责已被明确表述为：

- 记忆
- 历史对照
- recall
- 上下文支撑
- 后验修正

并且其主战场位于 `[5] 执行与策略层`，
同时又与 `[6] 外部行为与市场作用层` 的 outcome / feedback / attribution / post-action diagnosis 回流强相关。:contentReference[oaicite:0]{index=0}

这意味着：

- `MMN` 不只是 memory bank
- `MMN` 不只是 context augmenter
- `MMN` 不只是 RAG-style retrieval helper

更准确地说：

> `MMN` 应被理解为系统经验中枢，
> 其对象族既要服务当前策略支撑，
> 也要服务未来 posterior correction。

---

## 3. 设计原则

当前阶段建议坚持以下原则：

### 3.1 先对象化，再谈具体存储
先明确：

- 记忆对象长什么样
- recall 输出长什么样
- historical comparison 输出长什么样
- write-back 对象长什么样

而不是一开始先决定数据库、向量索引或文件布局。

### 3.2 先主层，再派生层
记忆对象主层优先表达：

- 语义
- 支撑关系
- correction 关系
- 写回逻辑

检索、排序、嵌入、加速都视为派生层。

### 3.3 不让 MMN 退化成“只会找相似内容”
`MMN` 必须显式承载：

- 历史结果对照
- source trust
- posterior notes
- correction signals

### 3.4 写回必须与 recall 同等重要
若只定义 recall，而不定义 write-back，
则 `MMN` 很容易成为“临时上下文增强器”，而非真正经验系统。

---

## 4. 当前建议的最小对象族

当前建议至少定义以下对象族：

### 4.1 memory layer objects
用于表达不同温度的记忆对象。

包括：

- `HotMemoryObject`
- `WarmMemoryObject`
- `ColdMemoryObject`
- `PosteriorMemoryObject`

### 4.2 recall objects
用于表达一次受当前任务约束的回忆提取结果。

包括：

- `MemoryRecallRequest`
- `MemoryRecallResult`

### 4.3 comparison objects
用于表达当前对象与历史经验之间的对照关系。

包括：

- `HistoricalComparisonObject`

### 4.4 correction objects
用于表达由历史结果或外部结果带来的修正。

包括：

- `PosteriorCorrectionObject`

### 4.5 write-back objects
用于表达从 `[6]` 回流进入 `MMN` 的写回动作。

包括：

- `MemoryWriteBackRequest`
- `MemoryWriteBackRecord`

---

## 5. memory layer objects

## 5.1 HotMemoryObject

### 定义
表示当前候选最相关、最需要处于热上下文中的记忆对象。

### 作用
它回答的是：

> 当前对象最应立即看见的历史支撑是什么？

### 典型内容
可能包括：

- 最近最相似结构的简摘要
- 当前 source 的最近可靠性提示
- 当前时间窗口最相关的 posterior note
- 当前候选最需要看到的失败样例摘要

### 设计要求
- 小
- 热
- 面向当前判断
- 更适合直接进入当前上下文工作区

---

## 5.2 WarmMemoryObject

### 定义
表示近期常用、但不必始终贴在上下文尾部的中温记忆对象。

### 作用
它回答的是：

> 当前判断的中程背景支撑是什么？

### 典型内容
可能包括：

- 最近一段时间的 pattern summary
- 某类对象的中期表现摘要
- 当前市场阶段相关的经验说明
- 某类 source 家族的近阶段表现

### 设计要求
- 比热记忆更宽
- 仍然服务当前任务
- 可按需补入，不要求一直保持最热

---

## 5.3 ColdMemoryObject

### 定义
表示长期持久化、仅在需要时 recall 的较冷记忆对象。

### 作用
它回答的是：

> 系统长期保留了哪些历史经验材料？

### 典型内容
可能包括：

- 长期历史样本
- 较早期但结构重要的案例
- 长期 source trust 记录
- 长期失败样例与对照记录
- 长周期市场结构经验

### 设计要求
- 稳定
- 可长期持久化
- 不要求频繁进入热上下文
- 更适合作为 recall 源头

---

## 5.4 PosteriorMemoryObject

### 定义
表示由 outcome / attribution / feedback / post-action diagnosis 回写形成的后验记忆对象。

### 作用
它回答的是：

> 外部世界已经证明了什么，这些结果应如何修改未来判断？

### 典型内容
可能包括：

- 某类传播叙事常被高估
- 某类券商来源长期过度乐观
- 某类事件窗口通常滞后兑现
- 某类产业链联动经常只有核心标的兑现
- 某类候选风险估计常偏低

### 设计要求
- 不只是记录结果
- 必须携带 correction 含义
- 面向未来策略修正，而不只是历史存档

---

## 6. recall objects

## 6.1 MemoryRecallRequest

### 定义
表示一次面向 `MMN` 的回忆提取请求。

### 核心问题
它回答的是：

> 当前任务究竟想从历史中找回什么？

### 当前建议字段方向
可能包括：

- `request_id`
- `subject_id`
- `current_context_ref`
- `recall_goal`
- `time_horizon`
- `memory_layers_allowed`
- `max_items`
- `source_constraints`

### 说明
`MemoryRecallRequest` 不应只是模糊地说“给我记忆”，
而应至少表达：

- 当前对象是谁
- 要回忆什么类型的历史
- 允许使用哪些记忆层
- 更偏结果对照、来源对照，还是 correction recall

---

## 6.2 MemoryRecallResult

### 定义
表示一次 recall 的结构化输出结果。

### 核心问题
它回答的是：

> 当前任务最终从历史中提取回了哪些支撑？

### 当前建议字段方向
可能包括：

- `request_id`
- `matched_memory_refs`
- `hot_support_items`
- `warm_support_items`
- `cold_support_items`
- `posterior_support_items`
- `support_confidence`
- `recall_notes`

### 说明
`MemoryRecallResult` 不应只返回一堆 raw snippets，
而应显式告诉 downstream：

- 找回了什么
- 这些支撑来自哪个记忆层
- 哪些最值得进入当前上下文
- 这次 recall 的可信度与局限性如何

---

## 7. comparison objects

## 7.1 HistoricalComparisonObject

### 定义
表示当前对象与历史对象之间的对照关系对象。

### 核心问题
它回答的是：

> 当前对象与历史上类似对象相比，最关键的相同点、不同点与结果分岔在哪里？

### 当前建议字段方向
可能包括：

- `comparison_id`
- `subject_id`
- `current_pattern_summary`
- `historical_pattern_refs`
- `matched_dimensions`
- `divergent_dimensions`
- `historical_outcome_summary`
- `comparison_confidence`
- `comparison_notes`

### 说明
这类对象比普通 recall 更进一步：

- recall 解决“找回来什么”
- historical comparison 解决“找回来的东西和当前对象如何比较”

因此它应视为 `MMN` 的核心对象之一，而不是 recall 的附注。

---

## 8. correction objects

## 8.1 PosteriorCorrectionObject

### 定义
表示从历史经验或外部结果中提炼出的、用于修正当前判断的 correction 对象。

### 核心问题
它回答的是：

> 当前候选应当被怎样修正？

### 当前建议字段方向
可能包括：

- `correction_id`
- `subject_id`
- `correction_target`
- `correction_direction`
- `correction_strength`
- `correction_basis`
- `source_refs`
- `posterior_notes`

### 可能的修正目标
例如：

- 风险估计
- 传播半径估计
- 时间窗口估计
- source trust
- candidate promotion confidence
- multi-agent linkage expectation

### 说明
这类对象是 `MMN` 与普通记忆系统最关键的差异之一。

一句话概括：

> `PosteriorCorrectionObject` 让 `MMN` 从“能记住历史”升级为“能用历史修正当前”。

---

## 9. write-back objects

## 9.1 MemoryWriteBackRequest

### 定义
表示一次把外部结果或事后诊断写回 `MMN` 的请求对象。

### 核心问题
它回答的是：

> 这次外部结果中，哪些内容值得写回记忆层？

### 当前建议字段方向
可能包括：

- `write_back_id`
- `subject_id`
- `originating_action_ref`
- `originating_candidate_ref`
- `write_back_reason`
- `target_memory_layer`
- `source_evidence_refs`
- `write_back_mode`

### 说明
写回请求应显式区分：

- 写入热记忆
- 写入温记忆
- 写入冷记忆
- 写入 posterior 记忆

而不是统称“存起来”。

---

## 9.2 MemoryWriteBackRecord

### 定义
表示一次写回动作实际形成的记忆记录对象。

### 核心问题
它回答的是：

> 这次写回最终沉淀成了什么经验对象？

### 当前建议字段方向
可能包括：

- `write_back_id`
- `stored_memory_ref`
- `stored_memory_layer`
- `stored_memory_kind`
- `write_back_status`
- `retention_hint`
- `write_back_notes`

### 说明
它比 `MemoryWriteBackRequest` 更靠后，
更接近“写回完成后留下的已沉淀对象”。

---

## 10. 这些对象与 `[5]`、`[6]` 的关系

## 10.1 `[5] 执行与策略层`
在 `[5]` 中，`MMN` 更偏向输出：

- `MemoryRecallResult`
- `HistoricalComparisonObject`
- `PosteriorCorrectionObject`

它们的作用是：

- 给当前候选提供历史支撑
- 把当前对象放到历史经验中比较
- 对当前策略判断施加 correction

---

## 10.2 `[6] 外部行为与市场作用层`
在 `[6]` 中，`MMN` 更偏向消费：

- outcome
- attribution
- feedback
- post-action diagnosis

并把这些结果转成：

- `MemoryWriteBackRequest`
- `MemoryWriteBackRecord`
- `PosteriorMemoryObject`

一句话概括：

> `[5]` 里的 MMN 更偏“支撑当前”，  
> `[6]` 回流后的 MMN 更偏“修正未来”。

---

## 11. 一个金融文本场景中的对象族流向示意

假设输入为：

> “A 公司发布公告称，一季度净利润同比增长 68%，同时披露新增大客户订单。多家券商认为，公司全年业绩指引存在上修可能，产业链设备商与原材料供应商或同步受益。”

则一个简化流向可以写成：

```text
当前对象
    ↓
MemoryRecallRequest
    ↓
MemoryRecallResult
    ↓
HistoricalComparisonObject
    ↓
PosteriorCorrectionObject
    ↓
影响当前 candidate / risk / uncertainty / promotion judgement
    ↓
外部行为与市场反馈发生
    ↓
post-action diagnosis / attribution / outcome
    ↓
MemoryWriteBackRequest
    ↓
MemoryWriteBackRecord
    ↓
PosteriorMemoryObject
```

这条链说明：

* recall 不是终点
* comparison 不是装饰
* correction 才是 MMN 对当前策略真正施加影响的地方
* write-back 则决定系统是否真的拥有经验积累能力

---

## 12. 当前阶段最重要的工程判断

### 12.1 先定义对象族，不先定义重基础设施

当前最重要的不是先选：

* 向量数据库
* 图数据库
* 文件组织方式
* cache 层产品

而是先把 `MMN` 真正交换、真正消费、真正写回的对象定义出来。

### 12.2 先保证对象可解释，再谈更复杂加速层

如果未来要叠加：

* embedding retrieval
* graph-conditioned recall
* temporal weighting
* decay policies
* memory compression

也应当建立在上述对象族已经清楚的前提之上。

### 12.3 不让 MMN 退化成“只负责找历史”

如果对象族里只有 recall request / recall result，
而没有 historical comparison / posterior correction / write-back family，
则 MMN 会退化为普通 memory retriever。

---

## 13. 当前阶段的一句话总结

可以用下面这句话概括本文档的作用：

> `MMN_OBJECT_FAMILY_V0` 的目标，
> 是先把 `MMN` 从抽象“记忆模块”压缩为：
>
> * 分层记忆对象
> * recall 对象
> * 历史对照对象
> * posterior 修正对象
> * 写回对象
>
> 从而让 `MMN` 真正承担起：
> **历史支撑、当前修正与未来经验沉淀** 的三重职责。
