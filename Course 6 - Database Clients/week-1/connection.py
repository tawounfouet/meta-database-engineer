print("Importing MySQL Connector/Python API")
import mysql.connector as connector
print("MySQL Connector/Python API is imported successfully.\n")


# Establis connection with authorized user/password
print("Establishing a new connection between MySQL and Python.")
connection=connector.connect(user="admin-meta",password="admin")
print("A connection between MySQL and Python is successfully established")