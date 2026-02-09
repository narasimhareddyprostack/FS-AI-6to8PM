class-1
-----------------------
cmd>
mysql -uroot -proot

show databases;
system cls;

CREATE DATABASE 6pm;
USE 6pm;
show tables;

CREATE TABLE employees();
CREATE TABLE employees(
	eid int,
	ename VARCHAR(32),
	esal  float,
	gender VARCHAR(32)
);

DESC employees;


SELECT *FROM employees;

 --INSERT one more
INSERT INTO employees
VALUES
(101,'Rahul',45000.45,'Male');
-- insert multiple rows

INSERT INTO employees
VALUES
(102,'Sonia',55000.55,'Female'),
(103,'Priyanka',65000.65,'Female'),
(104,'Modi',75000.75,'Male');

SELECT *FROM employees;

-- insert only two column
INSERT INTO employees(eid,ename)
VALUES
(105,'Amith');

--update table data
UPDATE employees
SET ename="Rahul Gandhi"
WHERE eid=101;

--update table data without where
--it update all rows
UPDATE employees
SET esal=99999.99;

--delete one/more rows
DELETE FROM employees
WHERE eid=101;

--delete all rows
DELETE FROM employees;

DELETE vs DROP


INSERT INTO employees
VALUES
(101,'Rahul',45000.45,'Male');

INSERT INTO employees
VALUES
(102,'Sonia',55000.55,'Female'),
(103,'Priyanka',65000.65,'Female'),
(104,'Modi',75000.75,'Male');

INSERT INTO employees(eid,ename)
VALUES
(105,'Amith');


DELETE vs Drop?
DELETE one more more rows. but still TABLE SCHEMA exits
DROP : completely dropping TABLE SCHEMA AND data
DELETE FROM employees;
DROP TABLE employees;