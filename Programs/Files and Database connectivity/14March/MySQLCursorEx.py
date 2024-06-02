#Program for Creating Cursor object
#MySQLCursorEx.py
import mysql.connector
try:
    con=mysql.connector.connect(host="127.0.0.1",
                                                user="root",
                                                passwd="root")
    print("Python Program Got Connection from MySQL")
    cur=con.cursor()
    print("Python program created cursor")
except mysql.connector.DatabaseError as db:
    print("problem in mysql:",db)
