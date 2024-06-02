#MySQLDisplayTableEx.py
#Program for Obtaining Column Names and Records of  any Table
import mysql.connector
def selectcolnames():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root",
                                      database="6pmbatch")
        cur=con.cursor()
        cur.execute("select * from %s " %(input("Enter table Name:")))
        #Get all the col names by using an attribute description
        print("*"*50)
        colnames=cur.description
        for colname in colnames:
            print("\t{}".format(colname[0]),end="\t")
        print()
        print("*" * 50)
        records=cur.fetchall()
        for record in records:
            for val in record:
               print("\t{}".format(val),end="\t")
            print()
        print("*" * 50)


    except mysql.connector.DatabaseError as db:
        print("Table does not exist")
#Main program
selectcolnames()