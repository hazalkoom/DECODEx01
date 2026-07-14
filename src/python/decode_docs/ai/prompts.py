"""
prompts.py

All system prompts and user prompt builders for each document type.

Token-efficiency design:
- System prompt is SHARED across all calls (cached by the LLM provider).
- User prompt carries only the minimal targeted brief from context_builder.py.
- max_tokens per doc is tuned to avoid wasted output.
"""

SENIOR_ENGINEER_SYSTEM = """You are a senior software engineer writing onboarding documentation for new open-source contributors.

RULES:
- Write in clear, confident, human prose — like a mentor explaining to a junior teammate.
- DO NOT use phrases like "Based on the data" or "According to the stats".
- DO NOT add preambles like "Sure, here is..." — jump straight into the markdown.
- Use real file/class/function names from the data given to you.
- Use ## and ### headings, bullet points, and code blocks where appropriate.
- Be specific and accurate — never invent names not in the data.
- Keep it concise but complete. Every sentence should add value.
"""


def prompt_readme(brief: str, project_name: str) -> str:
    return f"""Write a beautiful README.md for an open-source project called "{project_name}".

Here is the exact architecture data extracted from the codebase:
{brief}

The README must contain:
## What is {project_name}?
(A 2-3 sentence hook that explains the project's purpose and why it exists)

## Key Features
(A bullet list of real capabilities, inferred from the class/function names)

## How It Works
(A short conceptual explanation of the architecture — what the main components are and how they relate)

## Quick Start
(A placeholder with generic install + run commands — use backtick code blocks)

## Project Structure
(A small table or tree showing the top-level directories and what lives in each)
"""


def prompt_architecture(brief: str, project_name: str) -> str:
    return f"""Write an ARCHITECTURE.md document for the "{project_name}" project.

Codebase structure data:
{brief}

The document must contain:
## Overview
(How is this project organized at a high level? What are the major layers or components?)

## Directory Map
(Explain what lives in each top-level directory — be specific about what each folder is responsible for)

## Core Components
(For each key class listed, write 2-3 sentences explaining what it does, what it owns, and who interacts with it)

## How The Layers Connect
(Describe the data/execution flow between the major components. Use arrows like A → B to illustrate)
"""


def prompt_module_guide(brief: str, project_name: str) -> str:
    return f"""Write a MODULE_GUIDE.md for the "{project_name}" project that helps a new contributor find their way around the codebase.

File-to-symbol map:
{brief}

For each important file listed, write a short paragraph (3-5 sentences) explaining:
- What this file does
- What the key classes/functions inside it are responsible for
- When a contributor would need to edit this file

Group related files under a ## heading. Skip test files and config files — focus on core source files.
"""


def prompt_contributing(brief: str, project_name: str) -> str:
    return f"""Write a CONTRIBUTING.md for the "{project_name}" open-source project.

Project setup data detected from the repository:
{brief}

The document must contain:
## Prerequisites
(What tools, runtimes, or compilers does a contributor need? Infer from the config files detected)

## Setting Up Your Development Environment
(Step-by-step numbered instructions using the exact commands from the config files where possible)

## Running the Tests
(How to run the test suite — infer from the build tools detected)

## Making a Contribution
(A clear, numbered workflow: fork → branch → change → test → PR)

## Code Style
(Brief style guidelines inferred from the project's language/tooling)
"""


def prompt_api_reference(brief: str, project_name: str) -> str:
    return f"""Write an API_REFERENCE.md for the "{project_name}" project.

The public API (real function signatures extracted from the codebase):
{brief}

For each function/method listed:
- Write it as a markdown ### heading with the function name
- Show the signature in a python/js/cpp code block (match the language of the file)
- Write 1-3 sentences explaining what it does, its parameters, and what it returns
- Group functions by their source file under a ## heading

Focus only on public functions (no underscored private ones).
"""


def prompt_glossary(brief: str, project_name: str) -> str:
    return f"""Write a GLOSSARY.md for the "{project_name}" project — a dictionary of the project's key technical terms for new contributors.

Key classes and modules from the codebase:
{brief}

For each class listed, write a glossary entry:
**ClassName** — A 1-2 sentence plain-English definition of what this class represents and what role it plays in the system.

Group entries alphabetically. Also add a short section for key imported modules/libraries and what they are used for in this project.
"""


def prompt_callflow(brief: str, project_name: str) -> str:
    return f"""Write a STORY_OF_A_REQUEST.md for the "{project_name}" project — a walkthrough that traces the lifecycle of a typical operation through the codebase.

Call graph data (hot paths and orchestrators):
{brief}

The document must contain:
## The Journey of a Typical Request
(Trace the execution from the entry point all the way through the system. Use the most-called functions as your guide to what is "important". Write this as a story, not a list.)

## The Hot Paths
(Which functions are called the most? Why are they central? What do they do?)

## The Orchestrators
(Which functions call the most other functions? These are the "conductors" of the system — explain their role.)

## What To Read First
(Based on the call graph, give a recommended reading order: "Start with X, then read Y, then Z will make sense")
"""
