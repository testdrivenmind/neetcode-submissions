-- Write your query below
SELECT
    ROUND(SUM
        (CASE
            WHEN d.order_date = d.customer_pref_delivery_date THEN 1.0
            ELSE 0
        END) / COUNT(d.delivery_id) * 100.00, 2) AS immediate_percentage
FROM
    delivery d

    