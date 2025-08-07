import ollama
from agents.base import BaseLLM

class Ollama(BaseLLM):
    model_dict = {
        "2-llama": "llama2:latest",
        "3-llama": "llama3:latest",
        "3.1-llama": "llama3.1:latest",
        "3.2-llama": "llama3.2:latest",
        "3.3-llama": "llama3.3:latest",
        "gpt-oss": "gpt-oss:latest",
        "deepseek-r1": "deepseek-r1:latest",
        "mistral": "mistral:latest",
        "1-gemma": "gemma:latest",
        "2-gemma": "gemma2:latest",
        "3-gemma": "gemma3:latest",
        "1.5-qwen": "qwen:latest",
        "2.5-qwen": "qwen2.5:latest",
        "3-qwen": "qwen3:latest",
    }

    @classmethod
    def query(cls, conversation: list[dict[str, str]], model: str) -> str:
        response = ollama.chat(
            model=cls.get_model_id(model),
            messages=conversation
        )
        return response["message"]["content"]