SELECT * FROM employees e
WHERE e.emp_no IN(
    SELECT
        emp_no
    FROM
        employees e
    ORDER BY e.birth_date ASC
    LIMIT 5);
