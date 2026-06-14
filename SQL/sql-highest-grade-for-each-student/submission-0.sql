-- Write your query below

WITH max_scores AS (
    SELECT
        student_id,
        MAX(score) AS max_score
    FROM
        exam_results 
    GROUP BY
        student_id
)
SELECT
    e.student_id,
    MIN(e.exam_id) AS exam_id,
    e.score
FROM
    exam_results e
JOIN
    max_scores m
ON
    e.student_id = m.student_id AND
    e.score = m.max_score
GROUP BY
    e.student_id, e.score
ORDER BY
    e.student_id

