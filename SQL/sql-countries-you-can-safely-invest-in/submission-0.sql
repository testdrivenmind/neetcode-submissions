-- Write your query below
WITH combined_calls AS (
    SELECT caller_id AS person_id, duration FROM calls
    UNION ALL
    SELECT callee_id AS person_id, duration FROM calls
)
SELECT 
    co.name AS country
FROM 
    combined_calls AS ca
JOIN
    person p
ON p.id = ca.person_id
JOIN 
    country co
ON LEFT(p.phone_number, 3) = co.country_code
GROUP BY co.name
HAVING avg(ca.duration) > (SELECT AVG(duration) FROM combined_calls)