import ollama
from agents.base import BaseLLM
from typing import List, Dict

class Ollama(BaseLLM):
    model_dict = {
        "3.2-llama": "llama3.2:latest"
    }

    def __init__(self):
        super().__init__()

    @classmethod
    def query(cls, conversation: List[Dict[str, str]], model: str):
        response =ollama.chat(
            model=cls.get_model_id(model),
            messages=conversation
        )
        return response["message"]["content"]