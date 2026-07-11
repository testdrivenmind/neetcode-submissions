-- Write your query below
SELECT
    ROUND(AVG
        (CASE
            WHEN d.order_date = d.customer_pref_delivery_date THEN 1.00
            ELSE 0
        END) * 100.00, 2) AS immediate_percentage
FROM
    delivery d

    