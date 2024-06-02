#program for deleting a Record Based on employee Number
#OracleRecordDeleteEx2.py
import oracledb as orc
def  recorddelete():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/xe")
            cur=con.cursor()
            #accept employee Number from Keyboard
            print("--------------------------------------------------------")
            sno=int(input("Enter student Number:"))
            #design the query and execute
            cur.execute("delete from studentTable where sno=%d" %sno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Deleted from studentTable Table ".format(cur.rowcount))
            else:
                print("student Record Does Not Exist")
            print("--------------------------------------------------------")
            ch=input("Do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle DB: ",db)
        except ValueError:
            print("Don't  enter alnums,strs and symbols for student Number(sno):")

#main program
recorddelete() # Function call