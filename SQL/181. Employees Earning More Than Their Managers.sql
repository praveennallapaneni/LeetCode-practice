SELECT a.Name as Employee
FROM Employee a JOIN Employee b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary
