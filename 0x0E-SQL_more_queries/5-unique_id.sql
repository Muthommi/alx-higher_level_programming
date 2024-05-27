-- A script that creates unique_id table

-- SQL query to create a unique_id table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
