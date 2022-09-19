# Write your MySQL query statement below
Select id as `Id`, 
CASE 
WHEN tree.id = (SELECT a.id from tree a where a.p_id is null) THEN 'Root'
WHEN tree.id  in (select b.p_id from tree b ) THEN 'Inner'
ELSE 'Leaf'    
 end as type
from Tree tree
order by `Id`

