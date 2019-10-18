SELECT
    e.last_name AS nom_famille,
    count(*) AS cnt
FROM
    employees e
GROUP BY
    last_name
HAVING
    cnt > 200;

