#Program for Obtaining Connection from MySQL Database
#MySQLConnectionTestEx2.py
import mysql.connector
try:
    con=mysql.connector.connect(host="127.0.0.1",user='root',passwd='root')
    print("python program got connection from mysql")
except mysql.connector.DatabaseError as db:
    print("problem in mysql:",db)

