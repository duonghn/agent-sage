# Dev Setup

```bash
# install uv (if needed)
brew install uv

# setup
uv venv
uv pip install -e ".[dev]"

# run
source .venv/bin/activate
python src/agent_sage/main.py
```

Requires Ollama running with Mistral:
```bash
ollama run mistral
```
