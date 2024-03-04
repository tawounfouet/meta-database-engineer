


```bash
CREATE DATABASE little_lemon_db;

USE little_lemon_db;



CREATE TABLE Customers(CustomerID INT NOT NULL PRIMARY KEY, FullName VARCHAR(100) NOT NULL, PhoneNumber INT NOT NULL UNIQUE);


INSERT INTO Customers(CustomerID, FullName, PhoneNumber) VALUES (1, "Vanessa McCarthy", 0757536378), (2, "Marcos Romero", 0757536379), (3, "Hiroki Yamane", 0757536376), (4, "Anna Iversen", 0757536375), (5, "Diana Pinto", 0757536374);


CREATE TABLE Bookings (BookingID INT NOT NULL PRIMARY KEY,  BookingDate DATE NOT NULL,  TableNumber INT NOT NULL, NumberOfGuests INT NOT NULL CHECK (NumberOfGuests <= 8), CustomerID INT NOT NULL, FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE ON UPDATE CASCADE);


INSERT INTO Bookings (BookingID, BookingDate, TableNumber, NumberOfGuests, CustomerID) VALUES (10, '2021-11-11', 7, 5, 1), (11, '2021-11-10', 5, 2, 2), (12, '2021-11-10', 3, 2, 4);



# Create Table Food_Orders_Delevery_Status;
CREATE TABLE Food_Orders_Delevery_Status (
OrderID INT NOT NULL PRIMARY KEY, 
Date_food_order_placed_with_supplier DATE,
Date_food_order_received_from_supplier DATE,
OrderStatus VARCHAR(50) NOT NULL
);

# Insert data into Food_Orders_Delevery_Status

INSERT INTO Food_Orders_Delevery_Status (OrderID, Date_food_order_placed_with_supplier, Date_food_order_received_from_supplier, OrderStatus) VALUES 
(1, '2022-04-05', '2022-04-05', 'Delivered'),
(2, '2022-03-08', '2022-10-08', 'Delivered'),
(3, '2022-05-19', NULL, 'In Progress'),
(4, '2022-01-10', '2022-01-15', 'Delivered')
;
```


# Create Tables Starters with colunms(StarterName, Cost)
```sql
CREATE TABLE Starters (
StarterName VARCHAR(50) NOT NULL,
Cost DECIMAL(6,2) NOT NULL
);

# Insert data into Starters
INSERT INTO Starters (StarterName, Cost) VALUES 
('Garlic Bread', 5.00),
('Bruschetta', 6.00),
('Calamari', 8.00),
('Caprese Salad', 7.00),
('Mozzarella Sticks', 6.00)
;
```

# Create Tables Courses with colunms(CoursesName, Cost)
```sql
CREATE TABLE Courses (
CoursesName VARCHAR(50) NOT NULL,
Cost DECIMAL(6,2) NOT NULL
);

# Insert data into Courses
INSERT INTO Courses (CoursesName, Cost) VALUES 
('Spaghetti Carbonara', 12.00),
('Lasagna', 14.00),
('Fettuccine Alfredo', 13.00),
('Penne alla Vodka', 15.00),
('Ravioli', 16.00)
;
```

### Instructions

There are two main objectives of this activity:
1. Create an INNER JOIN query.

2. Create a LEFT JOIN query.

Task Instructions
Please attempt the following tasks:

Task 1: Little Lemon want a list of all customers who have made bookings. Write an INNER JOIN SQL statement to combine the full name and the phone number of each customer from the Customers table with the related booking date and 'number of guests' from the Bookings table. 

The expected output result should be the same as the following screenshot (assuming that you have created and populate the tables correctly.)