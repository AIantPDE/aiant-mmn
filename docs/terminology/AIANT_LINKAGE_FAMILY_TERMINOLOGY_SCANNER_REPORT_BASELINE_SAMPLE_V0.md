# AIANT Linkage-family Terminology Scanner Report Baseline Sample V0

Status: draft sample report format  
Scope: AIANT terminology scanner preparation only  
Boundary: static sample only; non-executing; non-authorizing; no scanner runtime  
Sentinel: `AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_REPORT_BASELINE_SAMPLE_V0_READY`

## 1. Purpose / 目的

This document defines a static baseline sample report format for future AIANT
linkage-family terminology scanner outputs.

本文档定义 AIANT 链路类术语扫描器未来输出报告的静态样例格式。
它不是扫描器实现，不读取真实仓库文件，不遍历文件系统，不接入 CI，不阻断 PR，
也不执行自动替换。

The sample report is intended to make future report-only scanner output reviewable
before any scanner engine, CLI, CI policy, suppression format, or cross-repo rollout
is implemented.

## 2. Upstream references / 上游依据

This sample format is downstream of the following terminology preparation assets:

- `AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0`
- `AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0`
- `AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_PREPARATION_REPORT_ONLY_RULES_V0`

The current document does not activate any of those assets as enforcement policy.
It only shows how a future report-only scanner result may be shaped.

## 3. Non-goals / 非目标

This baseline sample does not provide:

- scanner CLI
- scanner engine
- repository traversal
- text matching implementation
- rule evaluator
- suppression format
- baseline diff engine
- CI gating
- blocking mode
- automatic replacement
- formal terminology registry activation
- cross-repo rollout execution

Therefore, every finding in this sample is illustrative and synthetic.

## 4. Report status / 报告状态

```text
report_id: AIANT_LINKAGE_FAMILY_TERMINOLOGY_REPORT_BASELINE_SAMPLE_V0
report_kind: static_sample
scanner_mode: report_only_sample
execution_state: non_executing
blocking_state: non_blocking
source_scope: synthetic_examples_only
runtime_authority: none
```

## 5. Sample report schema / 样例报告结构

A future report-only scanner may emit the following top-level shape:

```json
{
  "report_id": "AIANT_LINKAGE_FAMILY_TERMINOLOGY_REPORT_BASELINE_SAMPLE_V0",
  "report_kind": "static_sample",
  "scanner_mode": "report_only_sample",
  "execution_state": "non_executing",
  "blocking_state": "non_blocking",
  "source_scope": "synthetic_examples_only",
  "summary": {
    "total_findings": 5,
    "blocking_findings": 0,
    "rules_observed": [
      "RULE-LINKAGE-001",
      "RULE-LINKAGE-002",
      "RULE-LINKAGE-003",
      "RULE-LINKAGE-009",
      "RULE-LINKAGE-011"
    ]
  },
  "findings": []
}
```

The `findings` array is intentionally empty in the schema fragment above. The next
section gives synthetic sample findings.

## 6. Synthetic sample findings / 合成样例发现项

The following findings are not produced by a scanner. They are manually authored
sample rows used to stabilize the expected report format.

### Finding 1: generic Chinese linkage without English anchor

```text
finding_id: SAMPLE-LINKAGE-001
rule_id: RULE-LINKAGE-001
rule_name: generic_zh_linkage_without_english_anchor
severity: info
repo: aiant-mmn
file_path: docs/example/SYNTHETIC_ONLY.md
line: 12
matched_text: 链路
suggested_anchor: chain | lane | trace | path | route | lineage | bridge | seam | handoff | loop
recommendation: Add a precise English anchor before using 链路 as a generic Chinese term.
blocking: false
sample_only: true
```

### Finding 2: chain / lane / trace confusion

```text
finding_id: SAMPLE-LINKAGE-002
rule_id: RULE-LINKAGE-002
rule_name: chain_lane_trace_confusion
severity: warning
repo: aiant-mmn
file_path: docs/example/SYNTHETIC_ONLY.md
line: 24
matched_text: AEM field feedback chain
expected_term: lane, if the text describes an engineering work route
recommendation: Use chain only for ordered methodology; use lane for work-route classification; use trace for historical audit.
blocking: false
sample_only: true
```

### Finding 3: path / route confusion

```text
finding_id: SAMPLE-LINKAGE-003
rule_id: RULE-LINKAGE-003
rule_name: path_route_confusion
severity: warning
repo: aiant-pant
file_path: docs/example/SYNTHETIC_ONLY.md
line: 31
matched_text: runtime path admission
expected_term: route admission, if admission / preview / denial is being discussed
recommendation: Use path for reachability and route for admitted / denied / previewed processing choices.
blocking: false
sample_only: true
```

### Finding 4: graph / edge / link / chain confusion

```text
finding_id: SAMPLE-LINKAGE-004
rule_id: RULE-LINKAGE-009
rule_name: graph_edge_link_chain_confusion
severity: warning
repo: aiant-gant
file_path: docs/example/SYNTHETIC_ONLY.md
line: 44
matched_text: graph chain between two nodes
expected_term: edge, if this means one graph edge; link, if this means an object relation
recommendation: Do not collapse graph edge, object link, and ordered chain into the same Chinese 链路 wording.
blocking: false
sample_only: true
```

### Finding 5: DRL execution-semantics boundary

```text
finding_id: SAMPLE-LINKAGE-005
rule_id: RULE-LINKAGE-011
rule_name: drl_execution_semantics_boundary
severity: warning
repo: aiant-drl
file_path: docs/example/SYNTHETIC_ONLY.md
line: 58
matched_text: policy execution route
expected_term: policy candidate review chain or policy candidate observation surface
recommendation: Keep aiant-drl as future downstream preview / candidate surface only; avoid execution-route wording.
blocking: false
sample_only: true
```

## 7. Baseline summary contract / 基线摘要约定

A future report-only scanner baseline should be reviewable through a summary block:

```text
total_findings: number of report-only findings
blocking_findings: always 0 until governance explicitly approves blocking mode
rules_observed: rule identifiers that appeared in the report
repos_observed: repositories represented in the report
synthetic_sample: true for this V0 baseline sample
```

For this V0 sample:

```text
total_findings: 5
blocking_findings: 0
synthetic_sample: true
activation_ready: false
```

## 8. Report item minimum fields / 报告项最小字段

Every future report item should carry at least:

```text
finding_id
rule_id
rule_name
severity
repo
file_path
line
matched_text
expected_term
recommendation
blocking
sample_only
```

Optional fields may include:

```text
column
context_before
context_after
suggested_anchor
risk_note
suppression_hint
owner_review_status
```

## 9. Boundary assertions / 边界断言

This baseline sample explicitly asserts:

```text
no_scanner_cli: true
no_scanner_engine: true
no_file_traversal: true
no_match_engine: true
no_ci_gating: true
no_blocking_mode: true
no_auto_replacement: true
no_suppression_format: true
no_runtime_authority: true
synthetic_examples_only: true
```

## 10. Promotion conditions / 后续晋级条件

A future scanner implementation is not ready until all of the following exist:

- governance approval for report-only scanner scope
- explicit scanner CLI design
- file traversal policy
- match engine design
- false-positive handling strategy
- suppression format proposal
- baseline report generation command
- CI policy decision for report-only mode
- cross-repo rollout plan

Blocking mode requires a separate governance decision and is out of scope for this V0 sample.

## 11. Sentinel

```text
AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_REPORT_BASELINE_SAMPLE_V0_READY
```
