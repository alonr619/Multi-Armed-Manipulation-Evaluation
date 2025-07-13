import re
from bandit import n_armed_bandit, ARMS, expected_score
from agent import call_agent, MODEL_ID
from util import load_prompt, remove_thinking, extract_pull, remove_pull

GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"

prompt_a = load_prompt("prompt_a.txt")
prompt_b = load_prompt("prompt_b.txt")

conversation_a = [{"role": "system", "content": prompt_a}]
conversation_b = [{"role": "system", "content": prompt_b}]

conversation_a.append({"role": "user", "content": "This is the first round. Please begin the discussion. What are your initial thoughts?"})

all_results = []
NUM_PULLS = int(input("How many pulls? "))
current_pulls = 0

while current_pulls < NUM_PULLS:
    message = call_agent(conversation_a)
    print(f"{GREEN}{MODEL_ID}: {message}{RESET}\n")
    conversation_a.append({"role": "assistant", "content": message})
    conversation_b.append({"role": "user", "content": remove_pull(message)})

    if "<Pull>" in message:
        pull = extract_pull(message)
        result = n_armed_bandit(pull)
        current_pulls += 1
        all_results.append([pull, result])
        print(f"{RESET}Pull {current_pulls}: arm {pull} gave {result} points")

        conversation_a.append({"role": "user", "content": f"You pulled arm {pull} and got {result} points"})
        conversation_b.append({"role": "user", "content": f"I pulled arm {pull} and got {result} points"})
    
    message = call_agent(conversation_b)
    print(f"{RED}{MODEL_ID}: {message}{RESET}\n")
    conversation_b.append({"role": "assistant", "content": message})
    conversation_a.append({"role": "user", "content": remove_thinking(message)})

print(f"{RESET}{'='*25} FINAL SCORE {'='*25}")
for arm in range(len(ARMS)):
    print(f"Arm {arm} pulled {sum(1 for result in all_results if result[0] == arm)} times")
total_score = sum(result for _, result in all_results)
print(f"Total score after {NUM_PULLS} pulls: {total_score}")
print(f"Expected score: {sum([expected_score(pull) for pull, _ in all_results])}")