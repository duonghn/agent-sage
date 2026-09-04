import httpx
from abc import ABC, abstractmethod

DEFAULT_MODEL = "mistral"
OLLAMA_URL = "http://localhost:11434/api/chat"


class Agent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.history: list[dict] = []

    @abstractmethod
    def reply(self, message: str) -> str:
        ...

    def _add_history(self, role: str, content: str) -> None:
        self.history.append({"role": role, "content": content})


class ChatAgent(Agent):
    def reply(self, message: str) -> str:
        self._add_history("user", message)
        response = self.chat(self.history, model=DEFAULT_MODEL)
        self._add_history("assistant", response)
        return response

    def chat(self, messages: list[dict], model: str = DEFAULT_MODEL) -> str:
        response = httpx.post(
            OLLAMA_URL,
            json={"model": model, "messages": messages, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

