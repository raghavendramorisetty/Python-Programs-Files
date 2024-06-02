#Program for Obtaining Connection from MySQL Database
#MySQLConnectionTestEx1.py
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",
                                                user="root",
                                                passwd="root")
    print("Python Program Got Connection from MySQL")
except mysql.connector.DatabaseError as db:
    print("Problem in MySQL ",db)