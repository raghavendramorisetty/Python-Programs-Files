#Program for Removing the table
#OracleTableDropEx2.py
import oracledb as orc
def removetable():
    try:
        orc.init_oracle_client()
        con = orc.connect("system/manager@localhost/xe")
        cur = con.cursor()
        ##Desig the query,place the query in cursor and execute
        cur.execute("drop table %s" %input("Enter Table Name to remove:"))
        print("Table removed--verify")
    except orc.DatabaseError as x:
        print("Problem in Oracle DB: ",x)
#Main program
removetable()