# Write your MySQL query statement below

select seller_name
from seller s
left join (select seller_id, customer_id
          from orders
          where year(sale_date)=2020) o
using(seller_id)
where o.customer_id is null
order by 1


