import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

laptop_price = products['Laptop']
first_two = products[0:2]

print(products)
print(laptop_price)
print(first_two)
