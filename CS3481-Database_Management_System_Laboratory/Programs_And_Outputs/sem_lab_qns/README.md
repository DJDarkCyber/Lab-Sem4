# SEM 4 Questions

  1. Consider the following schema for a Library Database:
  BOOK (Book_id, Title, Publisher_Name, Pub_Year, No_of_copies)
  BOOK_AUTHORS (Book_id, Author_Name)
  PUBLISHER (Name, Address, Phone)

```
MySQL [an]> CREATE TABLE BOOK (
    ->     Book_id INT PRIMARY KEY,
    ->     Title VARCHAR(100),
    ->     Publisher_Name VARCHAR(100),
    ->     Pub_Year INT,
    ->     No_of_copies INT
    -> );
Query OK, 0 rows affected (0.037 sec)

MySQL [an]> CREATE TABLE BOOK_AUTHORS (
    ->     Book_id INT,
    ->     Author_Name VARCHAR(100),
    ->     FOREIGN KEY (Book_id) REFERENCES BOOK(Book_id)
    -> );
Query OK, 0 rows affected (0.036 sec)

MySQL [an]> INSERT INTO BOOK (Book_id, Title, Publisher_Name, Pub_Year, No_of_copies)
    -> VALUES
    ->     (1, 'Book 1', 'Publisher A', 2020, 100),
    ->     (2, 'Book 2', 'Publisher B', 2018, 50),
    ->     (3, 'Book 3', 'Publisher A', 2021, 75),
    ->     (4, 'Book 4', 'Publisher C', 2019, 120);
Query OK, 4 rows affected (0.012 sec)
Records: 4  Duplicates: 0  Warnings: 0

MySQL [an]> INSERT INTO BOOK_AUTHORS (Book_id, Author_Name)
    -> VALUES
    ->     (1, 'Author A'),
    ->     (1, 'Author B'),
    ->     (2, 'Author C'),
    ->     (3, 'Author D'),
    ->     (4, 'Author E');
Query OK, 5 rows affected (0.019 sec)
Records: 5  Duplicates: 0  Warnings: 0

MySQL [an]> CREATE TABLE PUBLISHER (
    ->     Name VARCHAR(100) PRIMARY KEY,
    ->     Address VARCHAR(100),
    ->     Phone VARCHAR(20)
    -> );
Query OK, 0 rows affected (0.033 sec)

MySQL [an]> INSERT INTO PUBLISHER (Name, Address, Phone)
    -> VALUES
    ->     ('Publisher A', 'Address A', '123-456-7890'),
    ->     ('Publisher B', 'Address B', '987-654-3210'),
    ->     ('Publisher C', 'Address C', '555-123-4567');
Query OK, 3 rows affected (0.017 sec)
Records: 3  Duplicates: 0  Warnings: 0


```

*    Retrieve details of all books in the Book_id, title, name of publisher, authors:

```
MySQL [an]> SELECT Book_id, Title, Name FROM BOOK JOIN PUBLISHER;
+---------+--------+-------------+
| Book_id | Title  | Name        |
+---------+--------+-------------+
|       1 | Book 1 | Publisher C |
|       1 | Book 1 | Publisher B |
|       1 | Book 1 | Publisher A |
|       2 | Book 2 | Publisher C |
|       2 | Book 2 | Publisher B |
|       2 | Book 2 | Publisher A |
|       3 | Book 3 | Publisher C |
|       3 | Book 3 | Publisher B |
|       3 | Book 3 | Publisher A |
|       4 | Book 4 | Publisher C |
|       4 | Book 4 | Publisher B |
|       4 | Book 4 | Publisher A |
+---------+--------+-------------+
12 rows in set (0.000 sec)
```

* Get the particulars of borrowers who have borrowed more than 3 books, but from Jan
2017 to Jun2017.


```
MySQL [an]> CREATE TABLE borrower_data (
    ->     Borrower_id INT PRIMARY KEY,
    ->     Name VARCHAR(100),
    ->     Borrowed_books INT,
    ->     Borrowed_date DATE
    -> );
Query OK, 0 rows affected (0.028 sec)

MySQL [an]> INSERT INTO borrower_data (Borrower_id, Name, Borrowed_books, Borrowed_date)
    -> VALUES
    ->     (1, 'John Doe', 5, '2017-02-10'),
    ->     (2, 'Jane Smith', 4, '2017-05-15'),
    ->     (3, 'Michael Johnson', 2, '2017-04-20'),
    ->     (4, 'Emily Brown', 6, '2017-01-05'),
    ->     (5, 'David Wilson', 1, '2017-06-30');
Query OK, 5 rows affected (0.011 sec)
Records: 5  Duplicates: 0  Warnings: 0

MySQL [an]> SELECT *
    -> FROM borrower_data
    -> WHERE Borrowed_books > 3
    ->   AND Borrowed_date BETWEEN '2017-01-01' AND '2017-06-30';
+-------------+-------------+----------------+---------------+
| Borrower_id | Name        | Borrowed_books | Borrowed_date |
+-------------+-------------+----------------+---------------+
|           1 | John Doe    |              5 | 2017-02-10    |
|           2 | Jane Smith  |              4 | 2017-05-15    |
|           4 | Emily Brown |              6 | 2017-01-05    |
+-------------+-------------+----------------+---------------+
3 rows in set (0.000 sec)

```



2. Create a table employee (S.No,Name,Desination,brach),

```
MySQL [an]> CREATE TABLE employee (
    ->   `S.No` INT NOT NULL AUTO_INCREMENT,
    ->   `Name` VARCHAR(255),
    ->   `Designation` VARCHAR(255),
    ->   `Branch` VARCHAR(255),
    ->   PRIMARY KEY (`S.No`)
    -> );
Query OK, 0 rows affected (0.022 sec)
```

* Alter the table by adding a column salary

```
MySQL [an]> ALTER TABLE employee ADD Salary DECIMAL(10,2);
Query OK, 0 rows affected (0.048 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

* Copy the table employee as Emp

```
MySQL [an]> CREATE TABLE Emp LIKE employee;
Query OK, 0 rows affected (0.035 sec)

```

* Delete 2nd row from the table

```
MySQL [an]> DELETE FROM employee WHERE `S.No` = 2;
Query OK, 0 rows affected (0.000 sec)

```

* Drop the table

```
DROP TABLE employee;
```

* Demonstrate the triggers for automatic updation.

```
MySQL [an]> CREATE TRIGGER update_salary
    -> BEFORE INSERT ON employee
    -> FOR EACH ROW
    -> SET NEW.Salary = NEW.Salary * 1.1;
Query OK, 0 rows affected (0.027 sec)

```

3. Create a table called Employee (Emp_no Emp_name, Emp_dept,Job ,Mgr ,Sal)

```
MySQL [an]> CREATE TABLE Employee (
    ->   Emp_no INT NOT NULL,
    ->   Emp_name VARCHAR(255) NOT NULL,
    ->   Emp_dept VARCHAR(255),
    ->   Job VARCHAR(255),
    ->   Mgr INT,
    ->   Sal DECIMAL(10, 2),
    ->   PRIMARY KEY (Emp_no)
    -> );
Query OK, 0 rows affected (0.038 sec)

MySQL [an]> INSERT INTO Employee (Emp_no, Emp_name, Emp_dept, Job, Mgr, Sal) VALUES (101, 'John Doe', 'Sales', 'Sales Manager', NULL, 5000.00);
Query OK, 1 row affected (0.003 sec)

MySQL [an]> INSERT INTO Employee (Emp_no, Emp_name, Emp_dept, Job, Mgr, Sal) VALUES (102, 'Jane Smith', 'Marketing', 'Marketing Manager', NULL, 5500.00);
Query OK, 1 row affected (0.002 sec)

MySQL [an]> INSERT INTO Employee (Emp_no, Emp_name, Emp_dept, Job, Mgr, Sal) VALUES (103, 'Bob Johnson', 'HR', 'HR Manager', NULL, 6000.00);
Query OK, 1 row affected (0.004 sec)

MySQL [an]> INSERT INTO Employee (Emp_no, Emp_name, Emp_dept, Job, Mgr, Sal) VALUES (104, 'Alice Lee', 'Sales', 'Sales Executive', 101, 3500.00);
Query OK, 1 row affected (0.002 sec)

MySQL [an]> INSERT INTO Employee (Emp_no, Emp_name, Emp_dept, Job, Mgr, Sal) VALUES (105, 'Tom Williams', 'Marketing', 'Marketing Executive', 102, 4000.00);
Query OK, 1 row affected (0.023 sec)

```

* By using the group by clause, display the Emp_name who belongs to
Emp_dept=”xxx” along with salary

```
MySQL [an]> SELECT Emp_name, Sal
    -> FROM Employee
    -> WHERE Emp_dept = 'xxx'
    -> GROUP BY Emp_name, Sal;
Empty set (0.001 sec)

```

* Display lowest paid employee details under each department

```
MySQL [an]> SELECT Emp_dept, Emp_name, Sal
    -> FROM Employee
    -> WHERE Sal IN (
    ->   SELECT MIN(Sal)
    ->   FROM Employee
    ->   GROUP BY Emp_dept
    -> )
    -> ORDER BY Emp_dept;
+-----------+--------------+---------+
| Emp_dept  | Emp_name     | Sal     |
+-----------+--------------+---------+
| HR        | Bob Johnson  | 6000.00 |
| Marketing | Tom Williams | 4000.00 |
| Sales     | Alice Lee    | 3500.00 |
+-----------+--------------+---------+
3 rows in set (0.003 sec)

```

* List the employee names in descending order.

```
MySQL [an]> SELECT Emp_name
    -> FROM Employee
    -> ORDER BY Emp_name DESC;
+--------------+
| Emp_name     |
+--------------+
| Tom Williams |
| John Doe     |
| Jane Smith   |
| Bob Johnson  |
| Alice Lee    |
+--------------+
5 rows in set (0.001 sec)

```

* Rename the column of Employee table using alter command

```
MySQL [an]> ALTER TABLE Employee
    -> CHANGE COLUMN Emp_dept Department VARCHAR(255);
Query OK, 0 rows affected (0.029 sec)
Records: 0  Duplicates: 0  Warnings: 0

```

* Insert row in employee table using Triggers.

```
MySQL [an]> CREATE TABLE Employee_Log (
    ->   Log_id INT NOT NULL AUTO_INCREMENT,
    ->   Emp_no INT NOT NULL,
    ->   Emp_name VARCHAR(255) NOT NULL,
    ->   Department VARCHAR(255),
    ->   Job VARCHAR(255),
    ->   Mgr INT,
    ->   Sal DECIMAL(10, 2),
    ->   Log_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ->   PRIMARY KEY (Log_id)
    -> );
Query OK, 0 rows affected (0.033 sec)

MySQL [an]> DELIMITER //
MySQL [an]> CREATE TRIGGER insert_employee
    -> AFTER INSERT ON Employee
    -> FOR EACH ROW
    -> BEGIN
    ->   INSERT INTO Employee_Log (Emp_no, Emp_name, Department, Job, Mgr, Sal)
    ->   VALUES (NEW.Emp_no, NEW.Emp_name, NEW.Department, NEW.Job, NEW.Mgr, NEW.Sal);
    -> END//
Query OK, 0 rows affected (0.022 sec)

```

4. Consider the following tables namely “DEPARTMENTS” and “EMPLOYEES” Departments (dept_no , dept_ name , dept_location ), Employees ( emp_id , emp_name , emp_salary,dept_no).

```
MySQL [an]> CREATE TABLE Departments (
    ->   dept_no INT NOT NULL,
    ->   dept_name VARCHAR(255) NOT NULL,
    ->   dept_location VARCHAR(255),
    ->   PRIMARY KEY (dept_no)
    -> );
    ->
    -> CREATE TABLE Employees (
    ->   emp_id INT NOT NULL,
    ->   emp_name VARCHAR(255) NOT NULL,
    ->   emp_salary DECIMAL(10, 2),
    ->   dept_no INT,
    ->   PRIMARY KEY (emp_id),
    ->   FOREIGN KEY (dept_no) REFERENCES Departments(dept_no)
    -> );
    Query OK, 0 rows affected (0.028 sec)

    Query OK, 0 rows affected (0.051 sec)


```

* Develop a query to grant some privileges of employees table into departments table

```
MySQL [an]> GRANT SELECT, INSERT,UPDATE, DELETE ON Employees TO Departments;
```

* Develop a query to revoke all privileges of employees table from departments table

```
REVOKE ALL PRIVILEGES ON Employees FROM Departments;
```

* Develop a query to revoke some privileges of employees table from departments table

```
REVOKE INSERT, UPDATE ON Employees FROM Departments;
```


* Write a query to implement the save point.

```
SAVEPOINT my_savepoint;
```

* Demonstrate the user defined procedure for the above employee database

```
MySQL [an]> DELIMITER //
MySQL [an]> CREATE PROCEDURE get_employee_by_dept(IN dept_name VARCHAR(255))
    -> BEGIN
    ->   SELECT emp_name, emp_salary
    ->   FROM Employees
    ->   WHERE dept_no = (
    ->     SELECT dept_no
    ->     FROM Departments
    ->     WHERE dept_name = dept_name
    ->   );
    -> END//
Query OK, 0 rows affected (0.011 sec)

MySQL [an]> DELIMITER ;
```


5. Create the following tables,

```
CREATE TABLE Event (
  eventid INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255),
  city VARCHAR(255),
  PRIMARY KEY (eventid)
);

CREATE TABLE Participant (
  playerid INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  eventid INT NOT NULL,
  gender VARCHAR(10),
  year INT,
  PRIMARY KEY (playerid),
  FOREIGN KEY (eventid) REFERENCES Event(eventid)
);

CREATE TABLE Prizes (
  prizeid INT NOT NULL,
  prize_money DECIMAL(10, 2),
  eventid INT NOT NULL,
  rank INT,
  year INT,
  PRIMARY KEY (prizeid),
  FOREIGN KEY (eventid) REFERENCES Event(eventid)
);

CREATE TABLE Winners (
  prizeid INT NOT NULL,
  playerid INT NOT NULL,
  PRIMARY KEY (prizeid, playerid),
  FOREIGN KEY (prizeid) REFERENCES Prizes(prizeid),
  FOREIGN KEY (playerid) REFERENCES Participant(playerid)
);

INSERT INTO Event (eventid, name, description, city)
VALUES (1, 'Marathon', 'A long-distance running race', 'New York');

INSERT INTO Participant (playerid, name, eventid, gender,year)
VALUES (1, 'John Doe', 1, 'Male', 1990);

INSERT INTO Prizes (prizeid, prize_money, eventid, rank, year)
VALUES (1, 1000.00, 1, 1, 2022);

INSERT INTO Winners (prizeid, playerid)
VALUES (1, 1);


```

*  Choose appropriate primary keys and foreign keys for the tables.
