-- Monthly Revenue Trend

SELECT 
    t.year,
    t.month,
    SUM(f.total_price) AS revenue
FROM fact_table f
JOIN time_dim t ON f.time_key = t.time_key
GROUP BY t.year, t.month
ORDER BY t.year, t.month;