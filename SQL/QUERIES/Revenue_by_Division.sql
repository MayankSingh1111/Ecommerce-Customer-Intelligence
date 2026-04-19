-- revenue by division

SELECT 
    s.division,
    SUM(f.total_price) AS revenue
FROM fact_table f
JOIN store_dim s ON f.store_key = s.store_key
GROUP BY s.division
ORDER BY revenue DESC;