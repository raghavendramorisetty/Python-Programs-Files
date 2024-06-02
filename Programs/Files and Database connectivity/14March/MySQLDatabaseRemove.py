#Program for Creating Database
#MySQLDatabaseRemove.py
import mysql.connector
def  removedb():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root")
        cur=con.cursor()
        #design the Query, place the query in cursor object and execute
        cur.execute("drop database 6pmbatch")
        print("Database Removed from MySQL Sucessfully--Verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL ", db)
    #Main Program
removedb() #Function call