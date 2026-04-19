-- Total Revenuen & Orders & Customers --

select sum(total_price) as Total_revenue,
       count(*) as Total_Orders,
       count(distinct customer_key) as Total_Customers
from fact_table;