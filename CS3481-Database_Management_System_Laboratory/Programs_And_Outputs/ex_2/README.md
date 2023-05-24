# CREATE A SET OF TABLES, ADD FOREIGN KEY CONSTRAINTS AND INCORPORATE REFERENTIAL INTEGRITY

## Queries

`CREATE TABLE departments (department_id INT PRIMARY KEY, department_name VARCHAR(50) NOT NULL);`

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
Query OK, 4 rows affected (0.011 sec)
Records: 4  Duplicates: 0  Warnings: 0
```

---

`INSERT INTO employees (employee_id, employee_name, department_id, salary) VALUES (1, 'John Doe', 1, 50000), (2, 'Jane Doe', 2, 55000), (3, 'Jim Smith', 3, 60000), (4, 'Sarah Johnson', 4, 65000), (5, 'Michael Johnson', 1, 55000), (6, 'Emily Davis', 2, 52000), (7, 'David Brown', 3, 60000), (8, 'Katie Wilson', 4, 63000), (9, 'William Davis', 1, 55000), (10, 'Emily Wilson', 2, 53000), (11, 'James Brown', 3, 65000);`

OUTPUT:

```
Query OK, 11 rows affected (0.011 sec)
Records: 11  Duplicates: 0  Warnings: 0
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
|           6 | Emily Davis     |             2 | 52000.00 |
|           7 | David Brown     |             3 | 60000.00 |
|           8 | Katie Wilson    |             4 | 63000.00 |
|           9 | William Davis   |             1 | 55000.00 |
|          10 | Emily Wilson    |             2 | 53000.00 |
|          11 | James Brown     |             3 | 65000.00 |
+-------------+-----------------+---------------+----------+
11 rows in set (0.000 sec)
```
