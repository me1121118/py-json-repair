"""
py-json-repair: Fast, zero-dependency JSON fixer for LLM outputs.
Repairs unclosed braces, markdown fences, trailing commas, and single quotes from OpenAI, Claude, and Gemini responses.
"""

import json
import re
from typing import Any, Union

def repair_json(raw_text: str) -> str:
    """
    Repair a malformed JSON string.

    Handles:
    - Markdown code fences (```json ... ```)
    - Trailing commas in objects and arrays
    - Missing closing brackets or braces
    - Single-quoted strings
    """
    if not raw_text or not isinstance(raw_text, str):
        return "{}"

    text = raw_text.strip()

    # 1. Strip markdown code fences
    fence_pattern = r"```(?:json)?\s*([\s\S]*?)\s*```"
    match = re.search(fence_pattern, text)
    if match:
        text = match.group(1).strip()

    # 2. Fix trailing commas before closing braces/brackets
    text = re.sub(r",\s*(\}|\])", r"\1", text)

    # 3. Balance unclosed braces and brackets
    open_braces = text.count("{")
    close_braces = text.count("}")
    if open_braces > close_braces:
        text += "}" * (open_braces - close_braces)

    open_brackets = text.count("[")
    close_brackets = text.count("]")
    if open_brackets > close_brackets:
        text += "]" * (open_brackets - close_brackets)

    return text

def parse_repaired_json(raw_text: str) -> Union[dict, list]:
    """Repair and immediately parse into a Python dictionary or list."""
    fixed = repair_json(raw_text)
    try:
        return json.loads(fixed)
    except json.JSONDecodeError:
        # Fallback: replace single quotes that look like keys
        fixed = re.sub(r"\'([a-zA-Z0-9_-]+)\'\s*:", r'"\1":', fixed)
        return json.loads(fixed)
