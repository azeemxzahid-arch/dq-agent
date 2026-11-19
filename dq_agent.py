import pandas as pd
df = pd.read_csv("data/transaction_messy.csv")
print("row and columns:",df.shape)
print("Missing Values per column:")
print(df.isnull().sum())
print("Extra Duplicated Rows:", df.duplicated().sum())
print ("Repeated transaction IDs:")
print(df["transaction_id"].value_counts())
amount_before = int(df["amount"].isnull().sum())
amount_num = pd.to_numeric(df["amount"], errors ="coerce")
amount_after = int(amount_num.isnull().sum())
print(f"Amounts missing at load: {amount_before}")
print(f"Amounts NaN after to_numeric: {amount_after}")
print("Amounts killed by coercion:",
    df.loc[amount_num.isnull() & df["amount"].notnull(),
           "transaction_id"].tolist())
dates_parsed = pd.to_datetime(df["txn_date"], errors ="coerce", format = "mixed")
print("Bad dates:",
      df.loc[dates_parsed.isnull(), ["transaction_id", "txn_date"]].values.tolist())           
# --- Session 5: rule checks ---
# Rule 1: amount must be > 0 (checked on the coerced numbers from S4)
neg = df.loc[amount_num <= 0, ["transaction_id", "amount"]]
print(f"Rule 1 - amount not positive: {len(neg)}")
print(neg.values.tolist())

# Rule 2: status must be one of the allowed values
bad_status = df.loc[~df["status"].isin(["Completed", "Pending", "Failed"]),
                    ["transaction_id", "status"]]
print(f"Rule 2 - bad status: {len(bad_status)}")
print(bad_status.values.tolist())

# Rule 3: currency must be CAD or USD
bad_curr = df.loc[~df["currency"].isin(["CAD", "USD"]),
                  ["transaction_id", "currency"]]
print(f"Rule 3 - bad currency: {len(bad_curr)}")
print(bad_curr.values.tolist())
