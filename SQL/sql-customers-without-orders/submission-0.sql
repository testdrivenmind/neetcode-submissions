-- Write your query below
SELECT
    name
FROM
    customers c
WHERE
    c.id NOT IN
    (SELECT customer_id FROM orders)
