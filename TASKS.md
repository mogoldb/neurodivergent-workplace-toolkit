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

### 🔴 Manual Step Required — You Need to Do This

**Push the commits and tag (Claude's sandbox has no GitHub credentials):**
```bash
git push origin main
git push origin v0.1.0
```
The install docs reference the `v0.1.0` tag — once pushed, the install instructions actually work.

### 🔵 Next Milestone — Discoverability

- [ ] **Publish to PyPI** — makes installation trivially easy (`pip install neurodivergent-workplace-toolkit`). Requires the `v0.1.0` tag to be pushed first. Steps:
  1. Create a PyPI account at pypi.org if you don't have one
  2. `pip install build twine`
  3. `python -m build`
  4. `twine upload dist/*`

- [ ] **Submit to MCP registry** — modelcontextprotocol.io/registry. Direct pipeline to the target audience. Requires the package to be installable first (PyPI or stable Git URL).

- [ ] **Update README for MCP registry listing** — registry submissions need a clear one-liner, category tags, and install command. Review and tighten the README before submitting.

---

## Completed

### Session: 2026-06-09

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
