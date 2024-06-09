#OopsWithMySQLDB.py
import mysql.connector
class Student:
    def getstuddata(self):
        self.tno=int(input("Enter teacher Number:"))
        self.name=input("Enter teacher Name:")
        self.sal=float(input("Enter Salary:"))
    def savestuddata(self):
        try:
            con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="6pmbatch")
            cur=con.cursor()
            iq="insert into teacher values(%d,'%s',%f)"
            cur.execute(iq %(self.tno,self.name,self.sal))
            con.commit()
            print("{} teacher Record inserted".format(cur.rowcount))
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL:",db)
#Main program
s=Student()
s.getstuddata()
s.savestuddata()