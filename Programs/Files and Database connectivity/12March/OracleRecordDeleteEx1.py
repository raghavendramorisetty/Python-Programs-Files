#program for deleting a Record Based on employee Number
#OracleRecordDeleteEx1.py
import oracledb as orc
def recorddelete():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #design the query and execute
        cur.execute("delete from studentTable where sno=3")
        con.commit()
        if(cur.rowcount>0):
            print("{} record deleted from employee table".format(cur.rowcount))
        else:
            print("employee record does not exist")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
#main program
recorddelete() #function call
