import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

np.random.seed(42)

X = np.linspace(-10, 10, 200)
y = 3 * X**2 + 2 * X + 5 + np.random.normal(0, 20, 200)

df = pd.DataFrame({"Feature": X, "Target": y})

X = df[["Feature"]]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_pred_poly = poly_model.predict(X_poly_test)
r2_poly = r2_score(y_test, y_pred_poly)

print("R² Score (Linear Model):", r2_linear)
print("R² Score (Polynomial Model):", r2_poly)
