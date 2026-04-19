-- top product per category using row_number

SELECT *
FROM (
    SELECT 
        i.item_name,
        SUM(f.total_price) AS revenue,
        ROW_NUMBER() OVER (ORDER BY SUM(f.total_price) DESC) AS rn
    FROM fact_table f
    JOIN item_dim i ON f.item_key = i.item_key
    GROUP BY i.item_name
) t
WHERE rn <= 5;