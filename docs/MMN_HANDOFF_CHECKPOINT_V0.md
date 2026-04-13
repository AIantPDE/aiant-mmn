# MMN_HANDOFF_CHECKPOINT_V0

时间：2026年4月13日

## 1. 目的

本文档用于为当前阶段的 `aiant-mmn` 提供一个可直接接续的新 chat / 新工作面的 handoff checkpoint。

其目标不是重新发明已落地对象，
也不是重新争论 `MMN` 的仓归属，
而是帮助后续工作在统一边界下继续推进。

---

## 2. 最高解释

本 handoff 采用以下规则：

> `AIANTPDE_README` 为最高解释。  
> 若局部 `README` / `docs` 与其冲突，一律以 `AIANTPDE_README` 为准。

因此：

- `MMN` 的本体职责仍以 AIant PDE `[5]` 与 `[6]` 为准
- 当前 `aiant-mmn` 不应再被解释为 `pant` 附属件
- 当前仓只是在其边界内承载最小 memory host 与最小 MMN object host

---

## 3. 当前阶段一句话状态

> `aiant-mmn` 已经从“最小 memory-semantic producer host”推进到“具备最小 MMN 本体对象族与最小 MMN 本体对象链”的阶段；
> 下一步默认先做 checkpoint / fixture / handoff 固化，而不是继续无节制扩对象。

---

## 4. 当前已落地内容

### 4.1 最小 host 正向链已成立

当前最小 host 正向链为：

```text
MemoryStubProviderV0
    -> MemoryPreviewOutputV0
    -> recall_stub_v0
    -> route_preview_memory_adapter_v0
````

它证明当前仓已经具备：

* 最小 preview output 生产能力
* recall-facing / preview-facing 最小消费面
* deterministic output shape
* fail-closed adapter posture

---

### 4.2 record-level bridge 已成立

当前 `MemoryRecordV0` 已明确作为：

* `MemoryPreviewOutputV0.records`

中的最小记录级单元存在。

它的角色是：

* 构成 preview output 内的最小 records
* 为 preview-facing 消费面提供最小 record contract
* 保持最小 identity / trace / reason visibility

它当前不承担：

* 完整 recall object
* 完整 posterior object
* 完整 write-back governance
* execution intent

---

### 4.3 最小 MMN 本体对象族已成立

当前已落地对象包括：

* `HistoricalComparisonObjectV0`
* `PosteriorCorrectionObjectV0`
* `MemoryWriteBackRequestV0`
* `MemoryWriteBackRecordV0`

它们当前表达的是：

* 历史对照
* 后验修正
* 写回请求语义
* 写回记录语义

---

### 4.4 最小 MMN 本体对象链 smoke 已成立

当前对象链为：

```text
HistoricalComparisonObjectV0
    -> PosteriorCorrectionObjectV0
    -> MemoryWriteBackRequestV0
    -> MemoryWriteBackRecordV0
```

已具备：

* object chain smoke
* package export surface
* public export tests
* fail-closed coverage
* contract payload projection helpers

---

## 5. 当前边界总结

当前 `aiant-mmn` 的边界应保持为：

* preview-only
* non-executing
* no worker coupling
* no formal execution payload
* deterministic output shape
* fail-closed integration

这些边界当前默认不应放松。

---

## 6. 当前哪些部分已经足够稳定

当前以下部分可视为阶段性稳定面：

### 6.1 仓定位

“最小 memory-semantic producer host + 最小 MMN object host”

### 6.2 preview output contract

`MemoryPreviewOutputV0`

### 6.3 record-level contract

`MemoryRecordV0`

### 6.4 最小 MMN 对象族

* historical comparison
* posterior correction
* memory write-back request
* memory write-back record

### 6.5 object-chain smoke / export surface

这些已经足够支撑 checkpoint 固化与 fixture 冻结。

---

## 7. 当前哪些部分仍只是 preview-only shell

后续工作必须继续记住：

* `MemoryRecordV0` 只是最小 preview record unit
* `HistoricalComparisonObjectV0` 只是最小 comparison shell
* `PosteriorCorrectionObjectV0` 只是最小 correction shell
* `MemoryWriteBackRequestV0` 只是 semantic request shell
* `MemoryWriteBackRecordV0` 只是 semantic record shell

它们都还不是：

* 完整 recall engine
* 完整 posterior engine
* 完整 persistence layer
* 完整 MMN governance system

---

## 8. 当前默认不要做的事

当前默认不要：

### 8.1 不要重新把 `MMN` 往 `pant` 归属上解释

此前命名校准已完成，
不要回退。

### 8.2 不要跳回去重新发明已落地对象

当前更需要冻结与整理，
不是重新起名或重复造壳。

### 8.3 不要无边界继续扩 object shell

除非理由非常强，
否则默认先不扩 richer objects。

### 8.4 不要把 write-back 误解成 backend mutation

当前只是语义层 request / record shell，
不是执行命令。

### 8.5 不要把 record 层与 richer MMN object 层混在一起

`MemoryRecordV0` 与 historical/posterior/write-back object family 不是同一层。

---

## 9. 当前最推荐的下一步顺序

建议继续推进时按以下顺序进行：

```text
1. 补 architecture checkpoint doc
2. 补 handoff checkpoint doc
3. 补 golden payload fixtures
4. 补 object-chain fixture tests
5. 再判断 richer MMN semantics 是否真的需要
```

---

## 10. 当前建议优先补的文件

### 10.1 文档

建议优先补：

* `docs/MMN_ARCHITECTURE_CHECKPOINT_V0.md`
* `docs/MMN_HANDOFF_CHECKPOINT_V0.md`

若需要，也可顺手补：

* `docs/MMN_FIXTURE_STRATEGY_V0.md`

---

### 10.2 fixtures

建议优先补：

```text
tests/fixtures/memory_preview_output_v0/memory_preview_default.json
tests/fixtures/memory_preview_output_v0/memory_preview_richer.json

tests/fixtures/mmn_object_chain_v0/historical_comparison_alpha.json
tests/fixtures/mmn_object_chain_v0/posterior_correction_alpha.json
tests/fixtures/mmn_object_chain_v0/memory_writeback_request_alpha.json
tests/fixtures/mmn_object_chain_v0/memory_writeback_record_alpha.json
tests/fixtures/mmn_object_chain_v0/mmn_object_chain_light_beta.json
```

这些 fixture 的目标不是追求复杂，
而是冻结：

* version
* id shape
* enum shape
* trace minimality
* reason_codes normalization
* forbidden execution-like fields absence

---

### 10.3 tests

建议优先补：

* `tests/test_memory_preview_output_golden_v0.py`
* `tests/test_mmn_object_chain_golden_v0.py`

推荐测试重点：

* canonical payload 不漂移
* linkage 不漂移
* required fields 不丢失
* forbidden execution-like fields 不渗入
* fixture round-trip / builder consistency 保持稳定

---

## 11. richer MMN semantics 的谨慎进入条件

只有在满足以下任一条件时，
才建议继续扩 richer MMN semantics：

### 11.1 明确下游消费需求出现

例如其他仓确实需要新的 MMN object contract。

### 11.2 现有对象无法表达必要差异

例如 fixture / checkpoint 过程中发现当前对象缺少不可替代字段。

### 11.3 AIANTPDE_README 下的总分层需要显式落一个新对象

且该对象能清楚解释其所在层级、面向谁、是否正式承诺。

若不满足以上条件，
默认继续冻结现有结构即可。

---

## 12. 后续新 chat 建议开场方式

若在新 chat 中继续，可直接用下面的开场说明：

> 继续推进 `aiant-mmn`。
> 以 `AIANTPDE_README` 为最高解释。
> 当前仓定位为：
>
> * preview-only
> * non-executing
> * fail-closed 的最小 memory-semantic producer host
> * 同时已具备最小 MMN 本体对象族与对象链
>   当前优先任务不是继续扩 object shell，
>   而是先做 checkpoint / fixture / contract freeze。

---

## 13. 当前阶段最终 handoff 结论

可以用下面这段话作为本阶段 handoff 总结：

> 当前 `aiant-mmn` 已经具备一次阶段性架构检查点所需的最小条件：
>
> * 仓定位清楚
> * 边界清楚
> * preview output 层已成立
> * record-level contract 已成立
> * 最小 MMN 本体对象族与对象链已成立
> * export / smoke / fail-closed posture 已具备
>
> 因此下一步最合理的方向是：
> 先做 architecture checkpoint、handoff 收口与 golden fixture 冻结，
> 默认暂不继续无边界扩 richer MMN object shell。