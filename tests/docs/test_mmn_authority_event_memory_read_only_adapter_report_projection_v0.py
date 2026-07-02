from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

SRC_PATH = (
    ROOT / "src/aiant_mmn/" / "mmn_authority_event_memory_read_only_adapter_report_projection_v0.py"
)
DOC_PATH = (
    ROOT
    / "docs/verification/"
    / "MMN_AUTHORITY_EVENT_MEMORY_READ_ONLY_ADAPTER_REPORT_PROJECTION_V0.md"
)
JSON_PATH = (
    ROOT
    / "docs/verification/"
    / "mmn_authority_event_memory_read_only_adapter_report_projection_v0.json"
)
FIXTURE_PATH = (
    ROOT
    / "tests/fixtures/mmn_authority_event_memory/"
    / "read_only_adapter_report_projection_v0.json"
)

DOCUMENT_NAME = "MMN_AUTHORITY_EVENT_MEMORY_READ_ONLY_ADAPTER_REPORT_PROJECTION_V0"
PROJECTION_KIND = "mmn_authority_event_memory_read_only_adapter_report_projection_v0"
GOLDEN_SHA = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"


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


def test_mmn_aem_read_only_adapter_report_projection_doc_exists() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_fragments = [
        "MMN Authority Event Memory Read-Only Adapter Report Projection V0",
        "read-only adapter report projection = non-authorizing summary",
        "read-only validation report != memory write authority",
        "report projection != runtime authorization",
        "Accepted contract surface is not downstream runtime authorization.",
        "Boolean authority fields are derived summaries, not authority sources.",
    ]

    for fragment in expected_fragments:
        assert fragment in text


def test_mmn_aem_read_only_adapter_report_projection_metadata() -> None:
    data = _read_json(JSON_PATH)

    assert data["document"] == DOCUMENT_NAME
    assert data["projection_kind"] == PROJECTION_KIND
    assert data["repo"] == "aiant-mmn"
    assert data["source_projection"] == str(SRC_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["fixture"] == str(FIXTURE_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["golden_fixture_canonical_sha256"] == GOLDEN_SHA
    assert data["projection_ready"] is True
    assert data["production_adapter_adoption_authorized"] is False
    assert data["report_projection_is_memory_write_authority"] is False
    assert data["report_projection_is_runtime_authorization"] is False
    assert data["read_only_adapter_report_projection_is_downstream_runtime_authorization"] is False


def test_mmn_aem_read_only_adapter_report_projection_authority_principles() -> None:
    data = _read_json(JSON_PATH)
    principles = cast(dict[str, object], data["authority_envelope_principles"])

    assert (
        principles["boolean_authority_fields_are_derived_summaries_not_authority_sources"] is True
    )
    assert principles["read_only_validation_report_is_not_memory_write_authority"] is True
    assert principles["report_projection_is_not_runtime_authorization"] is True
    assert principles["projection_preserves_fail_closed_reasons"] is True
    assert principles["default_on_missing_evidence"] == "false_fail_closed"


def test_mmn_aem_read_only_adapter_report_projection_valid_case() -> None:
    module = _load_projection()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])

    case = cases[0]
    projection = module.project_mmn_authority_event_memory_read_only_adapter_report_v0(
        case["source_report"]
    )

    expected = cast(dict[str, Any], case["expected_projection"])
    assert projection.projection_kind == PROJECTION_KIND
    assert projection.projection_decision == expected["projection_decision"]
    assert projection.projection_action == expected["projection_action"]
    assert projection.projected_status == expected["projected_status"]
    assert projection.fail_closed is False
    assert projection.fail_closed_reasons == ()
    assert projection.report_projection_is_memory_write_authority is False
    assert projection.report_projection_is_runtime_authorization is False
    assert projection.allowed_to_write_memory is False
    assert projection.allowed_to_execute is False
    assert projection.memory_write_authority_granted is False
    assert projection.drl_execution_authority_granted is False
    assert projection.trading_signal_authorized is False
    assert projection.future_live_execution_authorized is False


def test_mmn_aem_read_only_adapter_report_projection_fail_closed_cases() -> None:
    module = _load_projection()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])

    for case in cases[1:]:
        expected = cast(dict[str, Any], case["expected_projection"])
        projection = module.project_mmn_authority_event_memory_read_only_adapter_report_v0(
            case["source_report"]
        )

        assert projection.projection_decision == expected["projection_decision"]
        assert projection.projection_action == expected["projection_action"]
        assert projection.fail_closed is expected["fail_closed"]
        assert projection.fail_closed is True
        assert expected["required_reason"] in projection.fail_closed_reasons
        assert projection.allowed_to_write_memory is False
        assert projection.allowed_to_execute is False
        assert projection.memory_write_authority_granted is False
        assert projection.future_live_execution_authorized is False


def test_mmn_aem_read_only_adapter_report_projection_preserves_reasons() -> None:
    module = _load_projection()

    projection = module.project_mmn_authority_event_memory_read_only_adapter_report_v0(
        {
            "report_kind": "mmn_authority_event_memory_read_only_validation_report_v0",
            "adapter_mode": "validator_consumer_read_only",
            "allowed_to_write_memory": False,
            "allowed_to_execute": False,
            "fail_closed": True,
            "fail_closed_reasons": [
                "non_empty_missing_evidence",
                "non_empty_blocking_conditions",
            ],
        }
    )

    assert projection.fail_closed is True
    assert "non_empty_missing_evidence" in projection.fail_closed_reasons
    assert "non_empty_blocking_conditions" in projection.fail_closed_reasons


def test_mmn_aem_read_only_adapter_report_projection_non_authorizations() -> None:
    data = _read_json(JSON_PATH)
    non_auth = cast(dict[str, bool], data["explicit_non_authorizations"])

    expected = {
        "report_projection_is_memory_write_authority",
        "report_projection_is_runtime_authorization",
        "production_adapter_adoption_authorized",
        "downstream_runtime_consumption_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "memory_writeback_request_authorized",
        "memory_writeback_record_authorized",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
        "runtime_canonicalizer_created",
        "production_runtime_canonical_hash_created",
    }
    assert set(non_auth) == expected
    for key in expected:
        assert non_auth[key] is False


def test_mmn_aem_read_only_adapter_report_projection_followups_are_ordered() -> None:
    data = _read_json(JSON_PATH)

    assert data["recommended_followup_prs"] == [
        "core: add MMN authority event memory topology gate check-path preview v0",
        "governance: add MMN authority event memory scanner check-path denied fixtures v0",
        "mmn: add MMN authority event memory read-only adapter report projection fixtures v1",
    ]
