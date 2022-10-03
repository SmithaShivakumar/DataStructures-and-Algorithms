# Write your MySQL query statement below
select ROUND(100*(((SELECT COUNT(delivery_id) from Delivery where customer_pref_delivery_date = order_date))/COUNT(*)),2) as immediate_percentage
from Delivery
