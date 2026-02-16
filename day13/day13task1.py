import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

df = pd.read_csv("housing_dataset_500.csv")

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Histogram of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

price_skewness = skew(df["Price"])
price_kurtosis = kurtosis(df["Price"])

print("Skewness:", price_skewness)
print("Kurtosis:", price_kurtosis)

plt.figure()
sns.countplot(x=df["City"])
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()
