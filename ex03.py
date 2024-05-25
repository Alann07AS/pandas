import numpy as np
import pandas as pd

file = "Ecommerce_purchases.txt"

df = pd.read_csv(file, parse_dates=True, date_format="%m/%y")

print(df.dtypes)

print("\nHow many rows and columns are there?")
print("Rows:", df.shape[0], "Columns:", df.shape[1])

print("\nWhat is the average Purchase Price?")
print(df["Purchase Price"].mean())

print("\nWhat were the highest and lowest purchase prices?")
print("Highest:", df["Purchase Price"].max(), "Lowest:", df["Purchase Price"].min())

print("\nHow many people have English 'en' as their Language of choice on the website?")
print(df["Language"][df["Language"] == "en"].count())

print("\nHow many people have the job title of 'Lawyer' ?")
print(df["Job"][df["Job"] == "Lawyer"].count())

print("\nHow many people made the purchase during the AM and how many people made the purchase during PM ?")
print("AM:", df["AM or PM"][df["AM or PM"] == "AM"].count()) # methode count
print("PM:", (df["AM or PM"] == "PM").sum())                 # methode sum


print("\nWhat are the 5 most common Job Titles?")
print((df["Job"].value_counts()[:5]))


print("\nSomeone made a purchase that came from Lot: '90 WT' , what was the Purchase Price for this transaction?")
print(df.loc[df["Lot"] == '90 WT', "Purchase Price"].values[0]) #?


print("\nWhat is the email of the person with the following Credit Card Number: 4926535242672853")
print(df.loc[df["Credit Card"] == 4926535242672853,"Email"].values[0])

print("\nHow many people have American Express as their Credit Card Provider and made a purchase above $95 ?")
print(df["Job"][(df["CC Provider"] == "American Express") & (df["Purchase Price"]>= 95)].count())

print("\nHow many people have a credit card that expires in 2025?")
# df["CC Exp Date"] = pd.to_datetime(df["CC Exp Date"], format="%m/%y")
df["CC Exp Date"] = pd.to_datetime(df["CC Exp Date"], format="%m/%y")
print(df.loc[df["CC Exp Date"].dt.year == 2025, "CC Exp Date"].count())

print("\nWhat are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)")
print(df["Email"].apply(lambda x: x.split("@")[1]).value_counts()[:5])
