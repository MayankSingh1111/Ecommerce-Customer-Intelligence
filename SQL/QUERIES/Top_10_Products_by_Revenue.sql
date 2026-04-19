-- Top 10 Products by Revenue

SELECT TOP 10
    i.item_name,
    SUM(f.total_price) AS revenue
FROM fact_table f
JOIN item_dim i ON f.item_key = i.item_key
GROUP BY i.item_name
ORDER BY revenue DESC;