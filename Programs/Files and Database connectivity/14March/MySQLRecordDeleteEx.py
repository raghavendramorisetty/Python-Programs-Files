#program for deleteting a Record Based on employee Number
#MySQLRecordDeleteEx.py
import mysql.connector
def  recorddelete():
    while(True):
        try:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="6pmbatch")
            cur=con.cursor()
            #accept employee Number from Keyboard
            print("--------------------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            #design the query and execute
            cur.execute("delete from employee where empno=%d" %empno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Deleted from Employee Table ".format(cur.rowcount))
            else:
                print("Employee Record Does Not Exist")
            print("--------------------------------------------------------")
            ch=input("Do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)
        except ValueError:
            print("Don't  enter alnums,strs and symbols for Emp Number:")

#main program
recorddelete() # Function call
