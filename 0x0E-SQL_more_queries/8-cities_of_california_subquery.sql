-- A script that lists all the cities

-- SQL query to find the id of california
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- SQL query to list all the cities
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
