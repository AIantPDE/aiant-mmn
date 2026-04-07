## 概要

请简要说明本 PR 的目标、范围与当前阶段定位。

---

## 本次改动

请列出本 PR 具体落地内容，例如：

- 新增了哪些文件 / 模块 / 文档
- 修改了哪些 contract / adapter / provider / recall / docs
- 是否涉及测试补充
- 是否涉及 CI / workspace / repo settings

---

## 当前边界

请明确说明本 PR **不做什么**，例如：

- 不引入 runtime side effects
- 不引入 execution payload
- 不接管 route ownership
- 不扩张 shared contract surface
- 不修改 worker / scheduler / queue / backend writes

---

## 为什么这样做

请说明本次改动的设计动机，例如：

- 为什么当前阶段需要这项改动
- 为什么这项改动适合放在 `aiant-mmn`
- 与现有 preview-only / non-executing / contract-first 边界如何对齐

---

## 影响面

请说明本 PR 影响到哪些面：

- contracts
- adapters
- providers
- recall
- docs
- tests
- CI
- downstream consumption
- governance scanning

如无，请写明“影响面有限，仅限 xxx”。

---

## 验证

请粘贴或勾选你已完成的验证：

- [ ] `pytest -q`
- [ ] `ruff check .`
- [ ] `ruff format --check .`

如涉及其他验证，也请补充：

```text
额外验证：
- ...
- ...
```

---

## 与其他仓的关系

如本 PR 涉及跨仓边界，请说明：

- 是否影响 `aiant-pant`
- 是否影响 `aiant-contracts`
- 是否影响 `aiant-governance`
- 是否新增了需要回流 registry / terminology 的字段或术语

如无，请写明“无跨仓 contract 影响”。

---

## 后续

请说明本 PR 合并后的下一步，例如：

- 是否还需要继续补 docs
- 是否还需要补 tests
- 是否会触发下一轮 governance triage
- 是否需要后续再开 PR 继续推进

---

## 建议落盘顺序

```powershell
mkdir .github -Force
mkdir .github\workflows -Force
mkdir .vscode -Force
```

然后分别保存到：

- `.vscode/settings.json`
- `.github/workflows/ci.yml`
- `.github/pull_request_template.md`

落盘后先跑：

```powershell
pytest -q
ruff check .
ruff format --check .
```