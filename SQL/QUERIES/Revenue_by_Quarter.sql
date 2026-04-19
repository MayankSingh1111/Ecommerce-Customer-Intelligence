-- Revenue by Quarter

SELECT 
    t.year,
    t.quarter,
    SUM(f.total_price) AS revenue
FROM fact_table f
JOIN time_dim t ON f.time_key = t.time_key
GROUP BY t.year, t.quarter
ORDER BY t.year, t.quarter;