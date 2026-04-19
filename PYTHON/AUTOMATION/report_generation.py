import pandas as pd
import os
from sqlalchemy import create_engine

# =========================
# 1️⃣ DB CONNECTION
# =========================
engine = create_engine(
    "mssql+pyodbc://@Raghav\\SQLEXPRESS/Ecommerce?driver=ODBC+Driver+17+for+SQL+Server"
)

# =========================
# 2️⃣ PATHS
# =========================
query_folder = r"E:\PROJECT\Ecommerce-Customer-Intelligence\SQL\QUERIES"
output_csv_folder = r"E:\PROJECT\Ecommerce-Customer-Intelligence\OUTPUT\SQL_RESULT"
output_excel = r"E:\PROJECT\Ecommerce-Customer-Intelligence\OUTPUT\REPORTS\reports.xlsx"

os.makedirs(output_csv_folder, exist_ok=True)

# =========================
# 3️⃣ READ + EXECUTE QUERIES
# =========================
results = {}

for file in os.listdir(query_folder):
    if file.endswith(".sql"):
        
        file_path = os.path.join(query_folder, file)
        
        with open(file_path, "r") as f:
            query = f.read()
        
        print(f"Running: {file}")
        
        df = pd.read_sql(query, engine)
        
        # Remove .sql extension
        name = file.replace(".sql", "")
        
        # Save CSV
        csv_path = os.path.join(output_csv_folder, f"{name}.csv")
        df.to_csv(csv_path, index=False)
        
        print(f"✅ Saved CSV: {name}")
        
        # Store for Excel
        results[name] = df

# =========================
# 4️⃣ EXPORT TO EXCEL (MULTI-SHEET)
# =========================
with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
    for sheet_name, df in results.items():
        df.to_excel(writer, sheet_name=sheet_name[:31], index=False)

print("\n🚀 All queries executed & exported successfully!")