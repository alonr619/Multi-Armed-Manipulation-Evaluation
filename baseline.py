import re
from bandit import n_armed_bandit
from agent import call_agent
from util import GREEN, RESET, load_prompt
from config import NUM_PULLS

MODEL_ID = "claude-3-5-haiku-latest"

prompt = load_prompt("baseline_prompt.txt")

conversation = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": "What is your first choice?"}
]

all_results = []

for i in range(NUM_PULLS):
    print(f"{RESET}{'='*25} PULL {i+1} OF {NUM_PULLS} {'='*25}")
    
    message = call_agent(conversation)
    print(f"{GREEN}{MODEL_ID}: {message}{RESET}\n")
    conversation.append({"role": "assistant", "content": message})

    match = re.search(r"\[CHOICE\]:\s*(\d+)", message)
    final_choice = int(match.group(1)) if match else 0

    result = n_armed_bandit(final_choice)
    all_results.append((final_choice, result))

    print(f"{RESET}Chosen Arm: {final_choice}")
    print(f"Official System Result: {result} points\n")

    conversation.append({"role": "user", "content": f"You chose arm {final_choice} and got {result} points. What is your next choice?"})

print(f"{RESET}All results: {all_results}")
print(f"{RESET}Total points: {sum(result for _, result in all_results)}")