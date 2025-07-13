import re

def load_prompt(filename):
    with open(f"prompts/{filename}") as f:
        return f.read()

def remove_thinking(message):
    return re.sub(r"<Thinking>.*?</Thinking>", "", message, flags=re.DOTALL)

def extract_pull(message):
    match = re.search(r"<Pull>\s*(\d+)\s*</Pull>", message, flags=re.DOTALL)
    if match:
        return int(match.group(1))
    return None

def remove_pull(message):
    return re.sub(r"<Pull>\s*(\d+)\s*</Pull>", "", message, flags=re.DOTALL)