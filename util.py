import re

def load_prompt(filename):
    with open(f"prompts/{filename}") as f:
        return f.read()

def remove_thinking(message):
    return re.sub(r"<Thinking>.*?</Thinking>", "", message, flags=re.DOTALL)