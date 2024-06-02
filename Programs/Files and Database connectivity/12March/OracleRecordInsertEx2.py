#Program for Inserting employee values as Record in employee table
#OracleRecordInsertEx2.py
import oracledb as orc
def recordinsert():
    try:
        orc.init_oracle_client()
        con=orc.connect("system/manager@localhost/xe")
        cur = con.cursor()
        # Accept Employee Values from Key Board
        print("*" * 50)
        empno = int(input("Enter Employee Number:"))
        ename = input("Enter Employee Name:")
        empsal = float(input("Enter Employee Salary:"))
        compname = input("Enter Employee Company Name:")
        print("*" * 50)
        # design the query and execute
        iq = "insert into employeedb values(%d,'%s' ,%f,'%s')"
        cur.execute(iq % (empno, ename, empsal, compname))
        # OR
        # cur.execute("insert into employee values(%d,'%s' ,%f,'%s') "%(empno,ename,empsal,compname))
        con.commit()
        # print("%d Record Inserted in Employee Table--verify " %cur.rowcount)  OR
        print("{} Record Inserted in Employee Table--verify ".format(cur.rowcount))
        print("*" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle DB: ", db)


# main program
recordinsert()  # Function call