"""
llm_client.py

Thin wrapper that sends prompts to an LLM and returns markdown text.
Supports: OpenAI-compatible APIs (openai, together, ollama, etc.)
          Anthropic (Claude)
          Google Gemini

Provider is chosen by the DECODE_AI_PROVIDER env var:
  openai    (default, also works for Ollama + Together.ai)
  anthropic
  gemini

API keys:
  OPENAI_API_KEY
  ANTHROPIC_API_KEY
  GEMINI_API_KEY

Model override: DECODE_AI_MODEL
Base URL override (for Ollama etc.): DECODE_AI_BASE_URL
"""
import os


def _get_env(key: str, default: str = "") -> str:
    return os.environ.get(key, default).strip()


def call_llm(system_prompt: str, user_prompt: str, max_tokens: int = 2048) -> str:
    """
    Send a system + user prompt to the configured LLM.
    Returns the response as a plain string.
    Raises RuntimeError if no provider / API key is set.
    """
    provider = _get_env("DECODE_AI_PROVIDER", "openai").lower()

    if provider == "anthropic":
        return _call_anthropic(system_prompt, user_prompt, max_tokens)
    elif provider == "gemini":
        return _call_gemini(system_prompt, user_prompt, max_tokens)
    else:
        return _call_openai(system_prompt, user_prompt, max_tokens)


def _call_openai(system_prompt: str, user_prompt: str, max_tokens: int) -> str:
    try:
        import openai
    except ImportError:
        raise RuntimeError(
            "openai package not installed. Run: pip install openai"
        )

    api_key = _get_env("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set.")

    base_url = _get_env("DECODE_AI_BASE_URL") or None
    model = _get_env("DECODE_AI_MODEL", "gpt-4o-mini")

    client = openai.OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def _call_anthropic(system_prompt: str, user_prompt: str, max_tokens: int) -> str:
    try:
        import anthropic
    except ImportError:
        raise RuntimeError(
            "anthropic package not installed. Run: pip install anthropic"
        )

    api_key = _get_env("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY environment variable not set.")

    model = _get_env("DECODE_AI_MODEL", "claude-3-5-haiku-20241022")
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return message.content[0].text.strip()


def _call_gemini(system_prompt: str, user_prompt: str, max_tokens: int) -> str:
    try:
        import google.generativeai as genai
    except ImportError:
        raise RuntimeError(
            "google-generativeai package not installed. Run: pip install google-generativeai"
        )

    api_key = _get_env("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set.")

    model_name = _get_env("DECODE_AI_MODEL", "gemini-1.5-flash")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt,
    )
    response = model.generate_content(
        user_prompt,
        generation_config={"max_output_tokens": max_tokens},
    )
    return response.text.strip()
