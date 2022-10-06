# Write your MySQL query statement below

select d.dept_name, COUNT(s.student_id) as student_number
from Department d
left outer join Student s
on d.dept_id = s.dept_id
group by d.dept_name
ORDER BY student_number DESC , d.dept_name
