
# Developing functions in MySQL



Task 1 solution: 

Create a function that prints the cost value of a specific order. This should be based on the user input of the OrderID. The expected output result should be the same as the result in the screenshot below when you call the function with OrderID 5.

123
CREATE FUNCTION FindCost(order_id INT) 
RETURNS DECIMAL (5,2) DETERMINISTIC 
RETURN (SELECT Cost FROM Orders WHERE OrderID = order_id);
Screenshot of output of of findcost column in a table

