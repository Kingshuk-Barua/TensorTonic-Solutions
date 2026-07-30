-- Write your SQL query here
Select product_name as name, category, (unit_price*units_in_stock) as inventory_value from products;