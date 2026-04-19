-- Monthly Growth % (VERY IMP)

WITH monthly_sales AS (
    SELECT 
        t.year,
        t.month,
        SUM(f.total_price) AS revenue
    FROM fact_table f
    JOIN time_dim t ON f.time_key = t.time_key
    GROUP BY t.year, t.month
)
SELECT 
    *,
    LAG(revenue) OVER (ORDER BY year, month) AS prev_month,
    ((revenue - LAG(revenue) OVER (ORDER BY year, month)) * 100.0 
        / LAG(revenue) OVER (ORDER BY year, month)) AS growth_percent
FROM monthly_sales;