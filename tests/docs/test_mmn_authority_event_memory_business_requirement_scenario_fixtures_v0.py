from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

DOC_MD = (
    ROOT
    / "docs"
    / "verification"
    / "MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_REQUIREMENT_SCENARIO_FIXTURES_V0.md"
)
DOC_JSON = (
    ROOT
    / "docs"
    / "verification"
    / "mmn_authority_event_memory_business_requirement_scenario_fixtures_v0.json"
)
FIXTURE_JSON = (
    ROOT
    / "tests"
    / "fixtures"
    / "mmn_authority_event_memory"
    / "business_requirement_scenario_fixtures_v0.json"
)


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return cast(dict[str, Any], payload)


def _dict(value: Any) -> dict[str, Any]:
    assert isinstance(value, dict)
    return cast(dict[str, Any], value)


def _list(value: Any) -> list[Any]:
    assert isinstance(value, list)
    return cast(list[Any], value)


def test_business_requirement_scenario_fixture_docs_exist() -> None:
    assert DOC_MD.exists()
    assert DOC_JSON.exists()
    assert FIXTURE_JSON.exists()


def test_business_requirement_scenario_fixture_payloads_match() -> None:
    assert _load_json(DOC_JSON) == _load_json(FIXTURE_JSON)


def test_business_requirement_scenarios_are_non_executing() -> None:
    payload = _load_json(FIXTURE_JSON)

    assert payload["asset_kind"] == ("non_executing_business_requirement_scenario_fixtures")
    assert payload["scenario_count"] == len(_list(payload["scenarios"]))

    required_non_auth = set(_list(payload["required_non_authorization_keys"]))
    assert "memory_write_authority_granted" in required_non_auth
    assert "runtime_shadow_mode_authorized" in required_non_auth
    assert "future_live_execution_authorized" in required_non_auth

    for raw_scenario in _list(payload["scenarios"]):
        scenario = _dict(raw_scenario)
        assert scenario["scenario_kind"] == ("business_requirement_scenario_fixture")

        future_need = _dict(scenario["future_candidate_need"])
        assert future_need["requires_runtime"] is False
        assert future_need["requires_write"] is False
        assert future_need["requires_writeback_request"] is False

        expected = _dict(scenario["expected_current_result"])
        assert expected["fail_closed"] is True
        assert expected["action"] in {
            "report_requirements_only",
            "deny_fail_closed",
        }

        non_auth = _dict(scenario["explicit_non_authorizations"])
        assert set(non_auth) == required_non_auth
        assert all(value is False for value in non_auth.values())


def test_field_registry_feedback_is_explicit_and_non_authorizing() -> None:
    payload = _load_json(FIXTURE_JSON)
    required_feedback_keys = set(_list(payload["field_feedback_categories"]))

    for raw_scenario in _list(payload["scenarios"]):
        scenario = _dict(raw_scenario)
        feedback = _dict(scenario["field_registry_feedback"])

        assert set(feedback) == required_feedback_keys
        assert _list(scenario["required_fields"])

        derived_fields = _list(feedback["derived_summary_fields"])
        forbidden_interpretations = _list(feedback["forbidden_authority_interpretations"])

        assert derived_fields
        assert forbidden_interpretations


def test_docs_state_fixture_boundaries() -> None:
    text = DOC_MD.read_text(encoding="utf-8")

    assert "业务语义是真实的。" in text
    assert "执行路径为零。" in text
    assert "场景样例不是 Runtime Shadow Mode" in text
    assert "这些反馈不是正式 field registry。" in text
    assert "memory write" in text
    assert "future live execution" in text
