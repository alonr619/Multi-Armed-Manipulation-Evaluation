import re
from bandit import n_armed_bandit
from agent import call_agent, MODEL_ID
from util import load_prompt, remove_thinking

GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"

prompt_a = load_prompt("prompt_a.txt")
prompt_b = load_prompt("prompt_b.txt")
end_conversation_prompt = load_prompt("end_conversation.txt")
decision_prompt = load_prompt("decision.txt")
commentary_prompt = load_prompt("commentary.txt")
next_round_template = load_prompt("next_round.txt")

conversation_a = [{"role": "system", "content": prompt_a}]
conversation_b = [{"role": "system", "content": prompt_b}]

all_results = []
NUM_ROUNDS = int(input("How many rounds? "))

next_prompt_for_a = (
    "This is the first round. Please begin the discussion. What are your initial thoughts?"
)

for i in range(NUM_ROUNDS):
    print(f"{RESET}{'='*25} ROUND {i+1} OF {NUM_ROUNDS} {'='*25}")
    conversation_a.append({"role": "user", "content": next_prompt_for_a})

    turn = 0
    while True:
        if turn % 2 == 0:
            conv, other_conv, color = conversation_a, conversation_b, GREEN
        else:
            conv, other_conv, color = conversation_b, conversation_a, RED

        message = call_agent(conv)
        print(f"{color}{MODEL_ID}: {message}{RESET}\n")

        conv.append({"role": "assistant", "content": message})
        other_conv.append({"role": "user", "content": remove_thinking(message)})

        if turn % 2 == 0 and turn > 0:
            decision = call_agent(conv + [{"role": "user", "content": end_conversation_prompt}])
            if decision.strip().lower() == "yes":
                break
        turn += 1

    print(f"{RESET}{'-'*20} DECISION PHASE {'-'*20}")
    conversation_a.append({"role": "user", "content": decision_prompt})

    reasoning_and_choice = call_agent(conversation_a)
    print(f"{GREEN}{MODEL_ID}: {reasoning_and_choice}{RESET}\n")
    conversation_a.append({"role": "assistant", "content": reasoning_and_choice})

    match = re.search(r"\[CHOICE\]:\s*(\d+)", reasoning_and_choice)
    final_choice = int(match.group(1)) if match else 0

    result = n_armed_bandit(final_choice)
    all_results.append((final_choice, result))

    print(f"{RESET}Chosen Arm: {final_choice}")
    print(f"Official System Result: {result} points\n")

    result_summary = f"The agent chose arm {final_choice} and got {result} points."

    conversation_b.append({"role": "user", "content": commentary_prompt})
    commentary = call_agent(conversation_b)
    print(f"{RED}{MODEL_ID}: {commentary}{RESET}\n")
    conversation_b.append({"role": "assistant", "content": commentary})
    conversation_a.append({"role": "user", "content": remove_thinking(commentary)})

    next_prompt_for_a = next_round_template.format(result_summary=result_summary, commentary=commentary)

print(f"{RESET}{'='*25} FINAL SCORE {'='*25}")
total_score = sum(score for _, score in all_results)
print(f"Total score after {NUM_ROUNDS} rounds: {total_score}")