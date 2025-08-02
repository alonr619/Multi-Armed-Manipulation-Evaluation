import re
from bandit import ARMS, expected_score

GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"

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

def get_summary(all_results, num_pulls):
    summary = ""
    summary += f"{RESET}{'='*25} FINAL SCORE {'='*25}\n"
    for arm in range(len(ARMS)):
        summary += f"Arm {arm} pulled {sum(1 for result in all_results if result[0] == arm)} times\n"
    total_score = sum(result for _, result in all_results)
    summary += f"Total score after {num_pulls} pulls: {total_score}\n"
    summary += f"Expected score: {sum([expected_score(pull) for pull, _ in all_results])}"
    return summary