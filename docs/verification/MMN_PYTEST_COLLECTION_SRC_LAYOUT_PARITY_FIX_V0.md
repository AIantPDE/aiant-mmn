# MMN Pytest Collection Src-Layout Parity Fix V0

- 阶段标记：`STAGE-QGR-11`
- Batch：`QGR-BATCH-02`
- Route：`MMN-PYRIGHT-01`
- 仓库：`aiant-mmn`
- 变更面：pytest test infrastructure only

## 1. 发现方式

在完成 MMN 的 tests-only pyright 修复后，targeted pytest collection 暴露：

```text
ModuleNotFoundError: No module named 'mmn.adapters'
```

只读诊断确认：

```text
default resolution
→ mmn namespace path = <repo-root>\mmn
→ mmn.adapters missing

PYTHONPATH=<repo-root>
→ mmn.adapters missing

PYTHONPATH=<repo-root>\src
→ mmn.__file__ = <repo-root>\src\mmn\__init__.py
→ mmn.adapters.route_preview_memory_adapter_v0 import passed
```

## 2. 根因

仓库同时存在：

```text
mmn/
→ references fixture namespace at repository root

src/mmn/
→ actual Python package
→ adapters / contracts / providers / recall
```

pytest 从仓库根目录启动时，如果没有显式 pytest `pythonpath`，会先解析到
根目录 `mmn/` namespace，导致 `src/mmn/adapters` 不可见。

## 3. 最小修复

只补齐 pytest 配置：

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = "-q"
```

并新增回归测试：

```text
tests/test_mmn_pytest_collection_src_layout_parity_v0.py
```

## 4. 边界

```text
pytest_test_configuration_changed=True
test_import_parity_regression_added=True
production_code_changed=False
runtime_package_loader_changed=False
contract_schema_changed=False
memory_preview_output_schema_changed=False
memory_write_authorized=False
persistent_memory_mutation_authorized=False
runtime_authority_changed=False
```

## 5. 防误读

```text
pytest src-layout parity fix
≠ editable install requirement
≠ arbitrary cwd import enablement
≠ runtime package loader change
≠ production package relocation
≠ runtime authority grant
```
