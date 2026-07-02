from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

SRC_PATH = (
    ROOT / "src/aiant_mmn/" / "mmn_authority_event_memory_read_only_adapter_report_projection_v0.py"
)
DOC_PATH = (
    ROOT
    / "docs/verification/"
    / "MMN_AUTHORITY_EVENT_MEMORY_READ_ONLY_ADAPTER_REPORT_PROJECTION_FIXTURES_V1.md"
)
JSON_PATH = (
    ROOT
    / "docs/verification/"
    / "mmn_authority_event_memory_read_only_adapter_report_projection_fixtures_v1.json"
)
FIXTURE_PATH = (
    ROOT
    / "tests/fixtures/mmn_authority_event_memory/"
    / "read_only_adapter_report_projection_fixtures_v1.json"
)

DOCUMENT_NAME = "MMN_AUTHORITY_EVENT_MEMORY_READ_ONLY_ADAPTER_REPORT_PROJECTION_FIXTURES_V1"
FIXTURES_KIND = "mmn_authority_event_memory_read_only_adapter_report_projection_fixtures_v1"
GOLDEN_SHA = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"


@dataclass(frozen=True)
class SourceReportObject:
    report_kind: str
    adapter_mode: str
    allowed_to_write_memory: bool
    allowed_to_execute: bool
    fail_closed: bool
    fail_closed_reasons: list[str]


class ProjectionModuleProtocol:
    project_mmn_authority_event_memory_read_only_adapter_report_v0: Any


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _load_projection() -> ProjectionModuleProtocol:
    spec = importlib.util.spec_from_file_location(
        "mmn_aem_read_only_adapter_report_projection_v0",
        SRC_PATH,
    )
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return cast(ProjectionModuleProtocol, module)


def _object_from_payload(payload: dict[str, Any]) -> SourceReportObject:
    return SourceReportObject(
        report_kind=str(payload["report_kind"]),
        adapter_mode=str(payload["adapter_mode"]),
        allowed_to_write_memory=bool(payload["allowed_to_write_memory"]),
        allowed_to_execute=bool(payload["allowed_to_execute"]),
        fail_closed=bool(payload["fail_closed"]),
        fail_closed_reasons=list(cast(list[str], payload["fail_closed_reasons"])),
    )


def test_mmn_aem_projection_fixtures_v1_doc_exists() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_fragments = [
        "MMN Authority Event Memory Read-Only Adapter Report Projection Fixtures V1",
        "projection fixtures v1 = regression inputs",
        "projection fixtures v1 != memory write authority",
        "projection fixtures v1 != runtime authorization",
        "fixtures are not authority sources",
        "Boolean authority fields are derived summaries, not authority sources.",
    ]

    for fragment in expected_fragments:
        assert fragment in text


def test_mmn_aem_projection_fixtures_v1_metadata() -> None:
    data = _read_json(JSON_PATH)

    assert data["document"] == DOCUMENT_NAME
    assert data["fixtures_kind"] == FIXTURES_KIND
    assert data["repo"] == "aiant-mmn"
    assert data["source_projection"] == str(SRC_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["fixture"] == str(FIXTURE_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["docs_test_only"] is True
    assert data["projection_source_modified"] is False
    assert data["golden_fixture_canonical_sha256"] == GOLDEN_SHA
    assert data["fixtures_v1_ready"] is True
    assert data["report_projection_fixtures_v1_is_memory_write_authority"] is False
    assert data["report_projection_fixtures_v1_is_runtime_authorization"] is False


def test_mmn_aem_projection_fixtures_v1_authority_principles() -> None:
    data = _read_json(JSON_PATH)
    principles = cast(dict[str, object], data["authority_envelope_principles"])

    assert (
        principles["boolean_authority_fields_are_derived_summaries_not_authority_sources"] is True
    )
    assert principles["read_only_validation_report_is_not_memory_write_authority"] is True
    assert principles["report_projection_is_not_runtime_authorization"] is True
    assert principles["fixtures_are_regression_inputs_not_authority_sources"] is True
    assert principles["default_on_missing_evidence"] == "false_fail_closed"


def test_mmn_aem_projection_fixtures_v1_mapping_cases() -> None:
    module = _load_projection()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])

    mapping_cases = [case for case in cases if "source_report" in case]

    assert len(mapping_cases) == 5

    for case in mapping_cases:
        expected = cast(dict[str, Any], case["expected_projection"])
        projection = module.project_mmn_authority_event_memory_read_only_adapter_report_v0(
            case["source_report"]
        )

        assert projection.projection_decision == expected["projection_decision"]
        assert projection.projection_action == expected["projection_action"]
        assert projection.projected_status == expected["projected_status"]
        assert projection.fail_closed is expected["fail_closed"]
        assert projection.allowed_to_write_memory is False
        assert projection.allowed_to_execute is False
        assert projection.memory_write_authority_granted is False
        assert projection.future_live_execution_authorized is False

        if "required_reason" in expected:
            assert expected["required_reason"] in projection.fail_closed_reasons

        if "fail_closed_reasons" in expected:
            assert list(projection.fail_closed_reasons) == expected["fail_closed_reasons"]


def test_mmn_aem_projection_fixtures_v1_attribute_object_cases() -> None:
    module = _load_projection()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])

    object_cases = [case for case in cases if "source_report_object" in case]

    assert len(object_cases) == 2

    for case in object_cases:
        expected = cast(dict[str, Any], case["expected_projection"])
        source = _object_from_payload(cast(dict[str, Any], case["source_report_object"]))
        projection = module.project_mmn_authority_event_memory_read_only_adapter_report_v0(source)

        assert projection.projection_decision == expected["projection_decision"]
        assert projection.projection_action == expected["projection_action"]
        assert projection.projected_status == expected["projected_status"]
        assert projection.fail_closed is expected["fail_closed"]
        assert projection.allowed_to_write_memory is False
        assert projection.allowed_to_execute is False
        assert projection.memory_write_authority_granted is False

        for reason in expected.get("required_reasons", []):
            assert reason in projection.fail_closed_reasons


def test_mmn_aem_projection_fixtures_v1_non_authorizations() -> None:
    data = _read_json(JSON_PATH)
    non_auth = cast(dict[str, bool], data["explicit_non_authorizations"])

    expected = {
        "fixtures_v1_is_memory_write_authority",
        "fixtures_v1_is_runtime_authorization",
        "fixtures_v1_is_production_adapter_adoption",
        "downstream_runtime_consumption_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "memory_writeback_request_authorized",
        "memory_writeback_record_authorized",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    }
    assert set(non_auth) == expected
    for key in expected:
        assert non_auth[key] is False


def test_mmn_aem_projection_fixtures_v1_followups_are_ordered() -> None:
    data = _read_json(JSON_PATH)

    assert data["recommended_followup_prs"] == [
        (
            "contracts/governance/mmn: draft MMN authority event memory "
            "write authority grant envelope plan v0"
        ),
        ("governance: add MMN authority event memory scanner check-path preview CLI skeleton v0"),
        ("core: add MMN authority event memory topology gate denied fixtures v1"),
    ]
