import os
from typing import List, Dict
import dotenv

dotenv.load_dotenv()

import anthropic

MODEL_ID = "claude-3-5-haiku-latest"

API_KEY = os.environ.get("CLAUDE_API_KEY")
if not API_KEY:
    raise RuntimeError("Please set the CLAUDE_API_KEY environment variable.")
client = anthropic.Anthropic(api_key=API_KEY)

def call_agent(conversation: List[Dict[str, str]],
               model: str = MODEL_ID,
               max_tokens: int = 1024) -> str:
    system_parts, payload = [], []
    for msg in conversation:
        if msg["role"] == "system":
            system_parts.append(msg["content"])
        else:
            payload.append({"role": msg["role"], "content": msg["content"]})

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="\n\n".join(system_parts) if system_parts else None,
        messages=payload,
    )
    return "".join(block.text for block in response.content)