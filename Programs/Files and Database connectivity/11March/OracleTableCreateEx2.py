#Program for Creating a Table
#OracleTableCreateEx2.py
import oracledb as orc
def tablecreate():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #get the query from KBD
        tc=input("Enter query to create a table(follow oracle syntax):")
        cur.execute(tc)
        print("Table created--verify")
    except orc.DatabaseError as x:
        print("print in oracle Db: ",x)

# Main program
tablecreate() # function call