## 1. 目的

本文档用于给出一个最小、可讨论、可扩展的 `MMN` 流向示例。

目标不是冻结最终实现，
而是帮助说明：

- 当前对象如何触发一次 memory recall
- recall 结果如何进入 historical comparison
- comparison 如何进一步形成 posterior correction
- 外部结果如何通过 write-back 重新沉淀为 future memory

一句话概括：

> 本文档尝试把 `MMN` 的“记忆、历史对照、上下文支撑、后验修正、写回”压缩成一条最小可见链。

---

## 2. 当前背景

在 AIant PDE 当前总体分层中，`MMN` 的职责包括：

- 记忆
- 历史对照
- recall
- 上下文支撑
- 后验修正

其主战场在 `[5] 执行与策略层`，
并且与 `[6] 外部行为与市场作用层` 的 outcome / feedback / attribution / post-action diagnosis 回流紧密相连。:contentReference[oaicite:0]{index=0}

因此，`MMN` 的最小流向不应被理解为：

```text
input -> retrieve -> done
```

而应更接近：

```text
current object
    -> recall
    -> historical comparison
    -> posterior correction
    -> candidate support
    -> external result
    -> post-action diagnosis
    -> memory write-back
    -> future posterior
```

---

## 3. 示例输入文本

使用一条金融文本作为统一示例：

> “A 公司发布公告称，一季度净利润同比增长 68%，同时披露新增大客户订单。多家券商认为，公司全年业绩指引存在上修可能，产业链设备商与原材料供应商或同步受益。”

这条文本的最小语义直观包括：

* `事实`: 净利润同比增长 68%，新增大客户订单
* `推测`: 全年业绩指引可能上修
* `扩散叙事`: 产业链设备商与原材料供应商或同步受益

此时，`MMN` 不负责最初事实/推测的语义拆分，
那更接近 `V-ant`、`G-ant`、`TFT` 的职责；
但在这些最小语义已经形成之后，
`MMN` 负责把当前对象放进“历史经验场”里看。

---

## 4. 最小对象链

当前建议的最小对象链如下：

```text
current object
    ↓
MemoryRecallRequest
    ↓
MemoryRecallResult
    ↓
HistoricalComparisonObject
    ↓
PosteriorCorrectionObject
    ↓
memory-supported candidate view
    ↓
external outcome / attribution / feedback
    ↓
MemoryWriteBackRequest
    ↓
MemoryWriteBackRecord
    ↓
PosteriorMemoryObject
```

---

## 5. 第一步：形成当前对象

这里假设在 `[5] 执行与策略层` 中，
系统已经通过前序模块形成一个最小当前对象视图。

它不必是正式 contract，
但至少应表达：

* 当前主体是谁
* 当前叙事属于什么结构
* 当前对象希望回忆什么历史支撑

例如一个简化的当前对象摘要可写成：

```json
{
  "subject_id": "A_company_earnings_signal_v0",
  "current_pattern_summary": {
    "fact_signal": "profit_growth_68pct",
    "narrative_signal": "guidance_upgrade_possible",
    "propagation_hint": "supply_chain_benefit_possible"
  },
  "current_stage_hint": "earnings_repricing_window"
}
```

这一步不是 MMN 独自完成的，
而是 MMN 的上游输入前提。

---

## 6. 第二步：生成 `MemoryRecallRequest`

### 6.1 作用

`MemoryRecallRequest` 用来明确：

> 当前对象究竟想从历史中找回什么？

它的价值在于避免 MMN 退化成模糊搜索器。

### 6.2 本例中的直观需求

当前对象真正想回忆的不是“所有相似文本”，
而更可能是：

* 历史上类似“公告事实 + 券商上修预期”的案例
* 历史上“产业链同步受益”叙事是否经常兑现
* 当前 source family 历史可靠性
* 当前窗口下类似事件的兑现节奏

### 6.3 一个最小示例

```json
{
  "request_id": "mmn_recall_req_0001",
  "subject_id": "A_company_earnings_signal_v0",
  "recall_goal": [
    "similar_pattern_history",
    "historical_outcome_support",
    "source_trust_support",
    "posterior_correction_support"
  ],
  "time_horizon": "near_to_mid_term",
  "memory_layers_allowed": [
    "hot",
    "warm",
    "cold",
    "posterior"
  ],
  "max_items": 6
}
```

### 6.4 解释

这里要强调：

* `recall_goal` 明确表达“要找哪种历史支撑”
* `memory_layers_allowed` 表达本次 recall 允许动用哪些层
* `time_horizon` 表达当前策略更关注的兑现窗口

也就是说：

> recall 不只是“去搜一搜”，而是一次受当前对象约束的历史支撑提取请求。

---

## 7. 第三步：形成 `MemoryRecallResult`

### 7.1 作用

`MemoryRecallResult` 回答的是：

> 当前任务最终从历史经验中提取回了什么？

### 7.2 本例中的可能 recall 内容

对于这条金融文本，MMN 可能找回：

* 近期 2 个类似“盈利改善 + 上修预期”组合案例
* 1 个“产业链同步受益叙事最终未兑现”的失败样例
* 1 条关于当前券商 source family 的乐观偏差记录
* 1 条当前阶段下“利好先兑现核心标的、扩散后兑现不稳定”的 posterior note

### 7.3 一个最小示例

```json
{
  "request_id": "mmn_recall_req_0001",
  "matched_memory_refs": [
    "mem_case_earnings_upgrade_021",
    "mem_case_earnings_upgrade_034",
    "mem_failure_supply_chain_sync_008",
    "mem_source_trust_broker_family_003",
    "mem_posterior_core_vs_chain_lag_002"
  ],
  "hot_support_items": [
    {
      "memory_ref": "mem_case_earnings_upgrade_034",
      "support_kind": "recent_similar_pattern",
      "support_summary": "同类盈利改善 + 上修预期组合在近阶段通常先兑现核心标的。"
    }
  ],
  "warm_support_items": [
    {
      "memory_ref": "mem_case_earnings_upgrade_021",
      "support_kind": "mid_term_pattern_summary",
      "support_summary": "产业链扩散受益叙事存在分化，设备商兑现率高于原材料商。"
    }
  ],
  "cold_support_items": [
    {
      "memory_ref": "mem_failure_supply_chain_sync_008",
      "support_kind": "historical_failure_exemplar",
      "support_summary": "过往相似叙事中，‘同步受益’表述常被高估。"
    }
  ],
  "posterior_support_items": [
    {
      "memory_ref": "mem_posterior_core_vs_chain_lag_002",
      "support_kind": "posterior_note",
      "support_summary": "核心标的通常先被重估，链条扩散兑现存在更强不确定性。"
    }
  ],
  "support_confidence": "medium_to_high",
  "recall_notes": "当前 recall 更支持核心标的优先重估，弱支持链条同步扩散。"
}
```

### 7.4 解释

这里最重要的不是“找回了多少条”，而是：

* 支撑来自哪个记忆层
* 哪些是正向支撑
* 哪些是失败样例
* 哪些属于 posterior correction 类型

这说明：

> Recall 结果本身就不应只是 raw snippets，
> 而应已具备层级化与支撑语义。

---

## 8. 第四步：形成 `HistoricalComparisonObject`

### 8.1 作用

`HistoricalComparisonObject` 回答的是：

> 当前对象与历史上类似对象相比，最关键的相同点、不同点与结果分岔在哪里？

它比 recall 更进一步，因为它不是简单“把旧材料搬回来”，
而是在做结构比较。

### 8.2 本例中的比较重点

当前对象可能与历史案例有以下相同点：

* 都是公告确认了基本面改善
* 都有 sell-side 上修预期
* 都伴随链条扩散叙事

但不同点可能包括：

* 当前市场阶段对类似利好已更敏感
* 当前上游/下游链条价格传导条件不同
* 当前 source family 可靠性较历史均值更弱或更强
* 当前扩散叙事的兑现条件更苛刻

### 8.3 一个最小示例

```json
{
  "comparison_id": "mmn_cmp_0001",
  "subject_id": "A_company_earnings_signal_v0",
  "current_pattern_summary": {
    "core_fact": "profit_growth_68pct",
    "upgrade_hint": "guidance_upgrade_possible",
    "chain_hint": "supply_chain_benefit_possible"
  },
  "historical_pattern_refs": [
    "mem_case_earnings_upgrade_021",
    "mem_case_earnings_upgrade_034"
  ],
  "matched_dimensions": [
    "profit_improvement_fact",
    "sell_side_upgrade_expectation",
    "supply_chain_narrative_present"
  ],
  "divergent_dimensions": [
    "current_market_stage_more_sensitive",
    "chain_realization_conditions_weaker",
    "source_family_bias_more_optimistic"
  ],
  "historical_outcome_summary": {
    "core_asset_realization_rate": "high",
    "supply_chain_sync_realization_rate": "medium_to_low"
  },
  "comparison_confidence": "medium",
  "comparison_notes": "当前对象与历史上‘核心先兑现、链条分化兑现’模式更接近。"
}
```

### 8.4 解释

这一步的意义是：

* recall 让系统“想起”历史
* comparison 让系统“把当前放进历史坐标系中看”

也就是说：

> `HistoricalComparisonObject` 是 MMN 从“记忆模块”走向“经验模块”的关键中间对象。

---

## 9. 第五步：形成 `PosteriorCorrectionObject`

### 9.1 作用

`PosteriorCorrectionObject` 回答的是：

> 当前候选应当被怎样修正？

这是 MMN 最核心的地方之一。

如果没有 correction，对当前策略就只剩下“有历史支撑”；
而有了 correction，过去结果才真正开始改写现在。

### 9.2 本例中的修正方向

基于 recall 与 historical comparison，MMN 可能形成：

* 提高核心标的候选的支撑强度
* 下调“产业链同步扩散”的确信度
* 下调原材料商联动预期
* 保留设备商受益可能，但降低 promotion confidence
* 对 sell-side optimism 做适度折价

### 9.3 一个最小示例

```json
{
  "correction_id": "mmn_corr_0001",
  "subject_id": "A_company_earnings_signal_v0",
  "correction_target": [
    "core_asset_promotion_confidence",
    "supply_chain_propagation_expectation",
    "source_trust_weight"
  ],
  "correction_direction": {
    "core_asset_promotion_confidence": "up",
    "supply_chain_propagation_expectation": "down",
    "source_trust_weight": "slightly_down"
  },
  "correction_strength": {
    "core_asset_promotion_confidence": "medium_up",
    "supply_chain_propagation_expectation": "medium_down",
    "source_trust_weight": "light_down"
  },
  "correction_basis": [
    "historical_core_asset_realization_high",
    "historical_chain_sync_realization_low",
    "source_family_optimism_bias_present"
  ],
  "posterior_notes": [
    "核心标的优先兑现概率高于链条同步扩散。",
    "链条扩散叙事不宜与核心公告事实同强度处理。"
  ]
}
```

### 9.4 解释

这是当前示例中最重要的一步。

因为它说明 MMN 不只是说：

* “我找到类似案例了”

而是在说：

* “根据历史与后验，当前对象应作何种方向与强度的修正”

因此：

> `PosteriorCorrectionObject` 才是 MMN 真正把历史转化成当前策略修正力的地方。

---

## 10. 第六步：形成 memory-supported candidate view

### 10.1 作用

前面几个对象（recall / comparison / correction）不是终点，
它们要进一步影响当前 `[5]` 层的 candidate / risk / uncertainty / promotion judgement。

### 10.2 本例中的候选支撑结果

经过 MMN 支撑后，一个更接近 candidate synthesis 的结果可能变成：

* 对 A 公司核心标的形成较强 preview candidate support
* 对设备商形成弱到中等联动 support
* 对原材料商不形成强联动 promotion
* 对“产业链同步受益”的解释文本加入明确 uncertainty 与 risk slice

### 10.3 说明

这里的重点是：

> MMN 不直接生成最终执行动作，
> 但它显著影响：
>
> * candidate 的强弱
> * propagation 的可信度
> * uncertainty 的表达
> * risk 的解释

这与 AIant PDE 中 `[5]` 的对象塑形逻辑是对齐的。

---

## 11. 第七步：外部结果与 `post-action diagnosis`

### 11.1 假设的外部结果

假设后续 `[6]` 层真实发生的外部后果是：

* A 公司股价快速上行
* 设备商仅弱跟随
* 原材料商没有明显受益
* 券商后续虽然维持乐观叙事，但市场并未同步全面扩散

### 11.2 `post-action diagnosis` 的最小问题

此时系统应回答：

* 哪部分判断是对的？
* 哪部分扩散被高估？
* 哪些 source 权重需要修正？
* 哪些 propagation expectations 应当回写为 posterior？

### 11.3 一个直观诊断结论

例如：

* 核心资产直接重估判断正确
* 产业链“同步受益”叙事被高估
* 原材料链条联动预期应降权
* 当前 source family 的扩散型叙事可信度应轻度下调

这里就进入了 `MemoryWriteBackRequest` 的前提阶段。

---

## 12. 第八步：形成 `MemoryWriteBackRequest`

### 12.1 作用

`MemoryWriteBackRequest` 回答的是：

> 这次外部结果中，哪些内容值得真正沉淀回 MMN？

### 12.2 本例中的写回意图

系统可能决定写回以下内容：

* 一条新的 posterior：核心资产先兑现、链条扩散常分化
* 一条 source trust correction：当前券商 family 在扩散叙事上偏乐观
* 一条失败样例：原材料商同步受益未兑现

### 12.3 一个最小示例

```json
{
  "write_back_id": "mmn_wb_req_0001",
  "subject_id": "A_company_earnings_signal_v0",
  "originating_action_ref": "route_preview_action_candidate_0001",
  "originating_candidate_ref": "route_preview_candidate_0001",
  "write_back_reason": [
    "posterior_update_required",
    "source_trust_correction_required",
    "failed_chain_sync_exemplar"
  ],
  "target_memory_layer": [
    "posterior",
    "cold"
  ],
  "source_evidence_refs": [
    "outcome_trace_0001",
    "post_action_diagnosis_0001"
  ],
  "write_back_mode": "structured_posterior_update"
}
```

### 12.4 解释

这里强调的是：

* 写回不是“所有结果都存”
* 而是明确区分：

  * 为什么要写
  * 写去哪层
  * 基于哪些证据写

---

## 13. 第九步：形成 `MemoryWriteBackRecord`

### 13.1 作用

`MemoryWriteBackRecord` 回答的是：

> 这次写回最终沉淀成了什么稳定经验对象？

### 13.2 一个最小示例

```json
{
  "write_back_id": "mmn_wb_req_0001",
  "stored_memory_ref": "mem_posterior_core_vs_chain_lag_003",
  "stored_memory_layer": "posterior",
  "stored_memory_kind": "propagation_realization_correction",
  "write_back_status": "stored",
  "retention_hint": "medium_to_long_term",
  "write_back_notes": "新增 posterior：核心公告利好通常先兑现核心标的，链条同步扩散兑现不稳定。"
}
```

### 13.3 解释

写回记录的价值在于：

* 以后 recall 时，这条经验就不再只是外部结果碎片
* 而是已经成为一条结构化、可被 future correction 使用的 posterior memory

---

## 14. 第十步：形成新的 `PosteriorMemoryObject`

### 14.1 作用

最终，上一轮 `[6]` 的结果被吸收成未来 `[5]` 可使用的 posterior memory。

这意味着下一次系统再遇到：

* 公告事实 + 券商上修预期
* 并伴随“产业链同步受益”叙事

时，MMN 会更早、更强地提醒系统：

* 核心标的和链条扩散不能同强度处理
* “同步受益”应默认带更高 uncertainty
* source optimism bias 需纳入 correction

### 14.2 说明

这一步正是 MMN 与普通检索模块的关键差别：

> 它不是只把旧资料找出来，
> 而是把旧结果沉淀成未来判断的一部分。

---

## 15. 当前最小链条的意义

这条链的意义不是在当前阶段就冻结所有对象字段，
而是先明确：

### 15.1 recall 不是终点

Recall 只是记忆流的入口之一。

### 15.2 comparison 必须独立出来

不然 MMN 会退化成“搜一堆旧资料”。

### 15.3 correction 才是 MMN 真正改变系统的地方

如果没有 correction，历史只是背景；
有了 correction，历史才会改写当前 candidate。

### 15.4 write-back 决定系统是否真的拥有经验

没有 write-back，就没有稳定 posterior；
没有 posterior，MMN 就只剩下短期上下文增强功能。

---

## 16. 与当前 `aiant-mmn` 仓边界的关系

若把这条链映射到当前 `aiant-mmn` 的仓边界，
则更适合理解为：

* `contracts/`：逐步吸收已稳定的 preview output / memory record / recall-facing 对象
* `providers/`：在当前阶段先提供 stub memory support
* `recall/`：承接最小 recall 行为
* `adapters/`：把 route preview seam 与 memory preview output 接起来
* `docs/`：先把对象族与最小流向讲清楚，再决定哪些上升到正式 shared contract

也就是说：

> 当前文档的作用不是提前把所有 MMN 语义塞进 `aiant-contracts`，
> 而是先在 `aiant-mmn` 内部把模块对象链讲清楚。

---

## 17. 当前阶段的一句话总结

可以用下面这句话概括本文档：

> `MMN_MINIMAL_FLOW_EXAMPLE_V0` 试图说明：
>
> * 当前对象如何触发 recall
> * recall 如何进入 historical comparison
> * comparison 如何形成 posterior correction
> * correction 如何影响 candidate synthesis
> * 外部结果如何通过 post-action diagnosis 回写为 posterior memory
>
> 也就是说，
> `MMN` 真正的闭环不是“记住过去”，
> 而是：
> **过去支撑当前，当前经外部结果检验，再沉淀成未来修正。**
