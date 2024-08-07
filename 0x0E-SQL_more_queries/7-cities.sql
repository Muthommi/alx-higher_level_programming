-- A script that creates hbtn_0d_usa database and the cities table

-- SQL query that creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- SQL query to use the table
USE hbtn_0d_usa;

-- SQL query that creates the table
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
