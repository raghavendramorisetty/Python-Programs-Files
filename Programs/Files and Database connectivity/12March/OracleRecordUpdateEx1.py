#program for Updating a Record Based on employee Number
#OracleRecordUpdateEx1.py
import oracledb as orc
def recordupdate():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #design the query and execute
        cur.execute("update employeedb set esalary=4.7,compname='oracle' where eno=3")
        con.commit()
        if(cur.rowcount>0):
            print("{} record updated in employee table".format(cur.rowcount))
        else:
            print("employee record does not exist")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)

#main program
recordupdate() #function call