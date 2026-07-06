# AIANT 链路类术语规范 V0 / AIANT Linkage-family Terminology V0

Status: draft terminology guidance  
Scope: AIANT documentation and regression-test wording  
Boundary: terminology-only; docs/manifest/tests only; non-executing; non-authorizing

Sentinel: `AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0_READY`

## 1. 目的

AIANT 文档中经常出现类似 `A -> B` 的关系表达。很多关系在中文里都容易被泛泛翻译成“链路”，但它们治理的对象并不相同。

本规范用于避免将 `chain`、`lane`、`trace`、`route`、`path`、`lineage`、`bridge`、`seam`、`handoff`、`loop` 等术语全部压缩成一个含混的“链路”。

默认规则是：

```text
不要把每一个 A -> B 关系都翻译成“链路”。
“链路”只可作为宽泛家族标签，或在文档明确强调阶段之间连接关系时使用。
在精确术语中，应根据被治理对象选择更具体的中文词。
```

## 2. 快速判断规则

```text
先问：“这里治理的是什么？”

- mandatory stage order              -> chain / 有序链
- work-family classification         -> lane / 治理路线
- replayable historical record       -> trace / 可追溯轨迹
- topological reachability           -> path / 路径
- selected processing direction      -> route / 路由
- data or information movement       -> flow / 流 / 流程 / 信息流
- staged processing machinery        -> pipeline / 管线 / 流水线
- source inheritance                 -> lineage / 血缘 / 来源谱系
- source trust metadata              -> provenance / 来源证明 / 出处 / 来源元信息
- audit record of steps              -> audit trail / 审计轨迹
- safe cross-layer connection        -> bridge / 桥接 / 过桥
- thin module interface              -> seam / 接缝 / 接口接缝
- upstream-to-downstream transfer    -> handoff / 移交 / 交接 / 移交信封
- feedback return                    -> loop / 闭环 / 回路
- one object-to-object relation      -> link / 关联 / 链接
- externally consumable interface set-> surface / 暴露面 / 合同表面
- allow/deny scope                   -> boundary / 边界
```

压缩口诀：

```text
chain 管顺序；
lane 管归类；
trace 管复盘；
path 管可达；
route 管准入选择；
lineage 管来源继承；
bridge 管跨层连接；
seam 管薄接口；
handoff 管移交；
loop 管反馈回流。
```

## 3. 规范术语表

| English term | 推荐中文 | 不建议泛译 | 治理对象 | 判断问题 |
|---|---|---|---|---|
| `chain` | 有序链 / 方法链 / 流程链 | 链路 | 强制阶段顺序 | 下一步必须是什么？ |
| `lane` | 治理路线 / 工作路线 / 归类通道 | 链路 | 工作家族归类 | 这批工作属于哪类路线？ |
| `trace` | 可追溯轨迹 / 审计轨迹 / 修正轨迹 | 链路 | 可复盘历史 | 它怎么走到现在？ |
| `path` | 路径 | 链路 | 拓扑可达性 | 拓扑上能不能到？ |
| `route` | 路由 | 链路 | 被选择或被准入的处理方向 | 实际选择哪条走？ |
| `flow` | 流 / 流程 / 信息流 | 链路 | 数据、控制或信息移动 | 数据或信息怎么流？ |
| `pipeline` | 管线 / 流水线 | 链路 | 分阶段处理机制 | 哪些处理阶段串起来？ |
| `lineage` | 血缘 / 来源谱系 / 证据血缘 | 链路 | 来源继承关系 | 来源从哪里继承？ |
| `provenance` | 来源证明 / 出处 / 来源元信息 | 链路 | 来源可信元信息 | 谁证明来源可信？ |
| `audit trail` | 审计轨迹 | 链路 | 审计复盘记录 | 证据如何被审计复盘？ |
| `bridge` | 桥接 / 过桥 | 链路 | 安全跨层连接 | 两个层之间如何安全连接？ |
| `seam` | 接缝 / 接口接缝 | 链路 | 薄模块接口 | 两个模块的薄接口在哪里？ |
| `handoff` | 移交 / 交接 / 移交信封 | 链路 | 上游到下游的责任或上下文转移 | 上游如何交给下游？ |
| `loop` | 闭环 / 回路 | 链路 | 反馈回流 | 反馈如何回流？ |
| `link` | 关联 / 链接 | 链路 | 两个对象之间的一条关系 | 两个对象有什么关系？ |
| `surface` | 暴露面 / 合同表面 | 链路 | 可被外部消费的接口集合 | 哪些东西可被消费？ |
| `boundary` | 边界 | 链路 | 允许 / 禁止范围 | 哪里不能越界？ |

## 4. 必须区分的术语组

### 4.1 `chain` vs `lane` vs `trace`

`chain` 用于定义概念、能力或操作阶段之间的强制顺序。

```text
AEM ordered chain:
Observed Signal -> Authority Retrieval -> Attribution -> Anti-bias Review ->
Memory Promotion / Deferral / Denial -> Future Reuse
```

`lane` 用于对一组工作、PR、文档、fixture 或 governance review 进行工作家族归类。

```text
field-registry-feedback lane
governance-boundary lane
scanner-preparation lane
contracts schema promotion lane
runtime activation lane
```

`trace` 用于记录某个具体对象、PR 家族、receipt、decision 或 evidence item 如何到达当前状态。

```text
CAGP V2 -> V2_GVR_BRIDGE -> V3 trace
promotion decision trace
field derivation correction trace
receipt trace
```

规范规则：

```text
chain = method/order;
lane  = work-family classification;
trace = replayable history.

chain 表示方法或阶段顺序；
lane 表示工作家族归类；
trace 表示可复盘历史。
```

### 4.2 `path` vs `route`

`path` 描述拓扑上的可能可达性。  
`route` 描述已经被选择、准入、预览或拒绝的处理方向。

```text
runtime topology path      -> 运行时拓扑路径
route preview              -> 路由预览
route admission            -> 路由准入
route denial               -> 路由拒绝
```

规范规则：

```text
path 关注可达性；
route 关注选择、准入和拒绝。
```

### 4.3 `lineage` vs `provenance` vs `trace`

`lineage` 记录派生、继承或来源谱系。  
`provenance` 记录来源可信元信息与出处证明。  
`trace` 记录可复盘的过程历史。

```text
evidence lineage       -> 证据血缘
source provenance      -> 来源证明
promotion trace        -> 晋级审计轨迹
```

规范规则：

```text
lineage answers: derived from what?
provenance answers: origin proven by what?
trace answers: happened through which steps?

lineage 回答：从什么派生而来？
provenance 回答：出处由什么证明？
trace 回答：经历了哪些步骤？
```

### 4.4 `bridge` vs `seam` vs `handoff`

`bridge` 是安全的跨层连接。  
`seam` 是薄模块接口或接缝。  
`handoff` 是阶段之间对 envelope、责任或上下文的移交。

```text
[4] -> [5] bridge                 -> [4] 到 [5] 过桥
explain_bundle seam               -> explain_bundle 接缝
execution_handoff_envelope        -> 执行移交信封
```

规范规则：

```text
bridge = cross-layer connection;
seam = thin interface;
handoff = upstream-to-downstream transfer.

bridge 表示跨层连接；
seam 表示薄接口接缝；
handoff 表示上游到下游的移交。
```

### 4.5 `flow` vs `pipeline` vs `loop`

`flow` 描述数据、控制或信息的移动。  
`pipeline` 描述按阶段串起来的处理机制。  
`loop` 描述反馈回流或闭环校正。

```text
information flow                   -> 信息流
discover extraction pipeline        -> discover 抽取管线
feedback validation loop            -> 反馈验证闭环
```

规范规则：

```text
flow moves;
pipeline processes in stages;
loop returns feedback.

flow 表示流动；
pipeline 表示分阶段处理；
loop 表示反馈回流。
```

### 4.6 `link` vs `chain`

`link` 是两个对象之间的一条关系。  
`chain` 是多个关系或阶段构成的有序序列。

```text
attribution_link_ref               -> 归因关联引用
attribution chain construction      -> 归因链构造
```

规范规则：

```text
link = one relation;
chain = ordered relation sequence.

link 是一条关系；
chain 是有序关系序列。
```

### 4.7 `surface` vs `boundary`

`surface` 描述可被外部消费的对象、接口或合同集合。  
`boundary` 描述允许 / 禁止的治理范围。

```text
accepted schema surface             -> accepted schema 暴露面
non-authorizing boundary            -> 非授权边界
runtime boundary                    -> 运行时边界
```

规范规则：

```text
surface says what is consumable;
boundary says what must not be crossed.

surface 说明什么可以被消费；
boundary 说明什么不能越界。
```

## 5. AIANT 用法示例

### 5.1 GVR / AEM / CAGP

当强调概念顺序时，用 `chain`：

```text
GVR-to-AEM ordered chain:
Raw Natural Language -> Display -> Observed Signal Anchor -> ORSC Gate ->
Authority Retrieval -> Attribution -> Memory
```

当强调工作推进家族时，用 `lane`：

```text
GVR semantic front-end alignment lane
```

当强调理论修正历史时，用 `trace`：

```text
CAGP V2 -> V2_GVR_BRIDGE -> CAGP V3 semantic-front-end correction trace
```

当强调单个 AEM 关系对象时，用 `link`：

```text
attribution_link_ref is a relation between a turning point and an authority event.
It is not the full AEM attribution chain.
```

### 5.2 MMN AEM 字段推导

字段反馈工作家族使用 `lane`：

```text
AEM field-pressure discovery lane
field-registry-feedback lane
```

审查历史使用 `trace`：

```text
AEM seed scenario field derivation trace
AEM-3 attribution hypothesis pressure correction trace
```

前置记忆来源关系使用 `lineage`：

```text
predecessor memory lineage
predecessor receipt lineage
```

归因构造阶段顺序使用 `chain`：

```text
AEM-3 attribution chain construction
```

### 5.3 P-ant / runtime boundary 文档

涉及 preview、admission、denial 或 scheduler selection 时，用 `route`：

```text
route_preview
route_admission
route_denial
scheduler_route
```

描述拓扑可达性时，用 `path`：

```text
topology path
runtime topology path
```

上游对象移交给 guarded downstream reader 时，用 `handoff`：

```text
execution_handoff_envelope
handoff_read_side_adapter
```

强调安全跨层连接时，用 `bridge`：

```text
runtime [4] -> [5] bridge
```

## 6. 禁止性泛译示例

下面的翻译不建议使用，因为它们掩盖了被治理对象。

```text
route_preview                      != 路由链路预览
execution_handoff_envelope          != 执行链路信封
attribution_link_ref                != 归因链路引用, when it means a single relation
field-registry-feedback lane        != 字段注册反馈链路, when it means a work lane
promotion decision trace            != 晋级决策链路, when it means replay history
source provenance                   != 来源链路, when it means origin proof
feedback validation loop            != 反馈验证链路, when it means a closed loop
accepted schema surface             != accepted schema 链路, when it means consumable surface
non-authorizing boundary            != 非授权链路, when it means a boundary
```

更安全的写法是：

```text
route_preview                       -> 路由预览
execution_handoff_envelope           -> 执行移交信封
attribution_link_ref                 -> 归因关联引用
field-registry-feedback lane         -> 字段注册反馈治理路线
promotion decision trace             -> 晋级决策审计轨迹
source provenance                    -> 来源证明
feedback validation loop             -> 反馈验证闭环
accepted schema surface              -> accepted schema 暴露面
non-authorizing boundary             -> 非授权边界
```

## 7. 边界

本术语规范仅用于文档与测试用语指导。

它不会：

```text
- create formal field registry entries
- change contracts schema
- change runtime routing
- authorize memory write
- authorize execution
- modify scanner implementation
- create a new governance rule by itself
```

中文说明：

```text
- 不创建 formal field registry 条目
- 不修改 contracts schema
- 不修改 runtime routing
- 不授权 memory write
- 不授权 execution
- 不修改 scanner implementation
- 不单独创建新的治理规则
```

本规范可作为后续文档、治理 checklist 或 scanner-readiness plan 的稳定词汇来源。

## 8. 最小采用检查清单

在 AIANT 文档中使用“链路”前，先问：

```text
1. 这是强制有序阶段吗？如果是，用 有序链。
2. 这是工作家族归类吗？如果是，用 治理路线。
3. 这是可复盘历史记录吗？如果是，用 可追溯轨迹。
4. 这是拓扑可达性吗？如果是，用 路径。
5. 这是被选择或被准入的处理方向吗？如果是，用 路由。
6. 这是来源继承吗？如果是，用 血缘。
7. 这是跨层连接吗？如果是，用 桥接。
8. 这是薄接口吗？如果是，用 接缝。
9. 这是上游到下游的移交吗？如果是，用 移交。
10. 这是反馈回流吗？如果是，用 闭环。
```

如果以上都不符合，应优先选择领域专用词，而不是泛用“链路”。
