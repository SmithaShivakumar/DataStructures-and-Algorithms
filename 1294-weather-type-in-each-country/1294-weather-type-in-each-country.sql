# Write your MySQL query statement below
select c.country_name,
    CASE
    WHEN AVG(weather_state)<= 15 THEN 'Cold'
    WHEN AVG(weather_state) >= 25 THEN 'Hot' 
    ELSE 'Warm' END as weather_type
from Countries c
join Weather w
on c.country_id = w.country_id
WHERE w.day BETWEEN "2019-11-01" AND "2019-11-30"
group by w.country_id
order by weather_type

