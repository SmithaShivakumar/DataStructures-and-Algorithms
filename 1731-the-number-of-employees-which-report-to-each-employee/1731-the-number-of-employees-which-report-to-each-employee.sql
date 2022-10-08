# Write your MySQL query statement below

select a.employee_id, a.name, 
COUNT(b.reports_to) as reports_count, ROUND(AVG(b.age),0) as average_age
from Employees a join Employees b
on a.employee_id = b.reports_to
group by b.reports_to
order by b.reports_to

