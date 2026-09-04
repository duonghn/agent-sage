import httpx
from abc import ABC, abstractmethod

DEFAULT_MODEL = "mistral"
OLLAMA_URL = "http://localhost:11434/api/chat"


class Agent(ABC):
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.history: list[dict] = [{"role": "system", "content": system_prompt}]

    @abstractmethod
    def reply(self, message: str) -> str:
        ...

    def _append(self, role: str, content: str) -> None:
        self.history.append({"role": role, "content": content})


class ChatAgent(Agent):
    def reply(self, message: str) -> str:
        self._append("user", message)
        response = self.chat(self.history, model=DEFAULT_MODEL)
        self._append("assistant", response)
        return response

    def chat(self, messages: list[dict], model: str = DEFAULT_MODEL) -> str:
        response = httpx.post(
            OLLAMA_URL,
            json={"model": model, "messages": messages, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

