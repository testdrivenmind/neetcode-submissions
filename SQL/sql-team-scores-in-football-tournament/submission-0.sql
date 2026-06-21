-- Write your query below
WITH scores_team_perspective AS (
    SELECT
        host_team AS team_id,
        host_goals AS goals_scored,
        guest_goals AS goals_conceded
    FROM
        matches
    UNION ALL
    
    SELECT
        guest_team AS team_id,
        guest_goals AS goals_scored,
        host_goals AS goals_conceded
    FROM
        matches) 
SELECT
    t.team_id,
    t.team_name,
    COALESCE(SUM(CASE
            WHEN s.goals_scored > s.goals_conceded THEN 3
            WHEN s.goals_scored = s.goals_conceded THEN 1
            ELSE 0
        END), 0) AS num_points
FROM
    teams t
LEFT JOIN
    scores_team_perspective s
ON
    t.team_id = s.team_id
GROUP BY
    t.team_id, t.team_name
ORDER BY num_points DESC, t.team_id

