# MMN Authority Event Memory V1.3.1 Compatibility Boundary V0

## 边界规则

### Rule 1: 当前业务意图由 V1.3.1 定义

```text
Authority Event Memory V1.3.1 defines current business intent.
```

### Rule 2: V0 只是兼容 surface

```text
V0 preview/writeback/memory seams are compatibility surfaces only.
```

### Rule 3: contracts 拥有 schema truth

```text
aiant-contracts owns accepted schema truth, canonical hash, record id,
field registry alignment and cross-repo object stability.
```

### Rule 4: MMN 不授予执行权

```text
No MMN memory object, preview object, writeback request, audit digest
or probe result may authorize execution.
```

### Rule 5: opportunity candidate 不是买入信号

```text
MMNOpportunityCandidateMemoryRecordV1 is not a buy signal.
```

### Rule 6: risk memory 不是卖出信号

```text
MMNRiskMemoryRecordV1 is not a sell signal.
```

### Rule 7: audit pass 不是因果证明

```text
evidence_supported or high_confidence_candidate does not mean causal proof.
```

### Rule 8: writeback 不是持久化授权

```text
writeback preview / request / record discipline does not grant persistent memory mutation authority.
```

## 禁止措辞

以下措辞不得出现在 docs、tests、fixtures 与未来 payload 中：

```text
confirmed cause
news caused the turning point
opportunity memory says buy
risk memory says sell
memory authorizes execution
writeback grants persistence
audit digest is trading signal
validator pass means causal proof
```

中文语境下也应避免：

```text
已确认因果
新闻导致拐点
机会记忆建议买入
风险记忆建议卖出
记忆授权执行
写回授予持久化权限
审计摘要就是交易信号
validator 通过代表因果成立
```

## 推荐措辞

使用以下更安全的表达：

```text
candidate attribution
evidence-supported candidate
high-confidence candidate
non-executing memory candidate
authority-event retrieval anchor
audit-ready memory candidate
candidate-only opportunity memory
risk perturbation material
no_schema_authority
```

中文表达：

```text
候选归因
证据支持的候选
高置信候选
non-executing 记忆候选
权威事件回溯锚点
审计就绪记忆候选
candidate-only 机会候选记忆
风险扰动材料
无 schema authority
```

## 第一工程入口

第一工程入口必须是 docs/test-only。

可以增加：

- 当前业务意图文档；
- legacy seam alignment 文档；
- compatibility boundary 文档；
- engineering entry plan；
- docs regression tests。

不得增加：

- runtime validator implementation；
- production memory database；
- crawler；
- live ingestion；
- DRL execution；
- trading signal；
- schema authority bypass。
