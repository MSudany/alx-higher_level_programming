-- lists all records of second table
INSERT INTO second_table (name, score)
VALUES
('Aria', 18),
('Aria', 12);
DELETE FROM second_table
WHERE name = 'George';
SELECT score, name
FROM second_table
ORDER BY score DESC;
