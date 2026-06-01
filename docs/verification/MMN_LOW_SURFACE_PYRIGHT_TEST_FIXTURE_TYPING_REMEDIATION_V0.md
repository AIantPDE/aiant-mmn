# MMN Low-Surface Pyright Test Fixture Typing Remediation V0

- 阶段标记：`STAGE-QGR-11`
- Batch：`QGR-BATCH-02`
- Route：`MMN-PYRIGHT-01`
- 仓库：`aiant-mmn`
- PR 标题：`test/fix: harden mmn low-surface pyright test fixture typing v0`

## 1. 来源

```text
batch_id=QGR-BATCH-02
route_id=MMN-PYRIGHT-01
baseline_errors=7
affected_file_count=2
change_surface=tests_only
```

## 2. 子项 A：accepted semantic feature reference loader typing

目标测试的 JSON loader 原先声明：

```python
dict[str, object]
```

但测试需要访问嵌套 fixture：

```python
reference["authority_flags"][flag]
```

当嵌套值仍被推导为 `object` 时，pyright 会报告：

```text
reportIndexIssue
"__getitem__" method not defined on type "object"
```

最小修复是在测试文件中增加 test-local JSON mapping alias，并将
`json.loads()` 结果收窄为该 alias：

```python
JsonObject = dict[str, Any]


def load_reference() -> JsonObject:
    return cast(JsonObject, json.loads(...))
```

## 3. 子项 B：memory output assertion compatibility cleanup

`MemoryPreviewOutputV0` 已稳定使用：

```python
output.memory_output_id
```

旧测试中仍保留一个过时 fallback：

```python
output.memory_id if hasattr(output, "memory_id") else output.memory_output_id
```

pyright 会对并不存在的 `memory_id` 属性报告：

```text
reportAttributeAccessIssue
```

最小修复是直接断言：

```python
adapted["memory_output_id"] == output.memory_output_id
```

不得向 `MemoryPreviewOutputV0` schema 新增 `memory_id` 字段。

## 4. 边界

```text
tests_only=True
test_fixture_loader_typing_normalized=True
obsolete_memory_id_fallback_removed=True
production_code_changed=False
contract_schema_changed=False
memory_preview_output_schema_changed=False
runtime_loader_changed=False
memory_write_authorized=False
persistent_memory_mutation_authorized=False
execution_payload_enabled=False
runtime_authority_changed=False
```

## 5. 防误读

```text
test fixture typing normalization
≠ contract schema expansion
≠ runtime JSON loader change

obsolete memory_id fallback removal
≠ MemoryPreviewOutputV0 schema expansion
≠ memory-write authorization
≠ persistent mutation authorization
≠ execution payload enablement
≠ runtime authority grant
```
