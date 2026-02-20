import random

trials = 1000
count = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count += 1

experimental_probability = count / trials

print("Number of times sum = 7:", count)
print("Experimental Probability:", experimental_probability)