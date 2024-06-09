#OopsWithOracleDB.py
import oracledb as orc
class Student:
    def getstuddata(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Entyer Student Name:")
        self.marks=float(input("Enter Student Marks:"))
    def savestuddata(self):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/xe")
            cur=con.cursor()
            iq="insert into studentTable values(%d,'%s',%f)"
            cur.execute(iq %(self.sno,self.sname,self.marks))
            con.commit()
            print("{} Student Record inserted".format(cur.rowcount))
        except orc.DatabaseError as db:
            print("Problem in Oracle:".db)

#Main program
s=Student()
s.getstuddata()
s.savestuddata()