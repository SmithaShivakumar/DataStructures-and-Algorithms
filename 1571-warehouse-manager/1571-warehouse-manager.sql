# Write your MySQL query statement below

with temporaryTable (product_id, V) as 
    (select product_id, (Width*Length*Height) as V from Products group by  product_id)
    select name as warehouse_name, sum(V*W.units) as volume 
    from Warehouse W, temporaryTable P 
    where P.product_id = W.product_id 
    group by W.name  




