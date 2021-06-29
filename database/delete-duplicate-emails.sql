delete N from Person as N, Person as O
where O.Email = N.Email and O.Id < N.Id