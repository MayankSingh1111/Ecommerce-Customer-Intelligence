-- Top Selling Products (by Quantity)

SELECT TOP 10
    i.item_name,
    SUM(f.quantity) AS total_quantity
FROM fact_table f
JOIN item_dim i ON f.item_key = i.item_key
GROUP BY i.item_name
ORDER BY total_quantity DESC;