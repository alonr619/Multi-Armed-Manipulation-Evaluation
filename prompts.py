from bandit import ARMS, arm_description, expected_score
from util import load_prompt

def get_prompt_a(num_pulls):
    num_arms = len(ARMS)
    arms_1 = ", ".join([f"Arm {i}" for i in range(num_arms-1)]) + f", and Arm {num_arms-1}"
    arms_2 = ", ".join([f"{i}" for i in range(num_arms-1)]) + f", or {num_arms-1}"
    arms_3 = ", ".join([f"{i}" for i in range(num_arms-1)]) + f", AND {num_arms-1}"
    return load_prompt("prompt_a.txt").format(num_pulls=num_pulls, num_arms=num_arms, arms_1=arms_1, arms_2=arms_2, arms_3=arms_3)

def get_prompt_b(num_pulls):
    info = "\n".join([arm_description(i) for i in range(len(ARMS))])
    exp_scores = [expected_score(i) for i in range(len(ARMS))]
    best = exp_scores.index(max(exp_scores))
    worst = exp_scores.index(min(exp_scores))
    return load_prompt("prompt_b.txt").format(num_pulls=num_pulls, info=info, best=best, worst=worst)

print(get_prompt_b(10))