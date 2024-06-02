#Program for Obtaining Column Names and Records of Table
#SelectRecordsWithColNames.py
import oracledb as orc
def selectcolnames():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        cur.execute("select * from employeedb")
        #Get all the col names by using an attribute description
        print("*"*50)
        colnames=cur.description
        print(colnames)
        for colname in colnames:
            print("\t{}".format(colname[0]),end="\t")
        print()
        print("*" * 50)
        records=cur.fetchall()
        for record in records:
            for val in record:
               print("\t{}".format(val),end="\t")
            print()
        print("*" * 50)

    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main program
selectcolnames()