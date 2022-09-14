# Write your MySQL query statement below
select name as Customers from Customers C where 
C.id not in (select customerId from Orders O join Customers C where O.customerId = C.id )