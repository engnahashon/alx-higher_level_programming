-- Script: Create hbtn_0c_0 database
-- Task: Create the hbtn_0c_0 database in a MySQL server

-- Create hbtn_0c_0 database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Display a message indicating whether the database was created or not
SELECT 
    CASE 
        WHEN ROW_COUNT() = 0 THEN 'Database already exists'
        ELSE 'Database created successfully'
    END AS MESSAGE;
