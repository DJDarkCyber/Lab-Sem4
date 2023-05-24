# QUERY DATABASE TABLES USING NATURAL, EQUI AND OUTER JOINS

## Queries

`CREATE TABLE customers ( id INT PRIMARY KEY, name VARCHAR(50), email VARCHAR(50));`

OUTPUT:

```
Query OK, 0 rows affected (0.028 sec)
```

---

`CREATE TABLE orders ( id INT PRIMARY KEY,customer_id INT, product VARCHAR(50), price DECIMAL(10, 2), CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(id));`

OUTPUT:

```
Query OK, 0 rows affected (0.042 sec)
```

---

`INSERT INTO customers (id, name, email) VALUES (1, 'Prakash', 'john.doe@example.com'), (2, 'Jane Smith', 'jane.smith@example.com'), (3, 'Bob Johnson', 'bob.johnson@example.com');`

OUTPUT:

```
Query OK, 3 rows affected (0.019 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

---

`SELECT * FROM customers;`

OUTPUT:

```
+----+-------------+-------------------------+
| id | name        | email                   |
+----+-------------+-------------------------+
|  1 | Prakash     | john.doe@example.com    |
|  2 | Jane Smith  | jane.smith@example.com  |
|  3 | Bob Johnson | bob.johnson@example.com |
+----+-------------+-------------------------+
3 rows in set (0.000 sec)
```

---

`INSERT INTO orders (id, customer_id, product, price) VALUES (1, 1, 'Widget', 10.00), (2, 2, 'Gizmo', 15.00),(3, 1, 'Thingamajig', 20.00), (4, 3, 'Widget', 10.00);`

OUTPUT:

```
Query OK, 4 rows affected (0.004 sec)
Records: 4  Duplicates: 0  Warnings: 0
```

---

`SELECT*FROM orders;`

OUTPUT:

```
+----+-------------+-------------+-------+
| id | customer_id | product     | price |
+----+-------------+-------------+-------+
|  1 |           1 | Widget      | 10.00 |
|  2 |           2 | Gizmo       | 15.00 |
|  3 |           1 | Thingamajig | 20.00 |
|  4 |           3 | Widget      | 10.00 |
+----+-------------+-------------+-------+
4 rows in set (0.000 sec)
```


---

`SELECT * FROM customers NATURAL JOIN orders;`

OUTPUT:

```
+----+-------------+-------------------------+-------------+-------------+-------+
| id | name        | email                   | customer_id | product     | price |
+----+-------------+-------------------------+-------------+-------------+-------+
|  1 | Prakash     | john.doe@example.com    |           1 | Widget      | 10.00 |
|  2 | Jane Smith  | jane.smith@example.com  |           2 | Gizmo       | 15.00 |
|  3 | Bob Johnson | bob.johnson@example.com |           1 | Thingamajig | 20.00 |
+----+-------------+-------------------------+-------------+-------------+-------+
3 rows in set (0.000 sec)
```

---

`SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id;`

OUTPUT:


```
+----+-------------+-------------------------+----+-------------+-------------+-------+
| id | name        | email                   | id | customer_id | product     | price |
+----+-------------+-------------------------+----+-------------+-------------+-------+
|  1 | Prakash     | john.doe@example.com    |  1 |           1 | Widget      | 10.00 |
|  1 | Prakash     | john.doe@example.com    |  3 |           1 | Thingamajig | 20.00 |
|  2 | Jane Smith  | jane.smith@example.com  |  2 |           2 | Gizmo       | 15.00 |
|  3 | Bob Johnson | bob.johnson@example.com |  4 |           3 | Widget      | 10.00 |
+----+-------------+-------------------------+----+-------------+-------------+-------+
4 rows in set (0.000 sec)
```

---

`SELECT * FROM orders RIGHT OUTER JOIN customers ON orders.customer_id = customers.id;`

OUTPUT:

```
+------+-------------+-------------+-------+----+-------------+-------------------------+
| id   | customer_id | product     | price | id | name        | email                   |
+------+-------------+-------------+-------+----+-------------+-------------------------+
|    1 |           1 | Widget      | 10.00 |  1 | Prakash     | john.doe@example.com    |
|    3 |           1 | Thingamajig | 20.00 |  1 | Prakash     | john.doe@example.com    |
|    2 |           2 | Gizmo       | 15.00 |  2 | Jane Smith  | jane.smith@example.com  |
|    4 |           3 | Widget      | 10.00 |  3 | Bob Johnson | bob.johnson@example.com |
+------+-------------+-------------+-------+----+-------------+-------------------------+
```

---

`SELECT * FROM customers LEFT OUTER JOIN orders ON customers.id = orders.customer_id;`

OUTPUT:

```
+----+-------------+-------------------------+------+-------------+-------------+-------+
| id | name        | email                   | id   | customer_id | product     | price |
+----+-------------+-------------------------+------+-------------+-------------+-------+
|  1 | Prakash     | john.doe@example.com    |    1 |           1 | Widget      | 10.00 |
|  1 | Prakash     | john.doe@example.com    |    3 |           1 | Thingamajig | 20.00 |
|  2 | Jane Smith  | jane.smith@example.com  |    2 |           2 | Gizmo       | 15.00 |
|  3 | Bob Johnson | bob.johnson@example.com |    4 |           3 | Widget      | 10.00 |
+----+-------------+-------------------------+------+-------------+-------------+-------+
4 rows in set (0.000 sec)
```
