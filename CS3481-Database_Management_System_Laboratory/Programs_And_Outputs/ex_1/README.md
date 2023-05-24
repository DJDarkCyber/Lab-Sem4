# CREATE A DATABASE TABLE AND MANIPULATE DATA USING SQL DDL AND DML COMMANDS

## Query:

### Query 1 - Create a Table:

`CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER CHECK(age>=18), email VARCHAR(255) UNIQUE, gender CHAR(10) NOT NULL);`

OUTPUT:

```
Query OK, 0 rows affected (0.035 sec)
```

**Note: use `desc students;` to view info about the create table.**

### Query 2 - Inserting Data:

`INSERT INTO students(id, name, age, email, gender) VALUES (1, 'jack', 20, 'jack@gmail.com', 'Male'), (2, 'jane', 22, 'jane@gmail.com', 'Female');`

OUTPUT:

```
Query OK, 2 rows affected (0.022 sec)
Records: 2  Duplicates: 0  Warnings: 0
```

`SELECT * FROM students;`

OUTPUT:

```
+----+------------+------+----------------------+--------+
| id | name       | age  | email                | gender |
+----+------------+------+----------------------+--------+
|  1 | jack       |   20 | jack@gmail.com       | Male   |
|  2 | jane       |   22 | jane@gmail.com       | Female |
+----+------------+------+----------------------+--------+
```

### Query 3 - Update a row:

`update students SET age=23 WHERE id=2;`

OUTPUT:

```
Query OK, 1 row affected (0.014 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

`select * from students;`

OUTPUT:

```
+----+------+------+----------------+--------+
| id | name | age  | email          | gender |
+----+------+------+----------------+--------+
|  1 | jack |   20 | jack@gmail.com | Male   |
|  2 | jane |   23 | jane@gmail.com | Female |
+----+------+------+----------------+--------+
```

### Query 4 - Delete A Row

`DELETE FROM students WHERE id=2;`

OUTPUT:

```
+----+------+------+----------------+--------+
| id | name | age  | email          | gender |
+----+------+------+----------------+--------+
|  1 | jack |   20 | jack@gmail.com | Male   |
+----+------+------+----------------+--------+
```
