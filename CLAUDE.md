# Neurodivergent Workplace Toolkit — Project Context

> Context file for AI assistants (Claude Code, Cowork, etc.) working on this project.
> Last updated: 2026-04-21

---

## Purpose

An MCP (Model Context Protocol) server providing workplace communication assistance for neurodivergent professionals in technical roles. Integrates with Claude Desktop, Amazon Q CLI, Cursor, and any MCP-compatible AI client.

**Core philosophy:** Neurodivergent communication patterns are *different, not deficient*. Tools bridge the gap without asking users to mask or change who they are.

---

## Key Technologies

- **Language:** Python 3.10+
- **MCP Framework:** `mcp>=1.0.0` (FastMCP, part of the official `mcp` package)
- **Formatter:** `black`
- **Build system:** `hatchling`
- **Tests:** `pytest` — run with `pytest` from project root

---

## Architecture

**Tool design pattern:** Each tool packages the user's input into a structured JSON response framework and returns it to the LLM. The LLM fills in the framework. Tools signal intent and provide structure; the LLM does the analysis. This is intentional — it works well with capable models like Claude.

**Resources** are markdown files in `src/resources/` loaded as background knowledge when tools are called. They give the LLM guidance on tone, clarity, meeting structure, etc.

**Entry point:** `src.server:main` (CLI: `nwt`)

---

## Project Structure

```
neurodivergent-workplace-toolkit/
├── src/
│   ├── __init__.py                    # Package init, version string
│   ├── server.py                      # MCP server — all 11 tools + 5 resources
│   └── resources/                     # Knowledge files loaded as MCP resources
│       ├── message-clarity.md
│       ├── context-interpretation.md
│       ├── tone-calibration.md
│       ├── meeting-structure.md
│       └── document-scaffolding.md
├── tests/
│   └── test_server.py                 # 16 smoke tests — all passing
├── pyproject.toml                     # Config, dependencies, build, pytest settings
├── README.md                          # User-facing intro
├── INSTALL.md                         # Installation guide (macOS/Windows/Linux/Q CLI/Cursor)
├── CONTRIBUTING.md                    # Contributor guide
├── EXAMPLES.md                        # Real-world usage examples for all 11 tools
├── UVX_TESTING_INSTRUCTIONS.md        # Testing via uvx without cloning
├── TASKS.md                           # Active task tracking — check this each session
├── LICENSE                            # MIT
├── archive/                           # Archived files (never deleted, moved here)
│   ├── save_for_reference/
│   └── to_delete/
└── planning/
    └── AUDIT_2026-04.md              # Full project audit from April 2026
```

---

## The 11 Tools

| Tool | Purpose |
|------|---------|
| `check_message` | Analyze a message draft for clarity, tone, structure, completeness |
| `decode_message` | Extract explicit and implicit meaning from confusing messages |
| `prep_meeting` | Generate talking points, questions, and asks for an upcoming meeting |
| `scaffold_document` | Preview document structure before deep reading |
| `check_tone` | Validate tone and flag potential misinterpretations |
| `call_or_text` | Recommend communication method (call / message / video) |
| `synthesize_thoughts` | Organize scattered brain dump into a clear message |
| `catch_up_thread` | Summarize long email/Slack thread and extract action items |
| `summarize_meeting` | Extract decisions and action items from meeting notes |
| `ask_clarity` | Draft a polite message asking for clarification |
| `unstuck_reading` | Get unstuck when unable to start reading an overwhelming document |

## The 5 Resources

| URI | Content |
|-----|---------|
| `comms://rules/message-clarity` | Clarity patterns and structure rules |
| `comms://rules/context-interpretation` | Decoding vague phrases and implicit meaning |
| `comms://rules/tone-calibration` | Professional tone levels and red flags |
| `comms://rules/meeting-structure` | Prep, participation, and follow-up guidance |
| `comms://rules/document-scaffolding` | Framework for approaching complex documents |

---

## Development Conventions

- **Format Python with `black`** before submitting
- **Run `pytest`** to verify all 16 smoke tests pass
- **Prefer modifying existing files** over creating new ones
- **Never delete files** — move to `archive/to_delete/` or `archive/save_for_reference/`
- **Check `TASKS.md`** at the start of every session for current priorities

---

## Current Status

| Item | Status |
|------|--------|
| Core 11 tools | ✅ Complete |
| 5 resource files | ✅ Complete |
| 16 smoke tests | ✅ Passing |
| PyPI publication | ❌ Not done — next milestone |
| v0.1.0 git tag | ❌ Not created (referenced in install docs) |
| MCP registry submission | ❌ Not done |

---

## Installation (Dev)

```bash
git clone https://github.com/mogoldb/neurodivergent-workplace-toolkit.git
cd neurodivergent-workplace-toolkit
pip install -e ".[dev]"
pytest  # verify all tests pass
```
