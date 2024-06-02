#Program for Reading OR Selecting the Records from Employee Table--fetchone()
#SelectRecordEx1.py
import oracledb as orc
def selectrecords():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        cur.execute("select * from employeedb")
        #all the records of employee table are present in cur object
        print("*"*50)
        while(True):
            rec=cur.fetchone()
            #print(rec)
            if(rec!=None):
                for val in rec:
                    print("\t{}".format(val),end="\t")
                print()
            else:
                print("*"*50)
                break
    except orc.DatabaseError as db:
        print("Problem in oracle: ",db)

# Main program
selectrecords()
