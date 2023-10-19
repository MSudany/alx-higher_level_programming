-- ...
SELECT id AS cities.id, name AS cities.name, states.name AS states.name
FROM cities
JOIN states
ON cities.id = states.id
