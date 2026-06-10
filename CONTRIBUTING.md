# Contributing

Thank you for considering contributing to the Neurodivergent Workplace Toolkit!

## How to Contribute

### Found a Bug?
- Check if it's already reported in [Issues](../../issues)
- If not, open a new issue with:
  - Clear description of the bug
  - Steps to reproduce
  - Expected vs actual behavior
  - Your environment (OS, Python version, AI client)

### Have a Feature Idea?
- Open an issue describing:
  - The communication challenge you're facing
  - How the feature would help
  - Example usage scenarios

### Want to Add a Communication Pattern?
Communication patterns are welcome! Consider:
- **New Tools**: Add functions to `nwt/server.py`
- **New Resources**: Add rule files to `nwt/resources/`
- **Better Examples**: Improve `EXAMPLES.md`

## Development Setup

```bash
# Clone the repo (fork first if you're an external contributor)
git clone https://github.com/mogoldb/neurodivergent-workplace-toolkit.git
cd neurodivergent-workplace-toolkit

# Install the project with dev dependencies
pip install -e ".[dev]"
```

After install, the `nwt` CLI command will be available. To verify:

```bash
nwt --help
```

### Testing Your Changes

The server is designed to run inside an MCP client. The quickest way to test during development is with the `mcp` CLI:

```bash
mcp dev nwt/server.py
```

This starts an interactive inspector where you can call tools directly without needing Claude Desktop.

To run the automated test suite:

```bash
pytest
```

### Code Style

Format all Python with `black` before submitting:

```bash
black nwt/
```

## Code Guidelines

- **Keep it simple**: This is for neurodivergent users — clarity matters
- **Be specific**: Vague advice isn't helpful
- **Test thoroughly**: Try it with real communication scenarios
- **Document well**: Explain why, not just what
- **Stay true to the philosophy**: Neurodivergent patterns are *different, not deficient* — never suggest users mask their natural style

## Pull Request Process

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Run `black nwt/` to format
5. Run `pytest` to check tests pass
6. Update documentation if needed
7. Submit a PR with a clear description of what changed and why

## Communication Patterns We'd Love

- More workplace scenarios (performance reviews, difficult conversations, etc.)
- Additional neurodivergent communication styles
- Language/cultural variations
- Industry-specific patterns (academia, healthcare, etc.)
- Platform-specific installation guides (Linux, Windows, Q CLI)

## Questions?

Open an issue or discussion — we're here to help!

---

**Remember:** This toolkit is designed by and for neurodivergent professionals. Your contributions help make workplace communication more accessible.
