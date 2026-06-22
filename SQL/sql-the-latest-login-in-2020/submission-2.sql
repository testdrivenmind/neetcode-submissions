-- Write your query below
SELECT
    l.user_id,
    MAX(l.time_stamp) AS last_stamp
FROM
    logins l
WHERE
    EXTRACT(YEAR FROM l.time_stamp::timestamp) = '2020'
GROUP BY
    l.user_id

