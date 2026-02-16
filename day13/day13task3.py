import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_feature_dataset_500.csv")

plt.figure()
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()

high_corr = corr_matrix[abs(corr_matrix) > 0.8]
print("Highly Correlated Variables (>|0.8|):")
print(high_corr)

plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price (Outlier Detection)")
plt.show()
