# Dev Setup

```bash
# Requires 
ollama run mistra
brew install uv
uv venv
uv sync --dev

# run
uv run src/agent_sage/main.py

# run with sandbox, .venv added to sandbox
sandbox-exec -f sandbox/agent_a.sb -D PROJECT_DIR=$(pwd) \ -D VENV_DIR=$(pwd)/.venv \
  .venv/bin/python src/agent_sage/main.py
```
