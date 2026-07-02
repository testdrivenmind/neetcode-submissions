-- Write your query below
SELECT
    customer_number
FROM
    orders
GROUP BY
    customer_number
HAVING 
    sum(order_number) > -100
ORDER BY sum(order_number) desc
LIMIT 1