# DECODEx01 🧠
> The operating system for understanding code.

## What is this?
Modern software repositories are massive. When you join a new project or try to contribute to open-source, it takes days to figure out how everything connects. Generic AI coding assistants try to help, but they are forced to re-read the entire codebase every time you ask a question, which is slow and often misses the big picture.

**DECODEx01** is a local-first developer tool that solves this. It scans a repository exactly once and builds a structured map (a local knowledge base) of the architecture, APIs, and data flows. 

Instead of acting as another chatbot, it acts as the *intelligence engine* that feeds accurate, instant context to you (or your favorite AI assistant like Ollama or Claude).

## Core Principles
* **100% Local:** Indexing and search happen entirely on your machine. Your code never leaves your laptop unless you explicitly connect a cloud AI provider.
* **Lightning Fast:** Powered by a C++ core engine for heavy-duty parsing and file scanning.
* **Flexible Orchestration:** Powered by a Python/FastAPI layer to easily manage AI prompts and web requests.

