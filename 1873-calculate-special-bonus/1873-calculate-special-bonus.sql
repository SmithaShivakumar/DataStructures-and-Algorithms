# Write your MySQL query statement below
select employee_id, 
CASE 
    WHEN ((employee_id % 2) = 0 ) THEN 0
    WHEN (SUBSTRING(name, 1, 1) = 'M') THEN 0
    ELSE salary
END as bonus
from Employees 
ORDER BY employee_id