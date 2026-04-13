from __future__ import annotations

import json
from pathlib import Path
from typing import TypeAlias

from mmn.adapters import FORBIDDEN_EXECUTION_FIELDS_V0
from mmn.contracts.memory_preview_output_v0 import (
    memory_preview_output_to_payload_v0,
)
from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0

JsonScalar: TypeAlias = str | int | float | bool | None
JsonValue: TypeAlias = JsonScalar | list["JsonValue"] | dict[str, "JsonValue"]

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _load_fixture(*parts: str) -> JsonValue:
    path = FIXTURES_DIR.joinpath(*parts)
    data = json.loads(path.read_text(encoding="utf-8"))
    return _canonicalize(data)


def _canonicalize(value: object) -> JsonValue:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, tuple):
        return [_canonicalize(item) for item in value]

    if isinstance(value, list):
        return [_canonicalize(item) for item in value]

    if isinstance(value, dict):
        canonical: dict[str, JsonValue] = {}
        for key, item in value.items():
            canonical[str(key)] = _canonicalize(item)
        return canonical

    msg = f"Unsupported canonicalize value type: {type(value)!r}"
    raise TypeError(msg)


def test_memory_preview_output_golden_v0_default() -> None:
    provider = MemoryStubProviderV0()

    output = provider.generate(
        output_seed="alpha",
        richer_memory=False,
    )
    payload = memory_preview_output_to_payload_v0(output)

    expected = _load_fixture(
        "memory_preview_output_v0",
        "memory_preview_default.json",
    )

    assert _canonicalize(payload) == expected

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_memory_preview_output_golden_v0_richer() -> None:
    provider = MemoryStubProviderV0()

    output = provider.generate(
        output_seed="alpha-richer",
        richer_memory=True,
    )
    payload = memory_preview_output_to_payload_v0(output)

    expected = _load_fixture(
        "memory_preview_output_v0",
        "memory_preview_richer.json",
    )

    assert _canonicalize(payload) == expected

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload
