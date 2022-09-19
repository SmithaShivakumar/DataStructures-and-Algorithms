# Write your MySQL query statement below
select w.id 
from Weather w
join Weather we
ON DATEDIFF(w.recordDate, we.recordDate) = 1
        AND w.Temperature > we.Temperature
