#Program for Reading OR Selecting the Records from Employee Table--fetchall()
#MySQLSelectRecordEx.py
import mysql.connector
def selectrecords():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root",
                                      database="6pmbatch")
        cur=con.cursor()
        cur.execute("select * from employee order by empsal")
        #all the records of employee table are present in cur object
        print("*"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
        print("*" * 50)
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL:",db)
#Main program
selectrecords()