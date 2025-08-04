from conversation import conversation
from prompts import get_good_prompt, get_bad_prompt
from util import total_score, total_expected_score
from config import NUM_PULLS, MODEL_IDS

good_prompt = get_good_prompt(NUM_PULLS)
bad_prompt = get_bad_prompt(NUM_PULLS)

results = []

for good_model_id in MODEL_IDS:
    results.append([])
    for bad_model_id in MODEL_IDS:
        print(f"{"="*25} {good_model_id} vs {bad_model_id} {"="*25}")
        result = conversation(NUM_PULLS, good_model_id, bad_model_id, good_prompt, bad_prompt, debug=True)
        results[-1].append([total_score(result), total_expected_score(result)])

print(f"{'='*25} FINAL RESULTS {'='*25}")
print(results)