create database test;
use test;

CREATE TABLE COMPANY (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10, 2),
    JoinDate DATE,
    Gender CHAR(1),
    City VARCHAR(50),
    Education VARCHAR(50),
    ExperienceYears INT
);

INSERT INTO COMPANY VALUES
    (1, 'abhi', 25, 'cs', 60000.00, '2022-01-01', 'M', 'kozhikode', 'Btech', 3),
    (2, 'dhane', 28, 'bca', 55000.50, '2021-05-15', 'M', 'kochi', 'degree', 5),
    (3, 'chithra', 22, 'mca', 48000.75, '2023-02-28', 'M', 'trivandum', 'pg', 1),
    (4, 'blair', 28, 'ece', 70000.25, '2022-10-10', 'M', 'kottayam', 'btech', 7),
    (5, 'sreya', 21, 'eee', 50000.00, '2020-12-05', 'F', 'kannur', 'btech', 10),
    (6, 'mithun', 24, 'civil', 55000.00, '2021-12-05', 'M', 'malappuram', 'btech', 10),
    (7, 'parvathy', 24, 'ece', 45000.00, '2024-12-05', 'F', 'mahe', 'btech', 10),
    (8, 'renjith', 30, 'IT', 75000.00, '2023-12-05', 'M', 'kollam', 'btech', 10),
    (9, 'darshan', 31, 'IT', 45455.00, '2022-12-05', 'M', 'thrissur', 'btech', 10),
    (10, 'sonu', 19, 'civil', 80000.00, '2021-12-05', 'M', 'kozhikode', 'btech', 10);
    

    
-- Select All Employees: 
SELECT * FROM COMPANY;

-- Select Specific Columns (First Name, and Salary):
SELECT FirstName, Salary FROM COMPANY;

-- Select Distinct Departments:
SELECT DISTINCT Department FROM COMPANY;

-- Select Employees in the IT Department:
SELECT * FROM COMPANY WHERE Department = 'IT';

-- Select Employees Older Than 28:
SELECT * FROM COMPANY WHERE Age > 28;

-- Select Female Employees:
SELECT * FROM COMPANY WHERE Gender = 'F';

-- Select Employees with Salaries Between $50000 and $70000:
SELECT * FROM COMPANY WHERE Salary BETWEEN 50000 AND 70000;

-- Select Employees in IT or ece Departments:
SELECT * FROM COMPANY WHERE Department IN ('IT', 'ece');

-- Select Employees with Specific experience years :
SELECT * FROM COMPANY WHERE ExperienceYears IN (10, 8, 7);

-- Select Employees with Names Starting with ‘d’:
SELECT * FROM COMPANY WHERE FirstName LIKE 'd%';

-- Select Employees with Salaries Above Average:
SELECT * FROM COMPANY WHERE Salary > (SELECT AVG(Salary) FROM COMPANY);

-- Select Employees Who Joined Before 2022-01-01:
SELECT * FROM COMPANY WHERE JoinDate < '2022-01-01';

-- Select Employees in IT Department AND Older Than 25:
SELECT * FROM COMPANY WHERE Department = 'IT' AND Age > 25;

-- Select Employees in IT Department OR eee Department:
SELECT * FROM COMPANY WHERE Department = 'IT' OR Department = 'eee';

-- Insert a new person:
INSERT INTO COMPANY VALUES
    (11, 'JITHIN', 21, 'civil', 50000.00, '2022-12-05', 'M', 'kozhikode', 'btech', 11);
    


    












    


    

    
