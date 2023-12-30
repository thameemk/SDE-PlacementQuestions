--Second Highest Salary
--https://leetcode.com/problems/second-highest-salary/

SELECT LEAD(salary) OVER() AS SecondHighestSalary  FROM (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC) AS DerivedTable LIMIT 1;