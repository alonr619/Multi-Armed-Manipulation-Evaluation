import random
from config import ARMS

def n_armed_bandit(choice: int) -> float:
    spin = random.random()
    for option in sorted(ARMS[choice].keys()):
        if spin < option:
            return ARMS[choice][option]
    return 0