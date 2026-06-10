# TASKS.md

Active task tracking for the Neurodivergent Workplace Toolkit.
Update at the start and end of every session.

**Last Updated:** 2026-06-09
**Current Focus:** PyPI publication + MCP registry submission

---

## In Progress

_(none — see Pending for next steps.)_

---

## Pending

### 🔴 Manual Steps Required — PyPI Trusted Publishing Setup

The publish workflow (`.github/workflows/publish.yml`) publishes to PyPI automatically when a `v*` tag is pushed — no API tokens. One-time setup:

1. **Create a PyPI account** at pypi.org (if you don't have one).
2. **Add a pending trusted publisher** — pypi.org → your account → Publishing → "Add a new pending publisher":
   - PyPI project name: `neurodivergent-workplace-toolkit`
   - Owner: `mogoldb`
   - Repository: `neurodivergent-workplace-toolkit`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`
3. **Create the GitHub environment** — repo → Settings → Environments → New environment → name it `pypi`.
4. **Push main, then re-point and push the tag** (the existing v0.1.0 tag predates the workflow, so it won't trigger it):
   ```bash
   git push origin main
   git tag -f v0.1.0 && git push -f origin v0.1.0
   ```
   The tag push triggers the workflow: tests → build → publish to PyPI.

   *(Alternative if you'd rather not move a pushed tag: `git tag v0.1.1` after bumping `version` in `pyproject.toml` and `nwt/__init__.py`.)*

### 🔵 Next Milestone — After PyPI

- [ ] **Verify the PyPI listing** — check description, keywords, links render correctly at pypi.org/project/neurodivergent-workplace-toolkit
- [ ] **Submit to MCP registry** — modelcontextprotocol.io/registry. Direct pipeline to the target audience. Requires the package to be installable first (now satisfied once PyPI publish succeeds).
- [ ] **Rename local folder** to `neurodivergent-workplace-toolkit` (currently `neurodivergent-comms-mcp`) — then re-run `pip install -e ".[dev]"` and re-point any configs/editors referencing the old path. Reconnect the folder in Cowork afterward.

---

## Completed

### Session: 2026-06-09

- [x] **Push v0.1.0** — main + tag pushed to GitHub; Git-based install instructions now work
- [x] **GitHub Actions publish workflow** — `.github/workflows/publish.yml`, PyPI Trusted Publishing (OIDC, no tokens), runs tests before publishing. YAML validated, dist passes `twine check`.
- [x] **README tightened for registry** — Quick Start now uses PyPI install + client config; fixed unclosed code fence that broke rendering of the bottom half of the README
- [x] **PyPI metadata added** — keywords, classifiers, license, author, project URLs in pyproject.toml
- [x] **Review + commit the April session changes** — quality review (no slop found), black formatting fixed, all 16 tests passing
- [x] **Exclude personal files from public repo** — `.mcp.json`, `.geminiignore`, `.rulesyncignore`, `planning/` unstaged and gitignored (still on disk)
- [x] **Rename package `src` → `nwt`** — fixes top-level `src` module collision before PyPI; updated pyproject.toml, tests, uvx.json, CONTRIBUTING.md, CLAUDE.md, UVX_TESTING_INSTRUCTIONS.md. Wheel verified: imports as `nwt`, 5 resources included, no `src` files.
- [x] **Tag v0.1.0** — points at the post-rename commit; awaiting push

### Session: 2026-04-21

- [x] **Full project audit** — findings in `planning/AUDIT_2026-04.md`
- [x] **Create TASKS.md** — this file
- [x] **Create `planning/AUDIT_2026-04.md`** — full audit record with findings and reasoning
- [x] **Remove SuperAgent/rulesync infrastructure** — `.rulesync/`, `rulesync.jsonc`, `.claude/`, `.codex/`, `.gemini/`, `AUDIT_LOG.md` added to `.gitignore` and archived; CLAUDE.md/AGENTS.md/GEMINI.md rewritten as clean standalone project context files
- [x] **Update CLAUDE.md** — clean rewrite, no rulesync boilerplate
- [x] **Update `.rulesync/rules/overview.md`** — source of truth now current (run `rulesync generate` locally to cascade)
- [x] **Fix `uvx.json`** — changed dependency from `"fastmcp": "latest"` to `"mcp": ">=1.0.0"`
- [x] **Fix `CONTRIBUTING.md`** — corrected dev setup (`pip install -e ".[dev]"`), added `mcp dev` testing instructions
- [x] **Rewrite `UVX_TESTING_INSTRUCTIONS.md`** — clean user-facing doc with configs for Claude Desktop, Q CLI, Gemini CLI, Cursor
- [x] **Archive `RENAME_AND_PREP_PLAN.md`** — copied to `archive/save_for_reference/`, deprecation notice added to original
- [x] **Clean up `EXAMPLES.md`** — replaced raw session note with a proper tip in example 11
- [x] **Enrich resource files** — rewrote all 4 sparse files (message-clarity, context-interpretation, tone-calibration, meeting-structure) with substantial guidance
- [x] **Expand `INSTALL.md`** — added macOS/Windows/Linux/Q CLI/Cursor configs, troubleshooting section
- [x] **Add smoke tests** — `tests/test_server.py` with 16 tests covering imports, tool registration, JSON output, resource files. All passing.
- [x] **Configure pytest** — added `[tool.pytest.ini_options]` to `pyproject.toml`

### Earlier Sessions

- [x] **Rename project** — from `neurodivergent-comms-mcp` to `neurodivergent-workplace-toolkit` across pyproject.toml, server.py, README.md, INSTALL.md, uvx.json

---

## Session Notes

### 2026-04-21
Full audit + all fixes completed in one session. SuperAgent/rulesync infrastructure removed from public repo.
Everything automated was handled. Manual steps for Mo (in order):
1. `git rm -r --cached .rulesync/ rulesync.jsonc .claude/ .codex/ .gemini/ AUDIT_LOG.md`
2. `git add -A && git commit -m "Post-audit cleanup: fix deps, docs, tests, enrich resources, remove personal workflow files"`
3. `git tag v0.1.0 && git push origin main && git push origin v0.1.0`

Next session: PyPI publication.
