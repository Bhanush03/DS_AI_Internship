import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_feature_dataset_500.csv")

plt.figure()
plt.scatter(df["SquareFootage"], df["Price"])
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

plt.figure()
sns.boxplot(x="Location", y="Price", data=df)
plt.title("Price Distribution by Location")
plt.show()

print("Observation: As SquareFootage increases, Price generally increases.")
