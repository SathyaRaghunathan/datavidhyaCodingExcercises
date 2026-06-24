-- Write query here
-- TABLE NAME: `ic_data_1` and `ic_data_2`
WITH CTE1 AS (SELECT * FROM ic_data_1
UNION all
SELECT * FROM ic_data_2)
SELECT * FROM CTE1 ORDER BY age ASC