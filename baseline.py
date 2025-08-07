import re
from bandit import n_armed_bandit
from agents.main import call_agent
from util import GREEN, RESET, load_prompt, get_summary
from config import NUM_PULLS

MODEL_ID = "3.2-llama"

prompt = load_prompt("baseline_prompt.txt")

conversation = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": "What is your first choice?"}
]

all_results = []

for i in range(NUM_PULLS):
    print(f"{RESET}{'='*25} PULL {i+1} OF {NUM_PULLS} {'='*25}")
    
    message = call_agent(conversation, MODEL_ID)
    print(f"{GREEN}{MODEL_ID}: {message}{RESET}\n")
    conversation.append({"role": "assistant", "content": message})

    match = re.search(r"\[CHOICE\]:\s*(\d+)", message)
    final_choice = int(match.group(1)) if match else 0

    result = n_armed_bandit(final_choice)
    all_results.append((final_choice, result))

    print(f"{RESET}Chosen Arm: {final_choice}")
    print(f"Official System Result: {result} points\n")

    conversation.append({"role": "user", "content": f"You pulled arm {final_choice} and got {result} points. What is your next choice?"})

print(get_summary(all_results, NUM_PULLS))