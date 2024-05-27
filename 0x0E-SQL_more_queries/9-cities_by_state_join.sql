-- A script that lists all the cities in hbtn_0d_2 database


-- SQL query that lists all the cities in the database
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id - states.id
ORDER BY cities.id ASC;
