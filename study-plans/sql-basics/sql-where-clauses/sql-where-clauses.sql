-- Write your SQL query here
Select name, salary from employees 
    where 
(department = 'Engineering' or
department = 'Marketing') and
salary > 70000;
