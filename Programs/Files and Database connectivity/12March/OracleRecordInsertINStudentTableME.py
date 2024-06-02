#Program for Inserting employee values as Record in employee table
#OracleRecordInsertINStudentTableME.py
import oracledb as orc
def recordinsert():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/xe")
            cur=con.cursor()
            sno = int(input("Enter student Number:"))
            name = input("Enter student Name:")
            marks = float(input("Enter student marks:"))
            #design the query and execute
            iq="insert into studentTable values(%d,'%s',%f)"
            cur.execute(iq %(sno,name,marks))
            con.commit()
            print("Record inserted in studentTable table--verify")
            ch = input("Do u want to Insert Another Record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for this Program")
                break
        except orc.DatabaseError as db:
            print("problem in oracle db:",db)

#main program
recordinsert() #function call