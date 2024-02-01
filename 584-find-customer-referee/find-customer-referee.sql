# Write your MySQL query statement below

select name from customer
where referee_id != 2 or referee_id is null;

/*SELECT name
FROM Customer
WHERE COALESCE(referee_id,0) <> 2;

<> is same as !=

here COALESCE is used to replace NULL values with zero before checking whether it is equal to 2 or not.*/

#https://www.datacamp.com/tutorial/coalesce-sql-function 