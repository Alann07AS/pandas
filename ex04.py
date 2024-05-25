import numpy as np
import pandas as pd

file = "iris.csv"

df = pd.read_csv(file)

df = df.drop("flower", axis=1)



# Fill missing values with different strategies for each column
df_filled = df.copy()

df_filled = df_filled.apply(pd.to_numeric, errors='coerce')

# Bonus question: Print the row with index 122
special_row = df_filled.loc[122]
print("Row with index 122:")
print(special_row)


df_filled.fillna({
    "sepal_length": df_filled["sepal_length"].mean(),
    "sepal_width": df_filled["sepal_width"].median(),
    "petal_length": 0,
    "petal_width": 0
}, inplace=True)

# Bonus question: Print the row with index 122
special_row = df_filled.loc[122]
print("Row with index 122:")
print(special_row)

# Bonus question: Check for negative and huge values
negative_values = df_filled[df_filled < 0].any().any()
huge_values = df_filled[df_filled > 100].any().any()
print("Negative values detected:", negative_values)
print("Huge values detected:", huge_values)
