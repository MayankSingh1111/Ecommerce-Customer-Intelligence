import pandas as pd
from sqlalchemy import create_engine, text

# =========================
# 1️⃣ DB CONNECTION
# =========================
engine = create_engine(
    "mssql+pyodbc://@Raghav\\SQLEXPRESS/Ecommerce?driver=ODBC+Driver+17+for+SQL+Server"
)

# =========================
# 2️⃣ FILE PATH
# =========================
base_path = r"E:\PROJECT\Ecommerce-Customer-Intelligence\DATA\RAW"

# =========================
# 3️⃣ LOAD CSV FILES
# =========================
customer_df = pd.read_csv(f"{base_path}\\customer_dim.csv", encoding='latin1')
item_df = pd.read_csv(f"{base_path}\\item_dim.csv", encoding='latin1')
store_df = pd.read_csv(f"{base_path}\\store_dim.csv", encoding='latin1')
time_df = pd.read_csv(f"{base_path}\\time_dim.csv", encoding='latin1')
trans_df = pd.read_csv(f"{base_path}\\Trans_dim.csv", encoding='latin1')
fact_df = pd.read_csv(f"{base_path}\\fact_table.csv", encoding='latin1')

# =========================
# 4️⃣ CLEANING
# =========================

# Standardize column names
for df in [customer_df, item_df, store_df, time_df, trans_df, fact_df]:
    df.columns = df.columns.str.lower().str.strip()
    df.columns = df.columns.str.replace("coustomer_key", "customer_key")

# Fix customer data
customer_df['contact_no'] = customer_df['contact_no'].astype(str)
customer_df['nid'] = customer_df['nid'].astype(str)

# Fix item table
item_df.rename(columns={"desc": "description"}, inplace=True)

# Fix time table
time_df['date'] = pd.to_datetime(time_df['date'], dayfirst=True)
time_df.rename(columns={'date': 'full_date'}, inplace=True)
time_df['week'] = time_df['week'].str.extract(r'(\d+)').astype(int)
time_df['quarter'] = time_df['quarter'].str.replace('Q', '').astype(int)

# Fix trans table
trans_df['bank_name'] = trans_df['bank_name'].replace("None", None)

# =========================
# 5️⃣ REMOVE DUPLICATES
# =========================
customer_df.drop_duplicates(subset=['customer_key'], inplace=True)
item_df.drop_duplicates(subset=['item_key'], inplace=True)
store_df.drop_duplicates(subset=['store_key'], inplace=True)
time_df.drop_duplicates(subset=['time_key'], inplace=True)
trans_df.drop_duplicates(subset=['payment_key'], inplace=True)

# =========================
# 6️⃣ FIX FACT TABLE (IMPORTANT)
# =========================
# Remove columns not in SQL schema
fact_df = fact_df.drop(columns=['unit', 'unit_price'], errors='ignore')

# =========================
# 7️⃣ TRUNCATE TABLES
# =========================
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE fact_table"))
    conn.execute(text("TRUNCATE TABLE customer_dim"))
    conn.execute(text("TRUNCATE TABLE item_dim"))
    conn.execute(text("TRUNCATE TABLE store_dim"))
    conn.execute(text("TRUNCATE TABLE time_dim"))
    conn.execute(text("TRUNCATE TABLE trans_dim"))

print("🧹 Tables truncated")

print("Customer:", customer_df.shape)
print("Item:", item_df.shape)
print("Store:", store_df.shape)
print("Time:", time_df.shape)
print("Trans:", trans_df.shape)
print("Fact:", fact_df.shape)

# =========================
# 8️⃣ LOAD DATA (ORDER MATTERS)
# =========================

customer_df.to_sql("customer_dim", con=engine, if_exists="append", index=False)
print("✅ customer_dim loaded")

item_df.to_sql("item_dim", con=engine, if_exists="append", index=False)
print("✅ item_dim loaded")

store_df.to_sql("store_dim", con=engine, if_exists="append", index=False)
print("✅ store_dim loaded")

time_df.to_sql("time_dim", con=engine, if_exists="append", index=False)
print("✅ time_dim loaded")

trans_df.to_sql("trans_dim", con=engine, if_exists="append", index=False)
print("✅ trans_dim loaded")

fact_df.to_sql("fact_table", con=engine, if_exists="append", index=False)
print("✅ fact_table loaded")

# =========================
# 9️⃣ FINAL STATUS
# =========================
print("\n🚀 ALL DATA LOADED SUCCESSFULLY!")