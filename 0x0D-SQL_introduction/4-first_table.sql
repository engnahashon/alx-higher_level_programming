-- Script: Create first_table in current database
-- Task: Create a table called first_table with id and name columns in a MySQL database

USE database_name;

-- Create first_table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
