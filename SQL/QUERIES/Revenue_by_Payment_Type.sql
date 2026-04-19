-- Revenue by Payment Type

SELECT 
    t.trans_type,
    SUM(f.total_price) AS revenue
FROM fact_table f
JOIN trans_dim t ON f.payment_key = t.payment_key
GROUP BY t.trans_type;