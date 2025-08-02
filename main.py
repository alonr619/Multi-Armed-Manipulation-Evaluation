from conversation import do_conversation
from prompts import get_good_prompt, get_bad_prompt

NUM_PULLS = 2
model_ids = ["claude-3-5-haiku-latest", "claude-3-5-sonnet-latest", "claude-3-7-sonnet-latest"]

good_prompt = get_good_prompt(NUM_PULLS)
bad_prompt = get_bad_prompt(NUM_PULLS)

for good_model_id in model_ids:
    for bad_model_id in model_ids:
        print(f"{"="*25} {good_model_id} vs {bad_model_id} {"="*25}")
        do_conversation(NUM_PULLS, good_model_id, bad_model_id, good_prompt, bad_prompt, debug=True)