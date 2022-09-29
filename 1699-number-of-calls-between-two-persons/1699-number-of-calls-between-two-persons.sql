# Write your MySQL query statement below
WITH caller as (
    select from_id as person1, to_id as person2, duration
    from Calls
    UNION ALL
    select to_id as person1, from_id as person2, duration
    from Calls
),

unique_caller as (
    select person1, person2, duration
    from caller
    where person1 < person2
)

select
    person1, person2, count(*) as call_count, sum(duration) as total_duration
from unique_caller
group by person1, person2