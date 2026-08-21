Select customer_name, count(distinct product) as unique_products
from orders 
group by customer_name
order by unique_products desc