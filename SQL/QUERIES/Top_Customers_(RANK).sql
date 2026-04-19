-- Top Customers (RANK)

SELECT 
    c.name,
    SUM(f.total_price) AS total_spent,
    RANK() OVER (ORDER BY SUM(f.total_price) DESC) AS rank_no
FROM fact_table f
JOIN customer_dim c ON f.customer_key = c.customer_key
GROUP BY c.name;