# Write your MySQL query statement below
select
distinct a.account_id
from LogInfo a, LogInfo b
where a.login between (b.login) and (b.logout)
and a.account_id = b.account_id
and a.ip_address !=b.ip_address