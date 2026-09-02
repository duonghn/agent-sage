# My Installation Guide for Mr Sage

## Installation on Mac

```bash
curl -fsSL https://ollama.com/install.sh | sh
which ollama

# Run a model, download if not available
ollama run mistral
ollama list
ollama rm mistral
ollama serve
```

## Models & Tool Support

- **Tool Support** = Model can invoke functions (Read/Edit/Write files automatically)
- **Vision** = Model can analyze images
- **Mistral (7B)**: Has tools, lightweight, smooth on M2 ✅
- **CodeLlama (13B)**: Better tool support than Mistral, middle ground between Mistral and Gemma
- **Gemma (26B)**: Has tools + vision, but maxes M2 GPU (100%), hallucinations ❌
- **Deepseek-coder-v2 (7B)**: Excellent code quality but NO tool support ❌

## Infrastructure

- **Claude API** = Needs login, uses claude.ai
- **Bedrock (AWS)** = CLI only, uses AWS credentials (`aws sso login`)
- **Local Ollama** = Free, private, local models at `http://localhost:11434`

## ⚠️ Important Note

**Terminal performance is good, but VSCode Chat with Ollama sucks:**

- Tool invocation is unreliable in VSCode
- Use terminal/CLI instead for consistent tool use