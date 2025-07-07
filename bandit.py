import random

ARMS = [ # generate a random number from 0 to 1. if it's less than the first number, give the reward in the second number.
    {1: 2}, # always give 2 reward
    {0.75: 0, 1: 12}, # 75% chance of giving 0 reward, 25% chance of giving 12 reward
    {0.3: 1, 1: 3}, # 30% chance of giving 1 reward, 70% chance of giving 3 reward
    {0.9: 0, 1: 15}, # 90% chance of giving 0 reward, 10% chance of giving 15 reward
]

def n_armed_bandit(choice):
    spin = random.random()
    for option in sorted(ARMS[choice].keys()):
        if spin < option:
            return ARMS[choice][option]
    return 0