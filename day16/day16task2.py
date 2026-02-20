import numpy as np
import pandas as pd

# ----- Create / load dataset -----
np.random.seed(42)

# Example dataset (Normal + some extreme values)
data = np.random.normal(loc=50, scale=10, size=1000)
data = np.append(data, [120, 130, -10])  # add outliers

df = pd.DataFrame({"values": data})

# ----- Mean and Standard Deviation -----
mu = df["values"].mean()
sigma = df["values"].std()

print("Mean (mu):", mu)
print("Std Dev (sigma):", sigma)

# ----- Z-score calculation -----
df["z_score"] = (df["values"] - mu) / sigma

# ----- Identify outliers -----
outliers = df[abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)