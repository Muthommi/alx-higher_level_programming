-- A script that inserts a new row in first_table

-- SQL query that inserts a new row in first_table
INSERT INTO first_table (id, name) 
SELECT * FROM (SELECT 89 AS id, 'Best School' AS name) AS new_row
WHERE NOT EXISTS (
    SELECT id, name FROM first_table WHERE id = 89 AND name = 'Best School'
) LIMIT 1;
