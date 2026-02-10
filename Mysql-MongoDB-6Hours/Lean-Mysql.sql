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

--class -2
--__________________

mysql -uroot -proot

DROP DATABASE 6pm;

CREATE DATABASE 6pm;
USE 6pm;

CREATE TABLE order_tab(
order_id INT,
order_name VARCHAR(32),
price FLOAT,
status VARCHAR(32)
);

DESC order_tab;

INSERT INTO order_tab
VALUES
(1,'Marker Pen',30.30,'In Progress'),
(1,'Mouse',300.30,'In Progress'),
(1,'Laptap',55555.30,'Delivered'),
(1,'Charger',3000.30,'Delivered');

SELECT *FROM order_tab;

--Rules on data
--SQL contraints 
--Mysql 7 contraints
-- not null,unique,check,defualt,primary key,fk,index

CREATE TABLE employees(
	eid INT UNIQUE ,
	ename VARCHAR(32) NOT NULL,
	esal FLOAT CHECK(esal>=18000.00),
	loc VARCHAR(32) DEFAULT 'Bangalore'
);

INSERT INTO employees
VALUES
(101,'Rahul',19000,'Chennai');

--unique means duplicates are not allowed
-- but null values allowed mutliple times

INSERT INTO employees(ename,esal,loc)
VALUES
('Sonia',20000,'New Delhi'),
('Priya',21000,'USA'),
('Modi',22000,'Varanasi');

SELECT *FROM employees;


INSERT INTO employees(eid,esal,loc)
VALUES
(102,56000,'Marathahalli');

--default : if user not provided value it take default value
INSERT INTO employees(eid,ename,esal)
VALUES
(103,'Rajni',60000.60),
(104,'Vijay',70000.60),
(105,'VS',80000.60),
(106,'Kamal',90000.60);

SELECT *FROM employees;

INSERT INTO employees
VALUES
(107,'Narasimha',17000,'Chennai');

DROP TABLE employees;


CREATE TABLE employees(
	eid INT,
	ename VARCHAR(32) NOT NULL,
	esal FLOAT CHECK(esal>=18000.00),
	loc VARCHAR(32) DEFAULT 'Bangalore',

	PRIMARY KEY(eid)
);

INSERT INTO employees
VALUES
(101,'Rahul',19000,'Bangalore');

DROP TABLE employees;



CREATE TABLE employees(
	eid INT PRIMARY key,
	ename VARCHAR(32) NOT NULL,
	esal FLOAT CHECK(esal>=18000.00),
	loc VARCHAR(32) DEFAULT 'Bangalore'
);

DESC employees;