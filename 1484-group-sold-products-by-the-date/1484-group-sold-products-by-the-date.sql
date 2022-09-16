# Write your MySQL query statement below

select sell_date, count(DISTINCT(product)) as num_sold, 
GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') as products
from Activities
group by 1
order by 1
