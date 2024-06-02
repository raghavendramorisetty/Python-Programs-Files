#Program for Obtaining Column Names of Table
#MetaDataInfoEx1.py
import oracledb as orc
def selectcolnames():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        cur.execute("select * from employeedb ")
        #Get all the col names by using an attribute description
        print("*"*50)
        colnames=cur.description
        for colname in colnames:
            #print(colname)
            print("\t{}".format(colname[0]),end="\t")
            #print()
        print()
        print("*" * 50)
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main program
selectcolnames()