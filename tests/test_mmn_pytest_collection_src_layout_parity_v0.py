from __future__ import annotations

import importlib
import tomllib
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / "src"
PYPROJECT = ROOT / "pyproject.toml"
JsonObject = dict[str, Any]


def load_pyproject() -> JsonObject:
    return cast(JsonObject, tomllib.loads(PYPROJECT.read_text(encoding="utf-8")))


def test_mmn_pytest_src_layout_pythonpath_locked() -> None:
    pyproject = load_pyproject()
    pytest_options = pyproject["tool"]["pytest"]["ini_options"]
    assert pytest_options["testpaths"] == ["tests"]
    assert pytest_options["pythonpath"] == ["src"]
    assert pytest_options["addopts"] == "-q"


def test_mmn_adapters_resolve_from_src_layout() -> None:
    module = importlib.import_module("mmn.adapters.route_preview_memory_adapter_v0")
    module_file = module.__file__
    assert module_file is not None
    module_path = Path(module_file).resolve()
    assert SRC_ROOT.resolve() in module_path.parents
