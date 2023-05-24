# QUERY DATABASE TABLES USING SUBQUERIES AND SIMPLE JOIN OPERATIONS

## Queries

`CREATE TABLE departments ( department_id INT PRIMARY KEY, department_name VARCHAR(50) NOT NULL );`

OUTPUT:

```
Query OK, 0 rows affected (0.021 sec)
```

---

`CREATE TABLE employees(employee_id INT PRIMARY KEY, employee_name VARCHAR(50) NOT NULL, department_id INT, salary DECIMAL(10, 2), FOREIGN KEY(department_id) REFERENCES departments (department_id) ON DELETE RESTRICT ON UPDATE CASCADE);`

OUTPUT:

```
Query OK, 0 rows affected (0.053 sec)
```

---

`INSERT INTO departments (department_id, department_name) VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'IT'), (4, 'Finance');`

OUTPUT:

```
Query OK, 4 rows affected (0.022 sec)
Records: 4  Duplicates: 0  Warnings
```

---

`SELECT * FROM departments;`

OUTPUT:

```
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|             1 | Sales           |
|             2 | Marketing       |
|             3 | IT              |
|             4 | Finance         |
+---------------+-----------------+
```

---

`INSERT INTO employees (employee_id, employee_name, department_id, salary) VALUES (1, 'John Doe', 1, 50000), (2, 'Jane Doe', 2, 55000), (3, 'Jim Smith', 3, 60000), (4, 'Sarah Johnson', 4, 65000), (5, 'Michael Johnson', 1, 55000);`

OUTPUT:

```
Query OK, 5 rows affected (0.012 sec)
Records: 5  Duplicates: 0  Warnings: 0
```

---

`SELECT * FROM employees;`

OUTPUT:

```
+-------------+-----------------+---------------+----------+
| employee_id | employee_name   | department_id | salary   |
+-------------+-----------------+---------------+----------+
|           1 | John Doe        |             1 | 50000.00 |
|           2 | Jane Doe        |             2 | 55000.00 |
|           3 | Jim Smith       |             3 | 60000.00 |
|           4 | Sarah Johnson   |             4 | 65000.00 |
|           5 | Michael Johnson |             1 | 55000.00 |
+-------------+-----------------+---------------+----------+
5 rows in set (0.000 sec)
```

### Select all employees who make more than 55000

`SELECT * FROM employees WHERE salary > 55000;`

OUTPUT:

```
+-------------+---------------+---------------+----------+
| employee_id | employee_name | department_id | salary   |
+-------------+---------------+---------------+----------+
|           3 | Jim Smith     |             3 | 60000.00 |
|           4 | Sarah Johnson |             4 | 65000.00 |
+-------------+---------------+---------------+----------+
2 rows in set (0.000 sec)
```


### Select employee names and department names from both tables using a join

`SELECT employees.employee_name, departments.department_name FROM employees JOIN departments ON employees.department_id = departments.department_id;`

OUTPUT:

```
+-----------------+-----------------+
| employee_name   | department_name |
+-----------------+-----------------+
| John Doe        | Sales           |
| Michael Johnson | Sales           |
| Jane Doe        | Marketing       |
| Jim Smith       | IT              |
| Sarah Johnson   | Finance         |
+-----------------+-----------------+
5 rows in set (0.000 sec)
```

### Subquery to find the average salary of all employees

`SELECT AVG(salary) FROM (SELECT salary FROM employees) AS emp_salary;`

OUTPUT:

```
+--------------+
| AVG(salary)  |
+--------------+
| 57000.000000 |
+--------------+
1 row in set (0.000 sec)
```

### Simple join operation to combine data from both tables

`SELECT employees.employee_name, departments.department_name, employees.salary FROM employees JOIN departments ON employees.department_id = departments.department_id;`

OUTPUT:

```
+-----------------+-----------------+----------+
| employee_name   | department_name | salary   |
+-----------------+-----------------+----------+
| John Doe        | Sales           | 50000.00 |
| Michael Johnson | Sales           | 55000.00 |
| Jane Doe        | Marketing       | 55000.00 |
| Jim Smith       | IT              | 60000.00 |
| Sarah Johnson   | Finance         | 65000.00 |
+-----------------+-----------------+----------+
5 rows in set (0.000 sec)
```
