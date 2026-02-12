create table employee (
eid INT ,
fname VARCHAR(32),
lname VARCHAR(32),
city VARCHAR(32),
esal INT,
age INT,
PRIMARY KEY(eid)
);

mysql> desc employee;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| eid   | int         | NO   | PRI | NULL    |       |
| fname | varchar(32) | YES  |     | NULL    |       |
| lname | varchar(32) | YES  |     | NULL    |       |
| city  | varchar(32) | YES  |     | NULL    |       |
| esal  | int         | YES  |     | NULL    |       |
| age   | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

insert into employee values
(101,'Rahul','Gandhi','Wayanad',45000,52),
(102,'Sonia','Gandhi','New Delhi',55000,75),
(103,'Priyanka','Gandhi','Nodia',65000,45),
(104,'Modi','Narendra','New Delhi',75000,69),
(105,'Rajni','Kanth','Chennai',85000,65),
(106,'Vijay','Setupathi','Chennai',95000,47),
(107,'Nayana','Tara','Chennai',25000,40),
(108,'Alia','Bhut','Mumbai',45000,31),
(109,'Mahesh','Bhut','Mumbai',15000,68),
(110,'Sonam','Kapoor','Mumbai',30000,27),
(111,'Anil','Kapoor','Mumbai',38000,40),
(112,'Raj','Kapoor','Mumbai',18000,78),
(113,'Vishnu','Manchu','Hyderabad',10000,40),
(114,'Manoj','Manchu','Hyderabad',12000,35);

--Inserting a null salary value

INSERT INTO employee (eid,fname,lname,city,age)
values
(115,'Mohan','Manchu','Hyderabad',70);

Assignments
------------------
1. Write a query to fetch employee whose last name is same.
2. Write a query to fetch whose age is grater then 70.
3. Write a query to fetch employee with same city.
4. Write a query to fetch whose name ends with 'h'.
5. Write a query to count employee whose last name ends with 'i'.
6. Write a query to find employee with highest salary.
7. Write a query to find employee with lowest salary.
8. Write a query to change last name of employee whose id is 102.
9. Write a query to find name of employee whose name start's with 'A' and city name starts with 'B'.
10. Write a query to find employee with highest salary in 'Bangalore'.
11. Write a query to find employee who line in 'Hyderabad' with age above 70.
12. Write a query to find employee with salary below 50000.
13. Write a query to find name of employee with salary range between 20000 to 40000.
15. Write a query to find employee whose first name third character is 'j'.
16. Write a query to find employee whose first name third character is 'j' and live in 'Bangalore'.
17. Write a query to count employees whose first name third character is 'j'.
18. Write a query to fetch employee with lowest salary and add 10000 to its salary.
19. Write a query to Sort the table by ascending.
20. Write a query to Sort the table by descending.
21. Write a query to show employee whose name's last third word is 'j' and salary is more then 30000. 
22. Write a query to show all employee who live in 'Bangalore' and 'Wayanad'.
23. Write a query to fetch employee with first name count is 5.
24. Write a query to group by employee with their age.

26. Write a query to find employee with null salary.
27. Write a query to find employee whose cities are not null.
28. Write a query to delete data of employee whose id is 109.
29. Write a query to group by employee with their age and show first three rows of data.
30. Write a query to group by employee of 'Hyderabad' by their last name.