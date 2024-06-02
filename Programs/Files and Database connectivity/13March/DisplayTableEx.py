#DisplayTableEx.py
#Program for Obtaining Column Names and Records of any Table
import oracledb as orc
def selectcolnames():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        # employeedb or studentTable are table names that we have in our oracle database
        #so give any of above names as input
        cur.execute("select * from %s " %(input("Enter table Name:")))
        #Get all the col names by using an attribute description
        print("*"*50)
        colnames=cur.description
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
        print("Table does not exist")
#Main program
selectcolnames()