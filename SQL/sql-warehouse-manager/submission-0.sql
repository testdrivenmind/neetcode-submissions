-- Write your query below
WITH product_vol AS (
    SELECT
    product_id,
    product_name,
    width * length * height AS volume
FROM
    products
GROUP BY
    product_id

)

SELECT 
    w.name AS warehouse_name,
    sum(volume * w.units) AS volume
FROM
    warehouse w
JOIN
    product_vol v
ON 
    w.product_id = v.product_id
GROUP BY
    w.name