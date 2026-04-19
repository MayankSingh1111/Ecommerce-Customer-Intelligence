import pandas as pd
import os

# =========================
# LOAD DATA
# =========================
raw_path = r"E:\PROJECT\Ecommerce-Customer-Intelligence\DATA\RAW"

dataframes = {}

for file in os.listdir(raw_path):
    if file.endswith(".csv"):
        file_path = os.path.join(raw_path, file)

        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except:
            df = pd.read_csv(file_path, encoding='latin1')

        df_name = file.replace(".csv", "")
        dataframes[df_name] = df

        print(f"Loaded: {file} | Shape: {df.shape}")

print("\n All files loaded successfully!")

# =========================
# STANDARDIZE COLUMNS
# =========================
for name, df in dataframes.items():
    df.columns = df.columns.str.lower().str.strip()
    df.columns = df.columns.str.replace("coustomer_key", "customer_key")

# =========================
# ACCESS TABLES
# =========================
fact_df = dataframes["fact_table"]
customer_df = dataframes["customer_dim"]
item_df = dataframes["item_dim"]
store_df = dataframes["store_dim"]
time_df = dataframes["time_dim"]
trans_df = dataframes["Trans_dim"]

# =========================
# CHECK STRUCTURE
# =========================
for name, df in dataframes.items():
    print(f"\n{name}")
    print(df.info())

# =========================
# CHECK MISSING VALUES
# =========================
for name, df in dataframes.items():
    print(f"\n{name} missing values:\n{df.isnull().sum()}")

# =========================
# FIX DATA TYPES (KEEP AS STRING)
# =========================
for col in ['customer_key', 'payment_key', 'time_key', 'item_key', 'store_key']:
    if col in fact_df.columns:
        fact_df[col] = fact_df[col].astype(str)

customer_df['customer_key'] = customer_df['customer_key'].astype(str)
item_df['item_key'] = item_df['item_key'].astype(str)
store_df['store_key'] = store_df['store_key'].astype(str)
time_df['time_key'] = time_df['time_key'].astype(str)
trans_df['payment_key'] = trans_df['payment_key'].astype(str)

# =========================
# HANDLE MISSING VALUES (NO inplace)
# =========================
customer_df['name'] = customer_df['name'].fillna("Unknown")
fact_df['unit'] = fact_df['unit'].fillna("Unknown")
item_df['unit'] = item_df['unit'].fillna("Unknown")
trans_df['bank_name'] = trans_df['bank_name'].fillna("Unknown")

# =========================
# FIX DATE FORMAT
# =========================
time_df['date'] = pd.to_datetime(time_df['date'], dayfirst=True)

# =========================
# REMOVE DUPLICATES
# =========================
for name, df in dataframes.items():
    before = df.shape[0]
    df.drop_duplicates(inplace=True)
    after = df.shape[0]
    print(f"{name}: Removed {before - after} duplicates")

# =========================
# DUPLICATE COLUMNS BEFORE MERGE
# =========================
# Keep product pricing from item_dim (correct source)
fact_df = fact_df.drop(columns=['unit', 'unit_price'], errors='ignore')

# =========================
# MERGE DATA
# =========================
merged_df = fact_df \
    .merge(customer_df, on='customer_key') \
    .merge(item_df, on='item_key') \
    .merge(store_df, on='store_key') \
    .merge(time_df, on='time_key') \
    .merge(trans_df, on='payment_key')

# =========================
# SAVE CLEAN DATA
# =========================
output_path = r"E:\PROJECT\Ecommerce-Customer-Intelligence\data\processed\cleaned_data.csv"
merged_df.to_csv(output_path, index=False)

print("\nCleaned data saved successfully!")

# =========================
# FINAL VALIDATION
# =========================
print("\nFinal Data Types:\n", merged_df.dtypes)
print("\nFinal Shape:", merged_df.shape)