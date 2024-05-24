-- A script that lists all records of second_table

-- SQL query that lists all records of second table

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
