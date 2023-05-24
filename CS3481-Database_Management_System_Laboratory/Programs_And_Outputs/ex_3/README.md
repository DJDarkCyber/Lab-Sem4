# QUERY DATABASE TABLES USING WHERE CLAUSE CONDITIONS AND AGGREGATE FUNCTIONS

## Queries

`CREATE TABLE departments(department_id INT PRIMARY KEY, department_name VARCHAR(50) NOT NULL);`

OUTPUT:

```
Query OK, 0 rows affected (0.026 sec)
```

---

`CREATE TABLE employees (employee_id INT PRIMARY KEY, employee_name VARCHAR(50) NOT NULL, department_id INT, salary DECIMAL(10,2), FOREIGN KEY (department_id) REFERENCES departments (department_id) ON DELETE RESTRICT ON UPDATE CASCADE);`

OUTPUT:

```
Query OK, 0 rows affected (0.030 sec)
```

---

`INSERT INTO departments (department_id, department_name) VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'IT'), (4, 'Finance');`

OUTPUT:

```
Query OK, 4 rows affected (0.022 sec)
Records: 4  Duplicates: 0  Warnings: 0
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
4 rows in set (0.000 sec)
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

---

### Select all employees who work in a specific department

`SELECT * FROM employees WHERE department_id = 1;`

OUTPUT:


```
+-------------+-----------------+---------------+----------+
| employee_id | employee_name   | department_id | salary   |
+-------------+-----------------+---------------+----------+
|           1 | John Doe        |             1 | 50000.00 |
|           5 | Michael Johnson |             1 | 55000.00 |
+-------------+-----------------+---------------+----------+
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
```

### Select the average salary of employees in each department

`SELECT departments.department_name, AVG(salary) FROM employees JOIN departments ON employees.department_id = departments.department_id GROUP BY departments.department_name;`

OUTPUT:

```
+-----------------+--------------+
| department_name | AVG(salary)  |
+-----------------+--------------+
| Sales           | 52500.000000 |
| Marketing       | 55000.000000 |
| IT              | 60000.000000 |
| Finance         | 65000.000000 |
+-----------------+--------------+
4 rows in set (0.000 sec)
```
