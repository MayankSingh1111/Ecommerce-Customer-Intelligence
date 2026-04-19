# 📊 E-Commerce Customer Intelligence System

An end-to-end **Data Analytics Project** demonstrating a real-world workflow — from raw data ingestion to business insights using **SQL, Python, and Power BI**.

---

## 🚀 Project Overview

This project simulates a complete **data analytics pipeline**:

* 📥 Data ingestion from raw CSV files
* 🧹 Data cleaning and transformation using Python
* 🗄️ Data storage and querying using SQL Server
* ⚙️ Automated report generation using Python
* 📓 Exploratory Data Analysis (EDA) using Jupyter
* 📊 Interactive dashboard using Power BI

---

## 🛠️ Tech Stack

* **Python** → Pandas, Matplotlib, SQLAlchemy
* **SQL Server** → Joins, Aggregations, Window Functions
* **Power BI** → Dashboard, DAX, Data Modeling
* **Jupyter Notebook** → EDA & Visualization

---

## 📂 Project Structure

```
Ecommerce-Customer-Intelligence/
│
├── DATA/
│   ├── RAW/
│   │   ├── customer_dim.csv
│   │   ├── fact_table.csv
│   │   ├── item_dim.csv
│   │   ├── store_dim.csv
│   │   ├── time_dim.csv
│   │   └── Trans_dim.csv
│   │
│   └── PROCESSED/
│       └── cleaned_data.csv
│
├── OUTPUT/
│   ├── CHARTS/
│   │   ├── Customer Segmentation.png
│   │   ├── Ecommerce_Dashboard.pdf
│   │   ├── Payment Method Distribution.png
│   │   ├── Peak Sales Hour.png
│   │   ├── Revenue_Trend.png
│   │   ├── Sale By Region.png
│   │   ├── Top Customers.png
│   │   └── Top Products.png
│   │
│   ├── REPORTS/
│   │   └── reports.xlsx
│   │
│   └── SQL_RESULT/
│       ├── Avg_Order_Value_(AOV).csv
│       ├── BASIC_BUSINESS_METRICS.csv
│       ├── Best_Performing_Region.csv
│       ├── Customer_Purchase_Frequency.csv
│       ├── First_Purchase_vs_Latest_Purchase.csv
│       ├── Monthly_Growth_%.csv
│       ├── Monthly_Revenue_Trend.csv
│       ├── Payment_Method_Distribution.csv
│       ├── Peak_Sales_Hour.csv
│       ├── Repeat_Customers.csv
│       ├── Revenue_by_Division.csv
│       ├── Revenue_by_Payment_Type.csv
│       ├── Revenue_by_Quarter.csv
│       ├── Running_Revenue.csv
│       ├── Top_10_Customers_by_Spending.csv
│       ├── Top_10_Products_by_Revenue.csv
│       ├── Top_Customers_(RANK).csv
│       └── Top_Product_per_Category.csv
│
├── POWERBI/
│   └── Ecommerce_Dashboard.pbix
│
├── PYTHON/
│   ├── data_cleaning.py
│   ├── EDA_Analysis.ipynb
│   │
│   └── AUTOMATION/
│       ├── load_to_sql.py
│       └── report_generation.py
│
├── SQL/
│   ├── SCHEMA/
│   │   └── create_tables.sql
│   │
│   └── QUERIES/
│       ├── BASIC_BUSINESS_METRICS.sql
│       ├── Monthly_Revenue_Trend.sql
│       ├── Peak_Sales_Hour.sql
│       ├── Top_Products.sql
│       └── ...
│
├── DOC/
│   └── Project_Summary.pdf
│
└── README.md
```

---

## 📊 Power BI Dashboard

The dashboard provides a **comprehensive business overview and customer insights**.

### 🔹 Page 1: Business Overview

* Total Revenue, Orders, Customers, AOV
* Monthly Revenue Trend
* Top Products by Revenue
* Revenue by Region

### 🔹 Page 2: Customer & Behavior

* Top Customers by Spending
* Customer Segmentation (VIP / Regular / Low)
* Payment Method Distribution
* Peak Sales Hour

📄 Dashboard Preview available at:
`OUTPUT/CHARTS/Ecommerce_Dashboard.pdf`

---

## 📈 Key Insights

* Revenue shows consistent growth over time
* A small group of products contributes most of the revenue (Pareto effect)
* Business is highly dependent on VIP customers
* Digital payments dominate transactions
* Sales peak during specific hours
* Regional performance varies significantly

---

## ⚙️ Automation Pipeline

* Reads SQL queries dynamically from folder
* Executes queries on SQL Server
* Exports results to:

  * CSV files (`/OUTPUT/SQL_RESULT`)
  * Excel report (`/OUTPUT/REPORTS`)

---
## 📦 Dataset & Reproducibility

Due to GitHub file size limitations, the full dataset is not included in this repository.

### 🔹 How to Generate the Dataset

The cleaned dataset is generated through the data pipeline.

Run the following script:

```bash
python PYTHON/data_cleaning.py
```

This will automatically:

* Read raw data from `DATA/RAW/`
* Clean and transform the data
* Generate the processed dataset at:

```
DATA/PROCESSED/cleaned_data.csv
```

> If the `PROCESSED` folder does not exist, it will be created automatically by the script.

---

### 🔹 Note

* The dataset is reproducible using the provided scripts
* This ensures a lightweight repository and follows industry best practices
* All analysis and dashboards are built on the generated dataset

---

## 📓 Exploratory Data Analysis (EDA)

Performed using **Jupyter Notebook**:

* Revenue trend analysis
* Customer segmentation
* Product performance
* Payment behavior analysis

📊 Charts exported to:
`OUTPUT/CHARTS/`

---

## 🧠 Business Value

* Identifies high-value customers and products
* Supports data-driven decision-making
* Enables marketing and retention strategies
* Provides scalable analytics pipeline

---

## 🎯 Conclusion

This project demonstrates a complete **end-to-end data analytics workflow**, integrating SQL, Python, and Power BI to generate actionable business insights from raw data.

---

## 📌 Author

**Maynak Singh**
Data Analyst | SQL • Python • Power BI

---
