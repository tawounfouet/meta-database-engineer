### Connecting to the MySQL
```bash

# Connect to the MySQL server using the root user and password
mysql -u awf -p 
# Enter password: awf
```




## Lab Instructions  

Lucky Shrub is a medium-sized garden design firm that sells indoor and outdoor plants, making them a one stop shop for clients.  In this lab, you are going to complete the following tasks to make it easier for Lucky Shrub staff to print relevant order data on the screen.  


The Orders table contains information about the Order ID, Client ID, Product ID, Quantity and Cost as shown below.  

 ![Orders table](images/orders.PNG) 

Note: Before you begin, make sure you know how to access [MySQL environment](https://www.coursera.org/learn/database-structures-and-management-with-mysql/supplement/BSZK6/how-to-access-mysql-environment).

### Prerequisites  

To complete this lab, you must have the Lucky Shrub database created in MySQL. Also, you must have the Orders table created and populated with relevant data inside Lucky Shrub.  

The code to create the database and the Orders table is listed below.  

1: Create database 

```SQL 

CREATE DATABASE IF NOT EXISTS Lucky_Shrub;

``` 

2: Use database 

```SQL 

USE Lucky_Shrub; 

``` 

3: Create Orders table 

```SQL 

CREATE TABLE Orders (OrderID INT NOT NULL PRIMARY KEY, ClientID VARCHAR(10),  ProductID VARCHAR(10),  Quantity   INT, Cost DECIMAL(6,2)); 

``` 

4: Insert data 

```SQL 

INSERT INTO Orders (OrderID, ClientID, ProductID , Quantity, Cost) VALUES (1, "Cl1", "P1", 10, 500), (2, "Cl2", "P2", 5, 100), (3, "Cl3", "P3", 20, 800), (4, "Cl4", "P4", 15, 150), (5, "Cl3", "P3", 10, 450), (6, "Cl2", "P2", 5, 800), (7, "Cl1", "P4", 22, 1200), (8, "Cl3", "P1", 15, 150), (9, "Cl1", "P1", 10, 500), (10, "Cl2", "P2", 5, 100); 

```   
 
5.1 - Create customer_purchases table 
    
```SQL
CREATE TABLE customer_purchases (
    CustomerID INT NOT NULL PRIMARY KEY,
    CustomerName VARCHAR(50),
    Location VARCHAR(50),
    Purchses INT
);
```


5.2 - Insert data into customer_purchases table

```SQL
INSERT INTO customer_purchases (CustomerID, CustomerName, Location, Purchses) VALUES 
(1, "Takashi Ito", "Gram County", 1500), 
(3, "Jane Murphy", "Pinal County", 1750), 
(4, "Laurina Delgado", "Santa Cruz County", 2000), 
(5, "Benjamin Clauss", "Gila County", 2500),
(6, "Altay Ayhan", "Cochise County", 2000),
(7, "Greta Galkina", "Mohave County", 500),
(8, "July Marr", "Gila County", 2250),
(9, "Robert Anderson", "San Diego", 9000),
(10, "Jennifer Taylor", "Dallas", 10000);


# insert new record
INSERT INTO customer_purchases (CustomerID, CustomerName, Location, Purchses) 
VALUES (11, "Richard Harris", "San Francisco", 11000),
(12, "Linda Lee", "San Jose", 12000),
(13, "Michael Clark", "Austin", 13000),
(14, "Elizabeth Hall", "Jacksonville", 14000),
(15, "Charles Allen", "Indianapolis", 15000),
(16, "Karen Young", "Columbus", 16000),
(17, "Mark Hernandez", "Fort Worth", 17000),
(18, "Margaret King", "Charlotte", 18000),
(19, "Edward Wright", "Seattle", 19000),
(20, "Lisa Lopez", "Denver", 20000);
```

```sql
# detele the table
DROP TABLE customer_purchases;
```






## This activity aims to achieve the following objective:    

 
* Filtering data using WHERE clause and logical operators. 
 
 

## Tasks Instructions 

Please attempt the following tasks: 

**Task 1:** Write a SQL statement to print all records of orders where the cost is $250 or more. The expected output result should be the same as the following screenshot (assuming that you have populated the Orders table with the same data set) 

![Task 1 output](images/task1output.PNG) 

  
 

**Task 2:** Write a SQL statement to print all records of orders where the cost is between $50 and $750. The expected output result should be the same as the following screenshot (assuming that you have populated the orders table with the same data set) 

![Task 2 output](images/task2output.PNG)

 

**Task 3:** Write a SQL statement to print all records of orders that have been placed by the client with the id of Cl3 and where the cost of the order is more than $100. The expected output result should be the same as the following screenshot (assuming that you have populated the Orders table with the same data set) 

![Task 3 output](images/task3output.PNG) 

 

**Task 4:** Write a SQL statement to print all records of orders that have a product id of p1 or p2 and the order quantity is more than 2. The expected output result should be the same as the following screenshot (assuming that you have populated the Orders table with the same data set) 

![Task 4 output](images/task4output.PNG) 


 
 

