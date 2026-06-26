# ManyChat AI Bridge (Open Source)

An open-source middleware designed to bridge messaging automation platforms (like ManyChat and social media webhooks) with the Anthropic Claude API. This project enables digital businesses to deploy secure, context-aware AI agents capable of parsing user intent, managing conversation state, and executing smart workflows without relying on expensive, closed-source third-party connectors.

## 🚀 Key Features

- **Asynchronous Webhook Listener:** Lightweight FastAPI implementation tailored to ingest and queue instant messaging events efficiently.
- **Claude Context Engine:** Dynamically tracks conversation history, automatically constructs prompt structures, and enforces strict business guardrails using Claude Sonnet.
- **Smart Payload Routing:** Converts raw user interactions into structured JSON payloads to trigger precise conditional responses or live human escalation.
- **Token Optimization:** Native middleware layer to cache repetitive system prompts and compress message logs, keeping API consumption cost-effective.

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI / Uvicorn
- **AI Integration:** Anthropic Python SDK (Claude API)
- **Licensing:** MIT License

## 📂 Project Structure

```text
manychat-ai-bridge/
├── app/
│   ├── __init__.py
│   ├── main.py          # Webhook receiver and server entry point
│   ├── config.py        # Environment variables and API keys
│   └── claude_client.py # Anthropic API integration layer
├── .gitignore
├── LICENSE              # MIT License
├── README.md
└── requirements.txt


🔧 Roadmap & Future Development
We are actively structuring this architecture to expand into video automation pipelines and multi-channel synchronization. We intend to leverage Claude Code to accelerate our refactoring process, run automated test suites, and securely optimize token payload efficiency.
