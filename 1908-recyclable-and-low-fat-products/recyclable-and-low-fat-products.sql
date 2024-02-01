# Write your MySQL query statement below
select product_id from Products where low_fats ='Y' and recyclable ="Y";

/*

#what is enum dtype -> https://www.geeksforgeeks.org/enumerator-enum-in-mysql/

An ENUM is a string object whose value is decided from a set of permitted literals(Values) that are explicitly defined at the time of column creation.

Benefits of Enum data type –
Succinct data storage required to store data in limited size columns. 
The strings that you pass to the enum data types implicitly get the numerical numbering.


CREATE TABLE Student_grade(
id INT PRIMARY KEY AUTO_INCREMENT, Grade VARCHAR(250) NOT NULL,
priority ENUM('Low', 'Medium', 'High') NOT NULL
);

INSERT INTO Student_grade(Grade, priority)
VALUES('Poor grades', 1);
// Here we use 1 instead of using 'Low' enumeration value, 
since 1 is mapped to 'Low' implicitly.

*/