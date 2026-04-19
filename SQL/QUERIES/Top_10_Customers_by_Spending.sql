-- Top 10 Customers by Spending

SELECT TOP 10
    c.name,
    SUM(f.total_price) AS total_spent
FROM fact_table f
JOIN customer_dim c ON f.customer_key = c.customer_key
GROUP BY c.name
ORDER BY total_spent DESC;