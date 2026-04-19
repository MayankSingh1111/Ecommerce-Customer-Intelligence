-- First Purchase vs Latest Purchase

SELECT 
    f.customer_key,
    MIN(t.full_date) AS first_purchase,
    MAX(t.full_date) AS last_purchase
FROM fact_table f
JOIN time_dim t ON f.time_key = t.time_key
GROUP BY f.customer_key;