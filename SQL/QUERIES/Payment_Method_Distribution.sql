-- Payment Method Distribution

SELECT 
    t.trans_type,
    COUNT(*) AS transactions
FROM fact_table f
JOIN trans_dim t ON f.payment_key = t.payment_key
GROUP BY t.trans_type