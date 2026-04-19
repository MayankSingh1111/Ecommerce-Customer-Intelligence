-- Running Revenue (Cumulative Growth)


SELECT 
    t.year,
    t.month,
    SUM(f.total_price) AS monthly_revenue,
    SUM(SUM(f.total_price)) OVER (ORDER BY t.year, t.month) AS running_total
FROM fact_table f
JOIN time_dim t ON f.time_key = t.time_key
GROUP BY t.year, t.month
ORDER BY t.year, t.month;