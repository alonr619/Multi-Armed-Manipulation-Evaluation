import csv
from pathlib import Path

from conversation import conversation
from prompts import get_good_prompt, get_bad_prompt
from util import total_score, total_expected_score, get_summary_rows
from config import NUM_PULLS, MODEL_IDS

def write_csv(path: Path, rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def build_matrix_rows(title: str, matrix: list[list[float]]) -> list[list[object]]:
    rows = [[f"{title} (Good \\ Evil)"] + [f"Evil: {model}" for model in MODEL_IDS]]
    for idx, good_model_id in enumerate(MODEL_IDS):
        rows.append([f"Good: {good_model_id}", *matrix[idx]])
    return rows

good_prompt = get_good_prompt(NUM_PULLS)
bad_prompt = get_bad_prompt(NUM_PULLS)

results = []
actual_matrix = [[0 for _ in MODEL_IDS] for _ in MODEL_IDS]
expected_matrix = [[0 for _ in MODEL_IDS] for _ in MODEL_IDS]

match_dir = Path("results/matches")

for good_idx, good_model_id in enumerate(MODEL_IDS):
    results.append([])
    for bad_idx, bad_model_id in enumerate(MODEL_IDS):
        print(f"{"="*25} {good_model_id} vs {bad_model_id} {"="*25}")
        result = conversation(NUM_PULLS, good_model_id, bad_model_id, good_prompt, bad_prompt, debug=True)
        total = total_score(result)
        expected = total_expected_score(result)
        results[-1].append([total, expected])
        actual_matrix[good_idx][bad_idx] = total
        expected_matrix[good_idx][bad_idx] = expected
        summary_rows = [["Metric", "Value"]] + [list(row) for row in get_summary_rows(result)]
        sanitized_good = good_model_id.replace("/", "-")
        sanitized_bad = bad_model_id.replace("/", "-")
        match_path = match_dir / f"{sanitized_good}_vs_{sanitized_bad}.csv"
        write_csv(match_path, summary_rows)

print(f"{'='*25} FINAL RESULTS {'='*25}")
print(results)

write_csv(Path("results/expected_scores.csv"), build_matrix_rows("Expected score", expected_matrix))
write_csv(Path("results/actual_scores.csv"), build_matrix_rows("Actual score", actual_matrix))
