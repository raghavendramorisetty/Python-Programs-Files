# program for altering the table by adding column(s) name
# oracleTableAlterwithAddEx.py
import oracledb as orc


def alterwithadd():
    try:
        orc.init_oracle_client()
        con = orc.connect("system/manager@localhost/xe")
        cur=con.cursor()
        # Design the query,place the query in cursor and execute
        aq="alter table employeedb add(compname varchar2(10) not null)"
        cur.execute(aq)
        print("Table altered--verify")
    except orc.DatabaseError as x:
        print("problem in oracledb: ",x)

# Main program
alterwithadd() #Function call
