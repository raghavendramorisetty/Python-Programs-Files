#Program for Demonstrating Static Method
#StaticMethodEx1.py
class Student:
    def readstuddata(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.marks=float(input("Enter Student Marks:"))
        print("--------------------------------------------------")

class Employee:
    def readempdata(self):
        self.eno = int(input("Enter Employee Number:"))
        self.ename = input("Enter Employee Name:")
        print("--------------------------------------------------")
class Teacher:
    def readteacherdata(self):
        self.tno = int(input("Enter Teacher Number:"))
        self.tname = input("Enter Teacher Name:")
        self.tsub = input("Enter Teacher Subject:")
        self.exp= int(input("Enter Teacher Experience:"))
        print("--------------------------------------------------")
class Hyd:
    @staticmethod
    def dispobjdata(obj,objinfo):
        print("{} Information".format(objinfo))
        print("--------------------------------------")
        for dmn,dmv in obj.__dict__.items():
            print("\t{}---->{}".format(dmn,dmv))
        print("--------------------------------------")

#Main Program
s=Student()
e=Employee()
t=Teacher()
#Read the Data for Object s
s.readstuddata()
#Read the Data for Object e
e.readempdata()
#Read the Data for Object t
t.readteacherdata()
#Display the Data of any class object--we use static method
Hyd.dispobjdata(s,"Student")# static method accessed w.r.t Class Name
Hyd.dispobjdata(e,"Employee") # static method accessed w.r.t Class Name
Hyd.dispobjdata(t,"Teacher")# static method accessed w.r.t Class Name
