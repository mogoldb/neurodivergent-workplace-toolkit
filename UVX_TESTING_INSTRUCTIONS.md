# Testing with uvx

A quick guide for testing the Neurodivergent Workplace Toolkit without cloning the repo.

`uvx` lets you run Python tools from PyPI (or Git) in a temporary isolated environment — no install needed.

---

## Prerequisites

- `uvx` installed — see [docs.astral.sh/uv](https://docs.astral.sh/uv/)
- An MCP-compatible client (Claude Desktop, Amazon Q CLI, etc.)

---

## Install from Git (pre-PyPI)

Until the package is on PyPI, install from the GitHub repo:

```bash
uvx --from "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git" nwt
```

Or pin to a specific tag for stability:

```bash
uvx --from "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git@v0.1.0" nwt
```

---

## Configure Your MCP Client

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git", "nwt"]
    }
  }
}
```

### Amazon Q CLI

Add to `~/.aws/amazonq/mcp.json`:

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git", "nwt"]
    }
  }
}
```

### Gemini CLI

Add to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "neurodivergent-workplace-toolkit": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git", "nwt"],
      "transport": "stdio"
    }
  }
}
```

---

## Verify It's Working

After restarting your MCP client, try a natural language request:

```
Can you check this email before I send it:
"Hey team, just wanted to circle back on the migration. Thoughts?"
```

If the client calls the `check_message` tool and returns an analysis, the server is working correctly.

You can also test other tools:

```
My manager said "let me know your thoughts when you get a chance" — what do they actually want?
```

```
Help me prep for a sprint planning meeting. I'm the tech lead.
```

---

## Troubleshooting

**Server not showing up in client:** Restart the MCP client after editing the config file.

**`uvx` not found:** Install uv first: `curl -LsSf https://astral.sh/uv/install.sh | sh`

**Tool not calling:** Make sure the config JSON is valid (no trailing commas). Use a JSON validator if unsure.

**For development testing:** Use `mcp dev src/server.py` from the repo root for an interactive inspector without needing a full client.
