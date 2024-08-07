-- A script that creates the database and a user

-- SQL query to create a database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- SQL query to create a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- SQL query to grant privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
