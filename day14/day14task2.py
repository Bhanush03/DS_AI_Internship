import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

np.random.seed(42)

age = np.random.randint(20, 60, 200)
salary = np.random.randint(20000, 150000, 200)

df = pd.DataFrame({
    "Age": age,
    "Salary": salary
})

standard_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

plt.figure()
plt.hist(df["Salary"], bins=20)
plt.title("Salary Before Scaling")
plt.show()

plt.figure()
plt.hist(df_standardized["Salary"], bins=20)
plt.title("Salary After Standardization")
plt.show()

plt.figure()
plt.hist(df_normalized["Salary"], bins=20)
plt.title("Salary After Normalization")
plt.show()
