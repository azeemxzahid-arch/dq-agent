import pandas as pd
df = pd.read_csv("data/transaction_messy.csv")
print("row and columns:",df.shape)
print("Missing Values per column:")
print(df.isnull().sum())
print("Extra Duplicated Rows:", df.duplicated().sum())
print ("Repeated transaction IDs:")
print(df["transaction_id"].value_counts())
