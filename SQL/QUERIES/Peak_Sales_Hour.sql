-- Peak Sales Hour

SELECT TOP 1
    t.hour,
    SUM(f.total_price) AS revenue
FROM fact_table f
JOIN time_dim t ON f.time_key = t.time_key
GROUP BY t.hour
ORDER BY revenue DESC;