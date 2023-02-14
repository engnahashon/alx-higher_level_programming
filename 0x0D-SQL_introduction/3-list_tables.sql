-- Script: List tables in a database
-- Task: List all the tables in a MySQL database

USE database_name;

-- Get a list of all tables in the database
SELECT table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema = 'database_name';
