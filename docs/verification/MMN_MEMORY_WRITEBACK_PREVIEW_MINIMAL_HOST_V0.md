# MMN Memory Writeback Preview Minimal Host V0

- 阶段标记：`STAGE-MBI-27`
- 段落标记：`MMN-MBI-B2-I1`
- 来源段落：`MMN-MBI-B2-P1`
- Lane：`MBI-BI-B2`
- 仓库：`aiant-mmn`
- 阶段：`Mmn-VB-memory-writeback-preview-minimal-host-implementation-next`
- 状态：`MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_READY`

## 1. 本轮目的

本轮在 `aiant-mmn` 中落地 memory-writeback preview 的最小宿主位。该宿主位只生成
repo-local、read-side、reference-only、preview-only 对象，不执行真实 memory write，不触发持久化
memory mutation，不接入 runtime loader、worker、scheduler、PANT intake、ZANT-LLM 或 DMF。

同一 PR 中先以独立 commit 修复既有 Pyright baseline debt：

```text
src/mmn/recall/recall_stub_v0.py
reason_codes: object -> explicit Iterable fail-closed guard
```

该修复只收窄静态类型证明路径，不新增业务能力。

## 2. Minimal host shape

```text
preview_version=memory_writeback_preview_v0
preview_state=reference_only_preview
memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_granted=False
```

## 3. Fail-closed 输入边界

任何 execution-like、runtime-like、worker-like、DMF-like 或 shared-contract-expansion 字段进入
`material` 时，builder 都会拒绝构建：

```text
memory_write_authorized
persistent_memory_mutation_authorized
runtime_authority_granted
route_decision
fetch_command
scheduler_apply
queue_mutation
worker_dispatch
execution_payload
provider_backend_call
model_call
shared_contract_expansion
dmf_bootstrap
```

## 4. 保持关闭

```text
memory_write_authorized=False
persistent_memory_mutation_authorized=False
mmn_consumption_enabled=False
pant_runtime_facing_intake_started=False
zant_llm_provider_connected=False
mbi_implementation_fanout_started=False
dmf_bootstrap_started=False
shared_contract_expansion_started=False
runtime_loader_changed=False
worker_activation_started=False
side_effecting_execution_authorized=False
runtime_authority_granted=False
```

## 5. 下一阶段

本 PR 合并、main 回读和 QRSC receipt 生成完成后，回到 `aiant-core` 做 realization review 和
exactly-one following-host selection。不得在 review 前提前授权下游实现。

---

# 补充说明

当前 patch 中，这两个文件实现的是 **MMN 的 memory-writeback preview 最小宿主位**：它能生成一个“准备写回记忆的只读预览对象”，但不会真的写入记忆，也不会触发任何运行时执行。

核心定位可以概括为：

```text
把“未来可能写回什么记忆”表达出来
→ 保留来源、理由、证据与追踪信息
→ 明确所有执行权限仍为 False
→ 对任何试图夹带执行字段的输入 fail-closed
```

它是一个 **read-side、reference-only、preview-only seam**，不是 memory writer。

---

## 一、`src/mmn/contracts/memory_writeback_preview_v0.py` 实现了什么

### 1. 定义最小预览对象

文件中定义了不可变数据类：

```python
@dataclass(frozen=True)
class MemoryWritebackPreviewV0:
    preview_version: str
    preview_id: str
    source_memory_output_id: str
    preview_state: str
    reason_codes: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    memory_write_authorized: bool
    persistent_memory_mutation_authorized: bool
    runtime_authority_granted: bool
    trace: Mapping[str, object]
```

它表达的是一张“写回预览卡片”。

业务上相当于：

```text
来源记忆输出是谁
→ 为什么考虑写回
→ 有哪些证据
→ 当前预览编号是什么
→ 当前是否允许写入
→ 当前是否允许持久化修改
→ 当前是否拥有运行时权限
```

目前最后三个权限字段始终为：

```text
memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_granted=False
```

因此，该对象只能用于审阅、追踪和后续治理判断，不能执行写回。

---

### 2. 生成稳定的 preview ID

builder：

```python
def build_memory_writeback_preview_v0(
    *,
    preview_seed: str,
    source_memory_output_id: str,
    reason_codes: tuple[str, ...] | list[str] = (),
    evidence_refs: tuple[str, ...] | list[str] = (),
    material: Mapping[str, object] | None = None,
) -> MemoryWritebackPreviewV0:
```

会根据：

```python
preview_id = f"memory-writeback-preview::{preview_seed.strip()}"
```

生成稳定 ID。

例如：

```text
preview_seed=alpha
→ preview_id=memory-writeback-preview::alpha
```

这为后续审计、回链、去重和 receipt 提供了最小标识位。

当前它还不是完整的 canonical hash，也不是 record ID 体系，只是最小 preview ID seam。

---

### 3. 对理由与证据做最小规范化

函数：

```python
normalize_str_tuple_v0(...)
```

实现了：

```text
None
→ ()

单个字符串
→ 去除首尾空格后转成单元素 tuple

list / tuple
→ 去除空字符串
→ 去除重复项
→ 保持原有顺序
→ 输出 tuple

其他类型
→ ValueError
```

例如：

```python
reason_codes=("MEMORY_PREVIEW", "MEMORY_PREVIEW")
```

会归一化为：

```python
("MEMORY_PREVIEW",)
```

这项能力很小，但很重要：它让后续 audit、hash、比较、fixture 和 receipt 更稳定。

---

### 4. 保留理由与证据引用

当前对象支持：

```text
reason_codes
evidence_refs
```

例如：

```python
reason_codes=("MEMORY_PREVIEW",)
evidence_refs=("memory-preview::alpha", "trace::alpha")
```

业务意义是：

```text
为什么产生这张写回预览
→ reason_codes

它依据哪些上游对象或追踪记录
→ evidence_refs
```

它还没有引入复杂 evidence bundle，也没有计算 Credibility、Conflict 或 Freshness 分数；这里只建立最小引用位。

---

### 5. 构建只读 trace

builder 同时生成：

```python
trace = {
    "source_stage": SOURCE_STAGE_V0,
    "preview_id": preview_id,
    "source_memory_output_id": source_memory_output_id.strip(),
    "preview_state": PREVIEW_STATE_V0,
    "reason_codes": normalized_reason_codes,
    "evidence_refs": normalized_evidence_refs,
    "memory_write_authorized": False,
    "persistent_memory_mutation_authorized": False,
    "runtime_authority_granted": False,
}
```

这使 preview 自身具备最小审计链。

当前 trace 回答：

```text
从哪里来
→ source_memory_output_id

在哪个阶段生成
→ source_stage

当前是什么状态
→ reference_only_preview

依据是什么
→ reason_codes + evidence_refs

权限是否打开
→ 全部 False
```

---

### 6. 提供 payload 投影

函数：

```python
memory_writeback_preview_to_payload_v0(...)
```

将不可变对象投影为：

```python
dict[str, object]
```

这为后续：

```text
JSON 输出
fixture
日志
receipt
adapter
CLI preview
治理扫描
```

提供基础形态。

它仍然只是序列化投影，不是写入命令。

---

## 二、最关键的安全边界：fail-closed

文件中定义：

```python
FORBIDDEN_EXECUTION_FIELDS_V0
```

当前拒绝字段包括：

```text
memory_write_authorized
persistent_memory_mutation_authorized
runtime_authority_granted

route_decision
fetch_command
scheduler_apply
queue_mutation
worker_dispatch
execution_payload

provider_backend_call
model_call

shared_contract_expansion
dmf_bootstrap
```

builder 会检查：

```python
forbidden_present = sorted(
    FORBIDDEN_EXECUTION_FIELDS_V0.intersection(preview_material)
)

if forbidden_present:
    raise ValueError(...)
```

也就是说，任何调用方试图通过：

```python
material={...}
```

夹带执行意图、运行时权限、worker dispatch、DMF 或 shared-contract 扩展信息，构建都会立即失败。

例如：

```python
build_memory_writeback_preview_v0(
    preview_seed="gamma",
    source_memory_output_id="memory-preview::gamma",
    material={"memory_write_authorized": True},
)
```

不会生成对象，而是抛出：

```text
ValueError: forbidden execution-like fields
```

这正是当前阶段最重要的业务保护。

---

## 三、`tests/test_mmn_memory_writeback_preview_minimal_host_v0.py` 验证了什么

测试文件不是简单 smoke test，而是围绕最小业务边界建立了四类回归保护。

### 1. 验证 reference-only preview

测试：

```python
test_memory_writeback_preview_minimal_host_is_reference_only
```

确认：

```text
preview_version=memory_writeback_preview_v0
preview_id=memory-writeback-preview::alpha
source_memory_output_id=memory-preview::alpha
preview_state=reference_only_preview

reason_codes 去重
evidence_refs 保留

memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_granted=False
```

这证明对象可以表达预览，但没有获得执行权限。

---

### 2. 验证 payload 投影不会偷偷打开权限

测试：

```python
test_memory_writeback_preview_payload_retains_closed_authority
```

确认转换为 payload 后：

```text
memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_granted=False
```

trace 中也仍然保持相同的关闭状态。

这防止出现：

```text
对象层是 False
→ 但序列化层错误变成 True
```

---

### 3. 参数化验证所有禁止字段

测试：

```python
@pytest.mark.parametrize("field", sorted(FORBIDDEN_EXECUTION_FIELDS_V0))
def test_memory_writeback_preview_rejects_execution_like_fields(...)
```

会逐项验证全部 forbidden fields。

不是只抽查一个字段，而是对每个字段分别确认：

```text
material={field: True}
→ 必须 ValueError
```

这相当于最小治理扫描器。

---

### 4. 验证非法输入形态 fail-closed

测试：

```python
test_memory_writeback_preview_rejects_invalid_normalization_shape
```

使用：

```python
evidence_refs={"trace::delta"}
```

即 `set` 类型。

当前仅允许：

```text
string
list
tuple
None
```

因此必须拒绝 `set`：

```text
ValueError
```

这样可以避免不稳定顺序进入 hash、trace 或 receipt。

---

## 四、当前已经具备的最小业务价值

当前实现虽然很薄，但已经能承担 6 项真实工程职责。

| 能力                 | 当前是否具备 | 说明                          |
| ------------------ | -----: | --------------------------- |
| 表达“候选记忆写回预览”       |      是 | 生成结构化 preview 对象            |
| 回链上游 memory output |      是 | `source_memory_output_id`   |
| 携带最小理由             |      是 | `reason_codes`              |
| 携带最小证据引用           |      是 | `evidence_refs`             |
| 生成审计 trace         |      是 | `trace`                     |
| 阻止越权字段进入           |      是 | forbidden field fail-closed |
| 真实写入 memory        |      否 | 明确禁止                        |
| 修改持久化存储            |      否 | 明确禁止                        |
| 接入 worker          |      否 | 明确禁止                        |
| 接入 runtime loader  |      否 | 明确禁止                        |
| 跨仓 shared contract |      否 | 明确禁止                        |
| 接入 PANT intake     |      否 | 明确禁止                        |
| 接入 ZANT-LLM        |      否 | 明确禁止                        |
| 启动 DMF             |      否 | 明确禁止                        |

---

## 五、它在 AIant PDE 中的位置

当前链路可以理解为：

```text
上游 memory preview / memory output
        │
        ▼
MemoryWritebackPreviewV0
        │
        ├── reason_codes
        ├── evidence_refs
        ├── trace
        └── authority flags = False
```

它只是“把候选写回意图显式化”。

还没有进入：

```text
MemoryWritebackPreviewV0
        │
        ▼
policy review
        │
        ▼
admission
        │
        ▼
writeback request
        │
        ▼
worker
        │
        ▼
persistent mutation
```

这条后半段链路目前全部不存在或保持关闭。

---

## 六、当前代码刻意没有做什么

### 1. 没有真正写 memory

文件中没有：

```text
database write
file write
vector-store upsert
cache mutation
memory table insert
update
delete
commit
```

也没有任何 side effect。

---

### 2. 没有定义执行命令

没有：

```text
MemoryWriteCommand
WritebackExecutionPayload
WorkerDispatch
SchedulerApply
QueueMutation
```

这不是遗漏，而是当前边界要求。

---

### 3. 没有 adapter

目前仅有：

```text
contract / host shape
builder
payload projection
tests
```

还没有：

```text
memory_output → writeback_preview adapter
```

因此当前需要由显式调用方传入：

```python
preview_seed
source_memory_output_id
reason_codes
evidence_refs
```

---

### 4. 没有治理决策

当前不会判断：

```text
应该写回
不应该写回
延迟写回
拒绝写回
需要人工审阅
```

它只表达：

```text
这是一个 reference-only preview
```

---

## 七、今后扩展完善业务功能的正确方法

建议继续采用你长期使用的顺序：

```text
最小宿主位
→ adapter
→ governance
→ audit receipt
→ admission
→ request
→ execution boundary
→ 最后才考虑 worker 与持久化
```

不要直接在 `MemoryWritebackPreviewV0` 中把：

```python
memory_write_authorized=False
```

改成：

```python
memory_write_authorized=True
```

这会绕过治理层，破坏当前分层设计。

---

### 阶段 1：补 repo-local adapter

下一步最自然的是新增：

```text
src/mmn/adapters/memory_writeback_preview_adapter_v0.py
tests/test_memory_writeback_preview_adapter_v0.py
```

职责：

```text
读取既有 memory output
→ 提取 output ID
→ 提取 reasons
→ 提取 evidence refs
→ 调用 build_memory_writeback_preview_v0
→ 返回 preview
```

仍然禁止：

```text
真实 write
持久化 mutation
runtime authority
```

推荐输入输出：

```text
MemoryPreviewOutputV0
→ adapter
→ MemoryWritebackPreviewV0
```

---

### 阶段 2：增加 preview validation

新增：

```text
src/mmn/governance/memory_writeback_preview_validator_v0.py
```

校验：

```text
source_memory_output_id 是否存在
reason_codes 是否属于允许集合
evidence_refs 是否可回读
preview_id 是否稳定
trace 是否完整
权限字段是否全部 False
forbidden field 是否缺失
```

这一步仍然是 read-only。

---

### 阶段 3：增加 governance outcome

新增单独对象，不要污染 preview：

```text
MemoryWritebackPreviewReviewOutcomeV0
```

它可以表达：

```text
accept_for_further_review
reject
defer
needs_more_evidence
narrow_scope
```

注意：

```text
accept_for_further_review
≠ authorize_write
```

这里仍然不能产生真实写权限。

---

### 阶段 4：增加 canonical hash 与 audit receipt

为 preview 引入稳定哈希：

```text
canonical_hash
record_id
source_record_id
created_at
schema_version
```

建议新增独立 receipt：

```text
MemoryWritebackPreviewReceiptV0
```

用途：

```text
去重
幂等
main readback
跨阶段 handoff
证据链
audit
```

这一阶段可以与现有 ORSC / QRSC receipt workflow 对齐。

---

### 阶段 5：增加 admission 对象

通过治理审查后，再新增：

```text
MemoryWritebackAdmissionPreviewV0
```

它只能表达：

```text
candidate admitted for request construction
```

仍不能直接写入。

建议显式区分：

```text
preview
review outcome
admission preview
writeback request
execution authorization
execution result
```

不要把所有状态塞进一个 dataclass。

---

### 阶段 6：增加 writeback request，但仍保持 non-executing

新增：

```text
MemoryWritebackRequestV0
```

职责：

```text
表达未来可能执行的写回请求
```

但默认：

```text
execution_authorized=False
persistent_mutation_authorized=False
```

此时可以增加：

```text
target_namespace
memory_key
candidate_payload_ref
idempotency_key
expected_version
conflict_policy
expiry
```

仍然不能调用数据库。

---

### 阶段 7：增加 guarded executor seam

只有前面都稳定后，才新增：

```text
MemoryWritebackExecutorPortV0
```

建议先做：

```text
dry-run executor
non-executing stub
read-side receipt emitter
```

而不是立即接真实存储。

执行入口必须要求显式 capability：

```text
execution_authority_token
admission_receipt
canonical_hash
idempotency_key
expected_version
```

缺任意一个都 fail-closed。

---

### 阶段 8：最后才接持久化 worker

真正写 memory 时，应独立建设：

```text
worker
transaction boundary
idempotency
conflict detection
rollback
audit trail
retry policy
dead-letter
replay
```

并且必须区分：

```text
preview created
request constructed
request admitted
execution authorized
write attempted
write committed
write rejected
write rolled back
```

---

## 八、建议的对象演进图

```text
MemoryOutputV0
      │
      ▼
MemoryWritebackPreviewAdapterV0
      │
      ▼
MemoryWritebackPreviewV0
      │
      ▼
MemoryWritebackPreviewValidatorV0
      │
      ▼
MemoryWritebackPreviewReviewOutcomeV0
      │
      ▼
MemoryWritebackAdmissionPreviewV0
      │
      ▼
MemoryWritebackRequestV0
      │
      ▼
GuardedMemoryWritebackExecutorPortV0
      │
      ▼
DryRun / NonExecuting Stub
      │
      ▼
Future Persistent Worker
```

当前 patch 只落地到：

```text
MemoryWritebackPreviewV0
```

---

## 九、版本演进建议

不要直接修改 V0 的语义。未来扩展应新增版本：

```text
MemoryWritebackPreviewV0
→ 保持稳定、兼容、只读

MemoryWritebackPreviewV1
→ 增加 canonical hash、record ID、namespace 等字段
```

并保留：

```text
V0 fixture
V0 regression
V0 payload projection
V0 backward compatibility
V0 forbidden-field tests
```

推荐规则：

```text
新增字段
→ 优先新版本

修改字段语义
→ 必须新版本

打开执行权限
→ 必须新对象、新 gate、新 receipt
```

---

## 十、后续测试应如何扩展

当前测试主要保护 shape 与关闭边界。今后可以按层增加：

### Adapter tests

```text
memory output → preview
缺少 source ID → fail
非法 reasons → fail
重复 evidence refs → dedupe
```

### Governance tests

```text
证据不足 → defer
来源不可回读 → reject
authority field 非 False → reject
```

### Hash tests

```text
相同输入 → 相同 canonical hash
不同 evidence → 不同 hash
输入顺序规范化后 → hash 稳定
```

### Request tests

```text
preview 不可直接执行
未 admission 不可构造 executable request
缺少 idempotency key → reject
```

### Executor tests

```text
默认 dry-run
无 authority token → reject
重复 request → idempotent skip
版本冲突 → fail-closed
```

---

## 十一、当前最准确的状态摘要

```text
IMPLEMENTED:
- repo-local memory-writeback preview host
- immutable preview object
- deterministic preview ID
- reason-code normalization
- evidence-reference normalization
- audit trace
- payload projection
- forbidden execution-field rejection
- closed authority regression tests

NOT IMPLEMENTED:
- memory-output adapter
- governance review
- admission
- canonical hash
- writeback request
- worker
- runtime loader
- scheduler
- queue
- persistent memory mutation
- shared-contract expansion
- DMF
- PANT runtime-facing intake
- ZANT-LLM
```

当前实现是一个很合适的 **最小宿主位**：业务语义已经可表达，证据链已经可追踪，越权输入会被拒绝，但系统仍然没有任何真实写入能力。
