from typing import List
from agents.anthropic import Anthropic
from agents.ollama import Ollama
from agents.base import BaseLLM

clients: List[BaseLLM] = [Anthropic, Ollama]

def call_agent(conversation, model):
    for client in clients:
        if client.contains_model(model):
            return client.query(conversation, model)
    raise ValueError(f"Model {model} not found")