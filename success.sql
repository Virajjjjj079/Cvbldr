create database cvbldr;
use cvbldr;
CREATE TABLE users2(

name VARCHAR(100),
email VARCHAR(200),
password VARCHAR(200) 
);


CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    job VARCHAR(255),
    name VARCHAR(255),
    
    location VARCHAR(255),
    salary DECIMAL(10, 2),
    email VARCHAR(200)
);
SELECT * from employees;