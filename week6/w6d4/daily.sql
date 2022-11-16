-- 1
-- select first_name AS First, last_name AS Last from employees; 

-- 2
-- SELECT DISTINCT department_id from employees;


-- 3
-- SELECT * FROM employees 
-- order by first_name desc;

-- 4
-- SELECT first_name, last_name, salary, salary*0.15 as PF
-- from employees;

-- 5
-- SELECT employee_id, first_name, last_name, salary from employees
-- order by salary ASC;

-- 6
-- SELECT SUM(salary)
-- from employees;

-- 7
-- SELECT MIN(salary) from employees;

-- SELECT MAX(salary) from employees;

-- 8
-- SELECT AVG(salary) from employees;

-- 9
-- SELECT COUNT(employee_id) from employees;

-- 10
-- SELECT UPPER(first_name) from employees;

-- 11
-- SELECT SUBSTRING (first_name, 1, 3) from employees;

-- 12
-- SELECT concat (first_name, ' ', last_name) AS full_name from employees;

-- 13
-- SELECT first_name, last_name,
-- LENGTH(CONCAT(first_name, ' ', last_name)) AS len_full
-- from employees;


-- 14
-- SELECT first_name from employees
-- WHERE first_name like '%[0-9]%';

-- -- 15
-- SELECT * FROM employees limit 10;



Part 2
-- 1
-- SELECT first_name, last_name, salary from employees
-- where salary between 10000 and 15000;


-- 2
-- SELECT first_name, last_name, hire_date from employees
-- where extract(YEAR FROM hire_date) = 1987;

--3
-- SELECT first_name from employees 
-- where first_name like '%c%e%';

-- 4
-- SELECT last_name, job_title, salary from employees
-- Inner Join jobs on employees.job_id=jobs.job_id
-- where job_title != 'Programmer'
-- and job_title != 'Shippping Clerk'
-- and salary != 4500
-- and salary !=10000
-- and salary !=15000;

-- 

-- 5
-- SELECT last_name from employees
-- where LENGTH(last_name) = 6;

-- 6
-- SELECT last_name from employees 
-- where last_name like '__e%';

--7
-- SELECT DISTINCT job_title from employees
-- inner join jobs
-- on employees.job_id=jobs.job_id;

--8
-- select * from employees
-- where last_name ='Jones'
-- or last_name = 'Blake'
-- or last_name = 'Scott'
-- or last_name = 'King'
-- or last_name = 'Ford';