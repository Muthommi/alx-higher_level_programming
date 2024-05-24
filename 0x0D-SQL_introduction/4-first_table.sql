-- This script creates a table called first_table in the specified database

-- SQL query to create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Use the specified database
USE hbtn_0c_0;

-- SQL query to create the table if it does not exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
