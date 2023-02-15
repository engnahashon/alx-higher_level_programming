-- This script creates a table called force_name in a specified MySQL database

-- Check if the force_name table already exists, and create it if it does not
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
