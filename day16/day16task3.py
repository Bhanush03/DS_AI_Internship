import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ----- Original skewed dataset (dice rolls 1–6) -----
population = np.random.randint(1, 7, size=100000)

# ----- Take 1000 samples of size 30 -----
sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())

# ----- Plot histogram of sample means -----
plt.hist(sample_means, bins=30, density=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()