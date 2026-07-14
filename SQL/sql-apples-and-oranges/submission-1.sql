-- Write your query below
SELECT
    o.sale_date,
    (a.sold_num - o.sold_num) AS diff
FROM
    sales o
JOIN 
    sales a
ON
    o.sale_date = a.sale_date
WHERE
    o.fruit = 'oranges' AND a.fruit = 'apples'
ORDER BY sale_date


