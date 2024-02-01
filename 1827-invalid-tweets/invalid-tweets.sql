# Write your MySQL query statement below
select tweet_id from Tweets where char_length(content) >15;

/*select tweet_id from Tweets
where length(content) >15;

https://leetcode.com/problems/invalid-tweets/solutions/4431281/one-line-solution-length-vs-char-length-sql-gotcha/?envType=study-plan-v2&envId=top-sql-50 

Using LENGTH() instead of CHAR_LENGTH() is incorrect when trying to get the number of characters in the string

Definitions:
LENGTH(): returns the length of a string (in bytes).
CHAR_LENGTH(): return the length of a string (in characters).
Code
# Write your MySQL query statement below
SELECT tweet_id FROM Tweets 
WHERE CHAR_LENGTH(content) > 15;
Important Note:
Using Length() indeed passes all the test cases in this example. But it fails in case of UTF8 where different characters take up different number of bytes.

For example: Each Chinese character is represented by 3 bytes.

-- Creating a table with a string containing a multibyte character
CREATE TABLE Example (
    id INT,
    content VARCHAR(50)
);

INSERT INTO Example VALUES
(1, 'Hello, 你好'); --> ('Hello' -> 3 + ', ' -> 4 + '你好' -> 6 = 13)


SELECT LENGTH(content) AS Char_Length FROM Example;
Output:

+------------+
| Char_Length |
+------------+
| 13         |
+------------+
Correct length of the string is 9 but using Length() here gives out 13 as the answer.




*/