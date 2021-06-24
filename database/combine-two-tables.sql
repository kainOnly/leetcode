Select p.FirstName,p.LastName,a.City,a.State
from Person as p
Left join Address as a
on p.PersonId=a.PersonId