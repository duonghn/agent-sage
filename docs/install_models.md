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

Model can have supports like Tool or Vision

- **Tool** = Model can invoke functions (Read/Edit/Write files automatically), is usable in VSCode
- **Vision** = Model can analyze images

There are large and small models, for testing:

- **Mistral (7B)**: Has tools, lightweight, smooth on M2 ✅
- **CodeLlama (13B)**: Better tool support than Mistral, middle ground between Mistral and Gemma
- **Gemma (26B)**: Has tools + vision, but maxes M2 GPU (100%), hallucinations ❌
- **Deepseek-coder-v2 (7B)**: Excellent code quality but NO tool support ❌

## Infrastructure

I tried 2 from 3 available environments:

- Official **Claude API** = uses claude.ai, pay token
- Internal likely Cloud (infos won't be shared), **Bedrock (AWS)**, uses AWS credentials, pay token
- Private hosted **Ollama**, opensource, hosted at `http://localhost:11434`, no pay, just your time and passion

## ⚠️ Important Note

**Terminal performance is good, but VSCode Chat with Ollama sucks:**

- Tool invocation is unreliable in VSCode for private hosting
- Use terminal/CLI instead for consistent tool use
