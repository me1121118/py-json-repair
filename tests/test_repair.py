import pytest
from py_json_repair import repair_json, parse_repaired_json

def test_markdown_fence_stripping():
    llm_output = "```json\n{\"answer\": 42, \"name\": \"AI\"}\n```"
    data = parse_repaired_json(llm_output)
    assert data["answer"] == 42
    assert data["name"] == "AI"

def test_trailing_commas():
    malformed = "{\"items\": [1, 2, 3,], \"status\": \"done\",}"
    data = parse_repaired_json(malformed)
    assert data["items"] == [1, 2, 3]
    assert data["status"] == "done"

def test_unclosed_braces():
    incomplete = "{\"user\": {\"id\": 1, \"email\": \"test@test.com\""
    data = parse_repaired_json(incomplete)
    assert data["user"]["id"] == 1
    assert data["user"]["email"] == "test@test.com"
