import numpy as np
import pandas as pd

# Create DataFrame from NumPy array
data_array = np.array([
    ["Blue", [1, 2], 1.1],
    ["Red", [3, 4], 2.2],
    ["Pink", [5, 6], 3.3],
    ["Grey", [7, 8], 4.4],
    ["Black", [9, 10], 5.5]
], dtype=object)

df_from_array = pd.DataFrame(data_array, columns=['color', 'list', 'number'], index=[1, 3, 5, 7, 9])

# Print the DataFrames
print("DataFrame created from NumPy array:")
print(df_from_array)

# Create DataFrame from Pandas Series
data_series = {
    'color': pd.Series(['Blue', 'Red', 'Pink', 'Grey', 'Black'], index=[1, 3, 5, 7, 9]),
    'list': pd.Series([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], index=[1, 3, 5, 7, 9]),
    'number': pd.Series([1.1, 2.2, 3.3, 4.4, 5.5], index=[1, 3, 5, 7, 9])
}

df_from_series = pd.DataFrame(data_series)

# Print the DataFrames from Pandas Serie
print("DataFrame created from NumPy array:")
print(df_from_series)

# Print the types for every column and the types of the first value of every column
print("\nTypes for every column:")
print(df_from_series.dtypes)

print("\nTypes of the first value of every column:")
print(df_from_series.iloc[0].apply(type))
