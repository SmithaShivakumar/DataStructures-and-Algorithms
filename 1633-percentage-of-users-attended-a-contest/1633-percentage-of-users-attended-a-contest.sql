# Write your MySQL query statement below

select contest_id, 
ROUND((100*COUNT(DISTINCT user_id))/(SELECT COUNT(*) from Users),2) as percentage 
from Register
group by contest_id
order by percentage DESC, contest_id ASC