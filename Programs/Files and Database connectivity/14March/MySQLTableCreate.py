#Program for Creating Table
#MySQLTableCreate.py
import mysql.connector
def createtable():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root",
                                      database="6pmbatch")
        cur=con.cursor()
        #design Query,place the query  and execute
        #tc="create table teacher(tno int primary key, name  varchar(10) not null, sal float not null)"
        tc = "create table employee(empno int primary key, ename varchar(10) not null, empsal float not null, compname varchar(10) not null)"
        cur.execute(tc)
        print("Table Created Sucessfully in MySQL --Verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL ", db)

#Main program
createtable() # Function Call