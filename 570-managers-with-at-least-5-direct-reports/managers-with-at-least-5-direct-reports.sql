# Write your MySQL query statement below
select b.name from 
Employee as a 
inner join Employee as b
where a.managerId=b.id
group by b.id
having count(*) >=5;