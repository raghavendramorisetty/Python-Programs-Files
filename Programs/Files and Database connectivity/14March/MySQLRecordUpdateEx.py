#program for Updating a Record Based on employee Number
#MySQLRecordUpdateEx2.py
import mysql.connector
def  recordupdate():
    while(True):
        try:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="6pmbatch")
            cur=con.cursor()
            #accept employee Number from Keyboard
            print("--------------------------------------------------------")
            empno=int(input("Enter Employee Number for Updating Other details:"))
            empsal=float(input("Enter Ur New Salary:"))
            cmpname=input("Enter Ur New Comp Name:")
            #design the query and execute
            cur.execute("update employee set empsal=%f,compname='%s' where empno=%d" %(empsal,cmpname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Updated from Employee Table ".format(cur.rowcount))
            else:
                print("Employee Record Does Not Exist")
            print("--------------------------------------------------------")
            ch=input("Do u want to update another record(yes/no):")
            if(ch.lower()=="no"):
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)
        except ValueError:
            print("Don't  enter alnums,strs and symbols for Emp Number:")

#main program
recordupdate() # Function call