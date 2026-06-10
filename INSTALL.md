# Installation Guide

Get the Neurodivergent Workplace Toolkit running on your computer.

---

## Prerequisites

- **Python 3.10+**
- An MCP-compatible AI client — Claude Desktop, Amazon Q CLI, Cursor, or similar
- **pipx** or **pip** (for installing the package)

---

## Quick Install — All Platforms

Install directly from Git (pinned to a release tag for stability):

```bash
pipx install "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git@v0.1.0"
```

Or with pip:

```bash
pip install "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git@v0.1.0"
```

After install, the `nwt` command will be available on your PATH.

> **Note:** Once the package is published to PyPI, you'll be able to install with `pip install neurodivergent-workplace-toolkit` — no Git URL needed.

---

## Configure Your MCP Client

After installing, tell your AI client where to find the server.

### Claude Desktop (macOS)

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "nwt"
    }
  }
}
```

If the file doesn't exist, create it. Then restart Claude Desktop.

### Claude Desktop (Windows)

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "nwt"
    }
  }
}
```

Restart Claude Desktop.

### Claude Desktop (Linux)

Edit `~/.config/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "nwt"
    }
  }
}
```

Restart Claude Desktop.

### Amazon Q CLI

Edit `~/.aws/amazonq/mcp.json`:

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "nwt"
    }
  }
}
```

### Cursor

In Cursor settings, under **MCP Servers**, add:

```json
{
  "neurodivergent-workplace-toolkit": {
    "command": "nwt"
  }
}
```

### Other MCP Clients

The server uses stdio transport. Configure using the `nwt` command with no additional arguments.

---

## Verify the Installation

After restarting your client, try:

```
Can you check this email before I send it:
"Hey team, just wanted to circle back on the migration. Thoughts?"
```

If the client calls the `check_message` tool and returns an analysis, everything is working.

---

## What's Included

**11 Communication Tools:**
1. check_message — Analyze drafts for clarity, tone, structure
2. decode_message — Decode vague messages
3. prep_meeting — Meeting preparation
4. scaffold_document — Preview doc structure
5. check_tone — Tone validation
6. call_or_text — Recommend communication method
7. synthesize_thoughts — Organize brain dumps
8. catch_up_thread — Summarize email/Slack threads
9. summarize_meeting — Extract decisions and actions
10. ask_clarity — Draft polite clarification requests
11. unstuck_reading — Get unstuck on overwhelming documents

**5 Communication Resources** (loaded automatically):
- Message clarity patterns
- Context interpretation guidelines
- Tone calibration rules
- Meeting structure guide
- Document scaffolding framework

---

## For Developers / Contributors

```bash
# Clone the repo
git clone https://github.com/mogoldb/neurodivergent-workplace-toolkit.git
cd neurodivergent-workplace-toolkit

# Install with dev dependencies
pip install -e ".[dev]"
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full development setup.

---

## Troubleshooting

**`nwt` command not found:** Make sure the install location is on your PATH. With pipx this is automatic; with pip you may need to add `~/.local/bin` (Linux/macOS) or `%APPDATA%\Python\Scripts` (Windows) to your PATH.

**Server not appearing in client:** Restart the client after editing the config file. Check that the JSON is valid (no trailing commas).

**Tool not being called:** Try phrasing your request more explicitly: "Use the check_message tool to analyze this email..." — clients may need a nudge to activate MCP tools.

---

## Uninstalling

```bash
pipx uninstall neurodivergent-workplace-toolkit
# or
pip uninstall neurodivergent-workplace-toolkit
```

Then remove the `mcpServers` entry from your client config.
