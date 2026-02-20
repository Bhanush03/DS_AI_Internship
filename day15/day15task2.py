import random

trials = 100000
count = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H" and die == 6:
        count += 1

print("Experimental Probability (Heads AND 6):", count / trials)