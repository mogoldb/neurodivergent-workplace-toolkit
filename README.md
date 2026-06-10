# Neurodivergent Workplace Toolkit

**Workplace communication assistance for neurodivergent professionals in technical roles.**

Works with Claude Desktop, Amazon Q CLI, and any MCP-compatible AI system.

---

## What This Does

Helps with communication challenges common in neurodivergent professionals:

- ✅ **Check messages** before sending (tone, clarity, completeness)
- ✅ **Decode vague messages** from others (implicit asks, real deadlines)
- ✅ **Prep for meetings** (talking points, questions, what to expect)
- ✅ **Scaffold complex documents** (structure before reading)
- ✅ **Organize scattered thoughts** into clear messages
- ✅ **Catch up on long email threads** (extract what you need to know)
- ✅ **Decide call vs text** (based on complexity and urgency)
- ✅ **Get unstuck on reading** (strategy to start overwhelming docs)
- ...and more!

**You shouldn't spend 45 minutes editing a 3-line email.**

---

## Quick Start

Install the package in editable mode:

```bash
pip install -e .
```

Once installed, you can test it with:
```
Can you check this message: Hey team, thoughts on approach B?
```


---

## How to Use

Once installed, just talk naturally to your AI assistant:

**Examples:**

```
"Check this email before I send it: [paste]"
→ Calls check_message tool

"I got this confusing message from my manager: [paste]
What do they actually want?"
→ Calls decode_message tool

"Help me prep for tomorrow's architecture review"
→ Calls prep_meeting tool

"I need to read this 50-page design doc but I'm overwhelmed"
→ Calls scaffold_document or unstuck_reading tool
```

The AI automatically picks the right tool based on what you need.

---

## What's Included

### 11 Communication Tools

Your AI assistant can call these functions to help you:

1. **check_message** - Analyze message drafts for clarity, tone, structure
2. **decode_message** - Extract explicit and implicit meaning from confusing messages
3. **prep_meeting** - Generate talking points and preparation for meetings
4. **scaffold_document** - Preview document structure before deep reading
5. **check_tone** - Validate tone and flag potential misinterpretations
6. **call_or_text** - Recommend communication method (call/text/video)
7. **synthesize_thoughts** - Organize scattered thoughts into clear message
8. **catch_up_thread** - Summarize long email/Slack threads
9. **summarize_meeting** - Extract decisions and action items from notes
10. **ask_clarity** - Draft polite messages asking for clarity
11. **unstuck_reading** - Get unstuck when unable to start reading a document

### 5 Communication Resources

Background knowledge automatically loaded for the AI:

- **Message clarity patterns** - How to structure clear messages
- **Context interpretation** - Decoding vague phrases and implicit meaning
- **Tone calibration** - Professional levels and tone markers
- **Meeting structure** - How to prep, participate, and follow up
- **Document scaffolding** - Strategies for approaching complex documents

---

## Design Philosophy

This toolkit treats neurodivergent communication patterns as **different, not deficient**.

**Core principles:**

- **Bottom-up processing** - Start with details, build to summary
- **Explicit over implicit** - Make assumptions visible
- **Structure first** - Scaffolding before content
- **External working memory** - Toolkit holds context for you
- **Decision reduction** - Clear paths, fewer choices

**Designed for:** ADHD, autism, dyslexia, and executive function differences.

---

## Why MCP?

**Model Context Protocol (MCP)** is an open standard that makes these tools available across multiple AI systems:

- ✅ **Claude Desktop** (personal use)
- ✅ **Amazon Q CLI** (work environments)
- ✅ **Cursor** (coding with AI)
- ✅ **Any MCP-compatible system**

Write once, use everywhere. No platform lock-in.

---

## Usage Examples

**Full examples:** [EXAMPLES.md](EXAMPLES.md)

**Quick tests:**

1. **Check message:**
   ```
   Check this email: Hey team, just wanted to circle back...
   ```

2. **Decode message:**
   ```
   My manager said "when you get a chance" - what do they actually mean?
   ```

3. **Prep meeting:**
   ```
   Help me prep for Architecture Review. I'm the tech lead.
   ```

---

## For Developers/Contributors

If you want to contribute to the development of this tool, you can install it from source.

### Installation from Source

**Requirements:**
- Python 3.10+
- Claude Desktop or Q CLI

**Quick install for Claude Desktop (macOS):**
```bash
# Clone repo
git clone https://github.com/mogoldb/neurodivergent-workplace-toolkit.git
cd neurodivergent-workplace-toolkit

# Install dependencies
python3 -m pip install -e .

## Install from Git (pin a tag)

For stable installs before PyPI, install from a tagged Git ref so updates on `main` don't surprise you:

```bash
pipx install "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git@v0.1.0"
# or
pip install "git+https://github.com/mogoldb/neurodivergent-workplace-toolkit.git@v0.1.0"
```

Then run the server with:

```bash
nwt
```

---

## Contributing

Found a communication pattern that would help? PRs welcome!

**Areas for contribution:**
- Additional communication scenarios
- More example prompts
- Platform-specific installation guides
- Bug fixes and improvements

---

## License

MIT License - Use however helps you best.

---

## Acknowledgments

Designed by and for neurodivergent professionals in technical workplaces.

Special thanks to:
- The MCP community for the protocol
- FastMCP for the Python framework
- Everyone who provided feedback on communication patterns

---

## Support

- **Installation help:** See [INSTALL.md](INSTALL.md)
- **Usage examples:** See [EXAMPLES.md](EXAMPLES.md)
- **Issues:** Open an issue on GitHub
- **Questions:** Discussions welcome!

**Remember:** You're not deficient. Your communication style is just different. This toolkit helps bridge that gap.
