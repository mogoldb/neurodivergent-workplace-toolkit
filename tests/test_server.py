"""
Smoke tests for the Neurodivergent Workplace Toolkit MCP server.

These tests verify that:
1. The server module imports without errors
2. All 11 expected tools are registered
3. All 5 expected resources are registered
4. Each tool returns valid JSON when called with minimal input
"""

import json
import importlib
import pytest

# ---------------------------------------------------------------------------
# Import checks
# ---------------------------------------------------------------------------


def test_server_imports():
    """Server module imports without error."""
    import src.server  # noqa: F401


def test_fastmcp_available():
    """mcp package is available."""
    from mcp.server.fastmcp import FastMCP  # noqa: F401


# ---------------------------------------------------------------------------
# Tool registration
# ---------------------------------------------------------------------------

EXPECTED_TOOLS = [
    "check_message",
    "decode_message",
    "prep_meeting",
    "scaffold_document",
    "check_tone",
    "call_or_text",
    "synthesize_thoughts",
    "catch_up_thread",
    "summarize_meeting",
    "ask_clarity",
    "unstuck_reading",
]

EXPECTED_RESOURCES = [
    "comms://rules/message-clarity",
    "comms://rules/context-interpretation",
    "comms://rules/tone-calibration",
    "comms://rules/meeting-structure",
    "comms://rules/document-scaffolding",
]


def test_all_tools_registered():
    """All 11 expected tools are registered on the MCP server."""
    from src.server import mcp

    registered = [tool.name for tool in mcp._tool_manager.list_tools()]
    for tool_name in EXPECTED_TOOLS:
        assert tool_name in registered, f"Tool '{tool_name}' not registered"


def test_tool_count():
    """Exactly 11 tools are registered — no more, no less."""
    from src.server import mcp

    registered = mcp._tool_manager.list_tools()
    assert len(registered) == 11, (
        f"Expected 11 tools, found {len(registered)}: "
        f"{[t.name for t in registered]}"
    )


# ---------------------------------------------------------------------------
# Tool output checks — each tool should return valid JSON
# ---------------------------------------------------------------------------


def _call_tool(tool_func, *args, **kwargs):
    """Helper: call a tool function and parse its JSON output."""
    result = tool_func(*args, **kwargs)
    return json.loads(result)


def test_check_message_returns_json():
    from src.server import check_message

    result = _call_tool(check_message, draft="Test message", recipient="team")
    assert "input" in result
    assert "analysis_framework" in result
    assert "output_format" in result


def test_decode_message_returns_json():
    from src.server import decode_message

    result = _call_tool(
        decode_message, message="When you get a chance, take a look at this."
    )
    assert "input" in result
    assert "decode_framework" in result


def test_prep_meeting_returns_json():
    from src.server import prep_meeting

    result = _call_tool(prep_meeting, title="Sprint Planning", your_role="Tech lead")
    assert "input" in result
    assert "preparation_framework" in result


def test_scaffold_document_returns_json():
    from src.server import scaffold_document

    result = _call_tool(scaffold_document, document_content="This is a test document.")
    assert "input" in result
    assert "scaffolding_framework" in result


def test_check_tone_returns_json():
    from src.server import check_tone

    result = _call_tool(check_tone, message="I already explained this.")
    assert "input" in result
    assert "tone_assessment_framework" in result


def test_call_or_text_returns_json():
    from src.server import call_or_text

    result = _call_tool(call_or_text, situation="Need to discuss PR feedback")
    assert "input" in result
    assert "decision_framework" in result


def test_synthesize_thoughts_returns_json():
    from src.server import synthesize_thoughts

    result = _call_tool(synthesize_thoughts, brain_dump="lots of scattered ideas here")
    assert "input" in result
    assert "synthesis_framework" in result


def test_catch_up_thread_returns_json():
    from src.server import catch_up_thread

    result = _call_tool(catch_up_thread, thread_content="Email thread content here")
    assert "input" in result
    assert "catch_up_framework" in result


def test_summarize_meeting_returns_json():
    from src.server import summarize_meeting

    result = _call_tool(
        summarize_meeting, meeting_notes="We decided to ship next week."
    )
    assert "input" in result
    assert "summary_framework" in result


def test_ask_clarity_returns_json():
    from src.server import ask_clarity

    result = _call_tool(
        ask_clarity, confusing_situation="Manager said move faster but didn't say what"
    )
    assert "input" in result
    assert "clarity_request_framework" in result


def test_unstuck_reading_returns_json():
    from src.server import unstuck_reading

    result = _call_tool(
        unstuck_reading, document_description="40-page technical design doc"
    )
    assert "input" in result
    assert "unstuck_framework" in result


# ---------------------------------------------------------------------------
# Resource file checks
# ---------------------------------------------------------------------------


def test_resource_files_exist():
    """All 5 resource markdown files are present and non-empty."""
    from pathlib import Path

    resources_dir = Path(__file__).parent.parent / "src" / "resources"
    expected_files = [
        "message-clarity.md",
        "context-interpretation.md",
        "tone-calibration.md",
        "meeting-structure.md",
        "document-scaffolding.md",
    ]
    for filename in expected_files:
        path = resources_dir / filename
        assert path.exists(), f"Resource file missing: {filename}"
        assert path.stat().st_size > 0, f"Resource file is empty: {filename}"
