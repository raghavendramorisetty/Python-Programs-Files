#Program for Inserting employee values as Record in employee table
#OracleRecordInsertEx1.py
import oracledb as orc
def recordinsert():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #design the query and execute
        iq="insert into employeedb values(40,'hunter',2.6,'mlu')"
        cur.execute(iq)
        con.commit()
        print("Record inserted in employee table--verify")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)

#main program
recordinsert() #function call