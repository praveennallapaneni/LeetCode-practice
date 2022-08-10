SELECT DISTINCT a.email as Email
FROM Person a join Person b
WHERE a.id != b.id AND a.email = b.email
