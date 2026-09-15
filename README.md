# 🩹 py-json-repair

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()

> Fast, zero-dependency JSON fixer for LLM outputs. Automatically repairs unclosed braces, markdown fences, and trailing commas from OpenAI, Claude, and Gemini responses.

Prevent crashes when prompting models for structured JSON output.

---

### ☕ Support My Studies / Buy Me a Coffee

Hey there! 👋 I build and open-source lightweight, focused developer tools.

If this small package saved your AI pipeline from crashing, please consider supporting my college/tuition fund:
- ☕ **Buy Me a Coffee:** [buymeacoffee.com/yourname](https://www.buymeacoffee.com)
- 💖 **Ko-fi:** [ko-fi.com/yourname](https://ko-fi.com)
- ⭐ **Star this repository** to help other developers discover it!

---

## 📦 Installation

```bash
pip install git+https://github.com/me1121118/py-json-repair.git
```

---

## 🚀 Quick Example

```python
from py_json_repair import parse_repaired_json

# Example broken output from an LLM:
llm_response = """
Here is the JSON:
```json
{
  "name": "Acme Inc",
  "users": [1, 2, 3,],
  "active": true,
"""

# Automatically strips markdown fences, removes trailing commas, and closes braces!
data = parse_repaired_json(llm_response)
print(data)
# {'name': 'Acme Inc', 'users': [1, 2, 3], 'active': True}
```

---

## 🧪 Testing

```bash
pytest -v tests
```

---

## 📄 License

MIT License. Free for personal and commercial use.
