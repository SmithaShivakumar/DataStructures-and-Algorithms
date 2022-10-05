# Write your MySQL query statement below

select c.customer_id, c.customer_name
from Customers c
join Orders o
on o.customer_id = c.customer_id
group by c.customer_id
having sum(o.product_name="A") >0 and sum(o.product_name="B") > 0 and sum(o.product_name="C")=0