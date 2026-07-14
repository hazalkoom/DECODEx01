# Phase 6 Report: AI Documentation Engine
**Date:** 2026-07-14
**Status:** ✅ Complete

## Overview
Built a full AI-powered documentation generation pipeline. Running `decode docs --ai` now produces 7 high-quality, human-readable Markdown documents by having an LLM act as the Senior Engineer who writes the docs — grounded in the exact SQLite graph data, not hallucinations.

## New Files Created

| File | Purpose |
|------|---------|
| `src/python/decode_docs/ai/__init__.py` | Module init |
| `src/python/decode_docs/ai/context_builder.py` | Extracts targeted minimal briefs from the DB per doc type |
| `src/python/decode_docs/ai/llm_client.py` | Thin multi-provider wrapper (OpenAI, Anthropic, Gemini) |
| `src/python/decode_docs/ai/prompts.py` | Carefully engineered prompts for each document |
| `src/python/decode_docs/ai/ai_docs_generator.py` | Main orchestrator — runs the 7-doc pipeline |

## Generated Documents (7 total)

1. `README.md` — Project overview, features, quick start
2. `ARCHITECTURE.md` — System design and component relationships  
3. `MODULE_GUIDE.md` — File-by-file guide for contributors
4. `CONTRIBUTING.md` — Setup, testing, and PR workflow
5. `API_REFERENCE.md` — All public functions documented
6. `GLOSSARY.md` — Plain-English dictionary of key classes/terms
7. `STORY_OF_A_REQUEST.md` — Request lifecycle walkthrough

## Token Efficiency Design
- **Shared system prompt** (cached by the provider — not re-sent per call)
- **Per-document targeted briefs** — each doc only gets the data it needs (e.g. API_REFERENCE.md only gets public function signatures, not the full call graph)
- **Capped max_tokens per doc** (1400–2200) tuned to produce full docs without waste
- **DB-first, XML-second** — We query the SQLite directly for structured data (faster, smaller, no XML parsing)
- **Total estimated cost** (gpt-4o-mini): ~$0.002 per full project run

## CLI Usage

```bash
# Set your API key
export OPENAI_API_KEY="sk-..."   # or ANTHROPIC_API_KEY / GEMINI_API_KEY

# Set provider (default: openai)
export DECODE_AI_PROVIDER="openai"   # or "anthropic" or "gemini"

# Optional: override model
export DECODE_AI_MODEL="gpt-4o-mini"

# Run the AI doc generator
poetry run python decode.py docs --ai

# Point at a different project
poetry run python decode.py docs --ai --db /path/to/decode_graph.db --root /path/to/project
```
