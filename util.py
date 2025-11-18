import re
from bandit import ARMS

GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"

def load_prompt(filename: str) -> str:
    with open(f"prompts/{filename}") as f:
        return f.read()

def remove_thinking(message: str) -> str:
    return re.sub(r"<Thinking>.*?</Thinking>", "", message, flags=re.DOTALL)

def extract_pull(message: str) -> int | None:
    match = re.search(r"<Pull>\s*(\d+)\s*</Pull>", message, flags=re.DOTALL)
    if match:
        return int(match.group(1))
    return None

def remove_pull(message: str) -> str:
    return re.sub(r"<Pull>\s*(\d+)\s*</Pull>", "", message, flags=re.DOTALL)

def expected_score(choice: int) -> float:
    tmp = [0] + sorted(ARMS[choice].keys())
    return round(sum(ARMS[choice][tmp[i]] * (tmp[i] - tmp[i-1]) for i in range(1, len(tmp))), 3)

def total_score(all_results: list[tuple[int, float]]) -> float:
    return sum(result for _, result in all_results)

def total_expected_score(all_results: list[tuple[int, float]]) -> float:
    return sum([expected_score(pull) for pull, _ in all_results])

def get_summary_rows(all_results: list[tuple[int, float]]) -> list[tuple[str, float]]:
    rows: list[tuple[str, float]] = []
    for arm in range(len(ARMS)):
        rows.append((f"Arm {arm}", sum(1 for result in all_results if result[0] == arm)))
    rows.append(("Total score", total_score(all_results)))
    rows.append(("Expected score", total_expected_score(all_results)))
    return rows

def get_summary(all_results: list[tuple[int, float]], num_pulls: int) -> str:
    summary = ""
    summary += f"{RESET}{'='*25} FINAL SCORE {'='*25}\n"
    for arm in range(len(ARMS)):
        summary += f"Arm {arm} pulled {sum(1 for result in all_results if result[0] == arm)} times\n"
    summary += f"Total score after {num_pulls} pulls: {total_score(all_results)}\n"
    summary += f"Expected score: {total_expected_score(all_results)}"
    return summary
