#program for Updating a Record Based on employee Number
#OracleRecordUpdateEx2.py
import oracledb as orc
def recordupdate():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/xe")
            cur=con.cursor()
            #accept employee number from keyboard
            print("------------------------------------------------")
            empno=int(input("Enter employee number for updating other details"))
            empsal=float(input("enter ur new salary:"))
            cmpname=input("enter ur new comp name:")
            #design the query and execute
            cur.execute("update employeedb set esalary=%f,compname='%s' where eno=%d" %(empsal,cmpname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} record updated from employee table".format(cur.rowcount))
            else:
                print("Employee record does not exist")
            print("------------------------------------------------")
            ch=input("do u want to update another record(yes/no):")
            if(ch.lower()=="no"):
                break
        except orc.DatabaseError as db:
            print("problem in oracle db:",db)
        except ValueError:
            print("Dont't enter alnums,strs and symbols for Emp Number:")

#main program
recordupdate() #function call
















