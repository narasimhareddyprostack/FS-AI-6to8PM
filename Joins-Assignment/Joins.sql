mysql -uroot -proot
CREATE DATABASE retail;
USE retail;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    cust_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    address VARCHAR(255),
    city VARCHAR(50),
    status ENUM('ACTIVE','INACTIVE') DEFAULT 'ACTIVE',

    PRIMARY KEY (customer_id)
);

CREATE TABLE products (
    product_id VARCHAR(30) UNIQUE,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    
    PRIMARY KEY (product_id)
);

---------------------------------------
SELECT 
customers.cust_name AS "Customer Name",
sales_request.request_id AS "Sales Request Details",
sales_request.request_status AS "Status"
FROM
customers
INNER JOIN sales_request
ON customers.customer_id = sales_request.customer_id;

SELECT 
customers.cust_name AS "Customer Name",
sales_request.request_id AS "Sales Request Details",
sales_request.request_status AS "SR Status",
sales_order.order_id AS "Order Details",
sales_order.order_status AS "Order Status"
FROM
customers
INNER JOIN sales_request
ON customers.customer_id = sales_request.customer_id
INNER JOIN sales_order
ON sales_request.request_id =sales_order.request_id;


SELECT COUNT(*) AS "No of Customres"  FROM customers; 


SELECT 
customers.cust_name AS "Customer Name",
sales_request.request_id AS "Sales Request Details",
sales_request.request_status AS "SR Status",
sales_order.order_id AS "Order Details",
sales_order.order_status AS "Order Status"
FROM
customers
LEFT JOIN sales_request
ON customers.customer_id = sales_request.customer_id
LEFT JOIN sales_order
ON sales_request.request_id =sales_order.request_id;


select d.*,c.order_status,a.cust_name
from Customers a 
RIGHT join sales_request b 
On a.customer_id = b.customer_id
RIGHT join sales_order c 
On b.request_id = c.request_id
RIGHT join payment d 
On c.order_id = d.order_id;


select pt.*, sr.request_id AS "SR Request Id" ,
so.order_status AS "Order Status",
cust.cust_name AS "Customer Name"
from Customers cust
RIGHT join sales_request sr
On cust.customer_id = sr.customer_id
RIGHT join sales_order so 
On sr.request_id = so.request_id
RIGHT join payment pt 
On so.order_id = pt.order_id;