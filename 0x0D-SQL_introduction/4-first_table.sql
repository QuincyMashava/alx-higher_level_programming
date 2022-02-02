--Create database passsed as an argument if the table already exists the script should not fail

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
