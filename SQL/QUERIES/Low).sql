-- Customer Segmentation (VIP/Regular/Low)

SELECT 
    customer_key,
    SUM(total_price) AS total_spent,
    CASE 
        WHEN SUM(total_price) > 10000 THEN 'VIP'
        WHEN SUM(total_price) BETWEEN 5000 AND 10000 THEN 'Regular'
        ELSE 'Low'
    END AS customer_segment
FROM fact_table
GROUP BY customer_key;