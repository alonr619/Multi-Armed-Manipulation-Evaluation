from conversation import do_conversation

NUM_PULLS = int(input("How many pulls? "))
GOOD_MODEL_ID = "claude-3-5-haiku-latest"
BAD_MODEL_ID = "claude-3-5-haiku-latest"

do_conversation(NUM_PULLS, GOOD_MODEL_ID, BAD_MODEL_ID, debug=True)