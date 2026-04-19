-- Customer Segmentation (VIP/Regular/Repeat Customers - Retention Logic)

SELECT 
    customer_key,
    COUNT(*) AS orders_count
FROM fact_table
GROUP BY customer_key
HAVING COUNT(*) > 1;