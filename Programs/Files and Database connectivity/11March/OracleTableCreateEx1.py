#Program for Creating a Table
#OracleTableCreateEx1.py
import oracledb as orc
def tablecreate():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        #Design the query,place the query in cursor and execute
        tc="create table studentTable(sno number(2) primary key,name varchar2(10) not null,marks number(5,2) not null)"
        cur.execute(tc)
        print("Table created successfully--verify")
    except orc.DatabaseError as db:
        print("Problem in oracle DB: ",db)

# Main Program
tablecreate() # Function Call
