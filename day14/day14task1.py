import pandas as pd   # Import pandas library for data handling

# Create a sample dataset using a dictionary
data = {
    'Transmission': ['Automatic', 'Manual', 'Manual', 'Automatic'],  # Binary categorical column
    'Color': ['Red', 'Blue', 'Green', 'Red']  # Nominal categorical column
}

# Convert dictionary into a DataFrame (table format)
df = pd.DataFrame(data)

# Apply Label Encoding using .map()
# Convert Transmission text values into numeric values
# Automatic → 0, Manual → 1
df['Transmission'] = df['Transmission'].map({'Automatic': 0, 'Manual': 1})

# Apply One-Hot Encoding to the Color column
# Creates separate binary columns for each color
# drop_first=True avoids dummy variable trap (multicollinearity)
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

# Display the final transformed dataset
print(df)
