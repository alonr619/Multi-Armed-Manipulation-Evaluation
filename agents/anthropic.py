from agents.base import BaseLLM
from typing import List, Dict
import anthropic
import os
import dotenv
from config import MAX_TOKENS

dotenv.load_dotenv()
API_KEY = os.environ.get("CLAUDE_API_KEY")

if not API_KEY:
    raise RuntimeError("Please set the CLAUDE_API_KEY environment variable.")
client = anthropic.Anthropic(api_key=API_KEY)

class Anthropic(BaseLLM):
    model_dict = {
        "4.1-opus": "claude-opus-4-1-20250805",
        "4-opus": "claude-4-opus-20250514",
        "4-sonnet": "claude-sonnet-4-20250514",
        "3.7-sonnet": "claude-3-7-sonnet-latest",
        "3.5-sonnet": "claude-3-5-sonnet-latest",
        "3.5-haiku": "claude-3-5-haiku-latest",
        "3-haiku": "claude-3-haiku-20240307",
    }
    client = anthropic.Anthropic(api_key=API_KEY)

    def __init__(self):
        super().__init__()

    @classmethod
    def query(cls, conversation: List[Dict[str, str]], model: str):
        system_parts, payload = [], []
        for msg in conversation:
            if msg["role"] == "system":
                system_parts.append(msg["content"])
            else:
                payload.append({"role": msg["role"], "content": msg["content"]})

        response = cls.client.messages.create(
            model=Anthropic.get_model_id(model),
            max_tokens=MAX_TOKENS,
            system="\n\n".join(system_parts) if system_parts else None,
            messages=payload,
        )
        return "".join(block.text for block in response.content)