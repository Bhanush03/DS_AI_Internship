import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----- Generate datasets -----
np.random.seed(42)

# 1) Normal distribution (Heights)
heights = np.random.normal(loc=170, scale=7, size=1000)

# 2) Right-skewed distribution (Incomes)
incomes = np.random.exponential(scale=50000, size=1000)

# 3) Left-skewed distribution (Easy exam scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Put into DataFrame
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

# ----- Function to plot Histogram + KDE -----
def plot_hist_kde(data, title):
    data.plot(kind="hist", bins=30, density=True, alpha=0.6)
    data.plot(kind="kde")
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()

# ----- Plot each dataset -----
plot_hist_kde(df["Heights"], "Normal Distribution (Heights)")
plot_hist_kde(df["Incomes"], "Right-Skewed Distribution (Incomes)")
plot_hist_kde(df["Scores"], "Left-Skewed Distribution (Scores)")

# ----- Mean vs Median -----
for col in df.columns:
    mean = df[col].mean()
    median = df[col].median()
    print(f"{col} -> Mean: {mean:.2f}, Median: {median:.2f}")