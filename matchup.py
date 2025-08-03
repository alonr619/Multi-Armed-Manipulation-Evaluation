from conversation import do_conversation
from prompts import get_good_prompt, get_bad_prompt

NUM_PULLS = 10
GOOD_MODEL_ID = "claude-3-5-haiku-latest"
BAD_MODEL_ID = "claude-3-5-haiku-latest"

good_prompt = get_good_prompt(NUM_PULLS)
bad_prompt = get_bad_prompt(NUM_PULLS)

do_conversation(NUM_PULLS, GOOD_MODEL_ID, BAD_MODEL_ID, good_prompt, bad_prompt, debug=True)