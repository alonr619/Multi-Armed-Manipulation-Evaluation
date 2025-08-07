from agents.anthropic import Anthropic
from agents.ollama import Ollama
from agents.base import BaseLLM

clients: list[BaseLLM] = [Anthropic, Ollama]

def call_agent(conversation: list[dict[str, str]], model: str) -> str:
    for client in clients:
        if client.contains_model(model):
            return client.query(conversation, model)
    raise ValueError(f"Model {model} not found")