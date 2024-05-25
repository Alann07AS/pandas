import numpy as np
import pandas as pd

# data = np.genfromtxt("household_power_consumption.txt", delimiter=";", dtype=np.object_, max_rows=20)
dataframe = pd.read_csv("household_power_consumption.txt", sep=";", na_values='?', parse_dates=True, index_col="Date", date_format='%d/%m/%Y') #, index_col='Date'
print(dataframe.head().index)

def update_types(df):
    df.drop(["Time", "Sub_metering_2", "Sub_metering_3"], axis=1, inplace=True)
    return df
dataframe = update_types(dataframe)
print(dataframe.dtypes)

print(dataframe.describe())

print("NAN______",dataframe.isna().sum())
dataframe = dataframe.dropna()
print("NAN______",dataframe.isna().sum())


# Define a function to apply the calculation
def transform_function(value):
    return (value+1)*0.06

dataframe["Sub_metering_1"] = dataframe["Sub_metering_1"].apply(transform_function)
# print(dataframe)


dataframe_filtered = dataframe.loc[(dataframe.index>="2008-12-27") & (dataframe["Voltage"] >= 242)]
print(dataframe_filtered.count())

print(dataframe.iloc[88888])


print(dataframe["Global_active_power"].idxmax())

dataframe_sorting = dataframe.sort_values(["Global_active_power", "Voltage"], ascending=[False, True])
print(dataframe_sorting.tail())

daily_mean = dataframe.groupby(dataframe.index.date).mean()
print(daily_mean["Global_active_power"])