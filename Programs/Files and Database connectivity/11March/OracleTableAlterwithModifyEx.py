#Program altering the column Sizes of any table
#OracleTableAlterwithModifyEx.py
import oracledb as orc
def alterwithmodify():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #Design the query,place the query in cursor and execute
        aq="alter table employeedb modify(eno number(5),ename varchar2(15))"
        cur.execute(aq)
        print("Table altered--verify")
    except orc.DatabaseError as x:
        print("problem in oracle db: ",x)

# Main program
alterwithmodify() # function call

