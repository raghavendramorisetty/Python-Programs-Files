#Program for Creating Database
#MySQLDatabaseCreate.py
import mysql.connector
def  createdb():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root")
        cur=con.cursor()
        #design the Query, place the query in cursor object and execute
        dc="create database 6pmbatch"
        cur.execute(dc)
        print("Database created in MYSQL successfully--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL", db)
#main program
createdb() #Function call
