#Program for Removing the table
#OracleTableDropEx1.py
import oracledb as orc
def removetable():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        # Design the query, place the query in cursor and execute
        cur.execute("drop table studentData")
        print("table removed--verify")
    except orc.DatabaseError as x:
        print("problem in oracle db: ",x)

#main program
removetable()
