# Write your MySQL query statement below

select sale_date,
 SUM(IF(fruit = "oranges", -sold_num, sold_num)) as diff
FROM Sales
group by sale_date
order by sale_date