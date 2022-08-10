SELECT p.firstname, p.lastname, a.city, a.state 
FROM Person p left join Address a 
ON p.personId = a.personId
