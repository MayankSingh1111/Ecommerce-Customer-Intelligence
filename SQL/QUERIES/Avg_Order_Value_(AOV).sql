-- Avereage Order Value (AOV) 

SELECT 
    SUM(total_price) / COUNT(*) AS avg_order_value
FROM fact_table;

