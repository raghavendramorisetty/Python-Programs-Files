#Program for Reading OR Selecting the Records from Employee Table--fetchall()
#SelectRecordEx3.py
import oracledb as orc
def selectrecords():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        cur.execute("select * from employeedb")
        #all the records of employee table are present in cur object
        print("*"*50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main program
selectrecords()