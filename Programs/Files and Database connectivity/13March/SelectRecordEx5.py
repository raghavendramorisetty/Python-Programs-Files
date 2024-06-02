#Program for Reading OR Selecting the Records from Employee Table--fetchall()
#SelectRecordEx5.py
import oracledb as orc
def selectrecords():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        cur.execute("select * from employeedb order by esalary")
        #all the records of employee table are present in cur object
        print("*"*50)
        records=cur.fetchall()
        print("Highest Sal Emp details")
        for val in records[-1]:
            print("\t{}".format(val),end="\t")
        print()
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main program
selectrecords()