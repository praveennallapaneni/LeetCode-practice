SELECT a.id AS Id
FROM Weather a JOIN Weather b
WHERE a.temperature > b.temperature AND DATEDIFF(a.recordDate,b.recordDate) = 1
