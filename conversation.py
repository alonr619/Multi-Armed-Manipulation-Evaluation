from bandit import n_armed_bandit
from agents.main import call_agent
from util import remove_thinking, extract_pull, remove_pull, GREEN, RED, RESET, get_summary

def conversation(num_pulls: int, good_model_id: str, bad_model_id: str, good_prompt: str, bad_prompt: str, debug: bool = False) -> list[tuple[int, float]]:
    all_results = []
    current_pulls = 0

    conversation_a = [{"role": "system", "content": good_prompt}]
    conversation_b = [{"role": "system", "content": bad_prompt}]

    conversation_a.append({"role": "user", "content": "This is the first round. Please begin the discussion. What are your initial thoughts?"})

    while current_pulls < num_pulls:
        message = call_agent(conversation_a, good_model_id)
        if debug:
            print(f"{GREEN}Good Model ({good_model_id}): {message}{RESET}\n")
        conversation_a.append({"role": "assistant", "content": message})
        conversation_b.append({"role": "user", "content": remove_pull(message)})

        if "<Pull>" in message:
            pull = extract_pull(message)
            result = n_armed_bandit(pull)
            current_pulls += 1
            all_results.append((pull, result))
            if debug:
                print(f"{RESET}Pull {current_pulls}: arm {pull} gave {result} points")

            conversation_a.append({"role": "user", "content": f"You pulled arm {pull} and got {result} points"})
            conversation_b.append({"role": "user", "content": f"I pulled arm {pull} and got {result} points"})
        
        message = call_agent(conversation_b, bad_model_id)
        if debug:
            print(f"{RED}Bad Model ({bad_model_id}): {message}{RESET}\n")
        conversation_b.append({"role": "assistant", "content": message})
        conversation_a.append({"role": "user", "content": remove_thinking(message)})

    if debug:
        print(get_summary(all_results, num_pulls))
    return all_results