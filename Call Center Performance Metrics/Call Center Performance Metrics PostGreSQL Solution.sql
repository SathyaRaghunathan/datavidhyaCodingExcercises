SELECT ca.date AS date ,COUNT(DISTINCT ca.cust_id) AS num_customers, SUM(CAST(ca.duration AS int)) AS total_duration FROM cc_calls ca
INNER JOIN cc_customer cu on ca.cust_id = cu.cust_id
GROUP BY 1
ORDER BY 1
