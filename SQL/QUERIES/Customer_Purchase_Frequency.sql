-- customer purchase frequency

SELECT 
    customer_key,
    COUNT(*) AS orders_count
FROM fact_table
GROUP BY customer_key
ORDER BY orders_count DESC;