# Write your MySQL query statement below

#select product_id, store, price from Products where
SELECT product_id,store,price 
FROM
(
SELECT product_id, store1 AS price,'store1' AS store, 1 AS Ord
FROM Products
UNION ALL
SELECT product_id, store2 AS price,'store2' AS store, 2 AS Ord
FROM Products
UNION ALL
SELECT product_id, store3 AS price,'store3' AS store, 3 AS Ord
FROM Products
)t
where price <> 0
ORDER BY product_id,Ord