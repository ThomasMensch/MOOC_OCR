SELECT
    salary
FROM
    salaries s
WHERE
    s.emp_no IN(
        SELECT emp_no
        FROM employees e
        WHERE e.hire_date > '1999-08-20');
