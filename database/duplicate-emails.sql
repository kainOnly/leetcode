select Email from (
    select Email, count(*) as count from Person
    group by Email
) as v where v.count > 1;

select Email from Person
group by Email
having count(Email) > 1;