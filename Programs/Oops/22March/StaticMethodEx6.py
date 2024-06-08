#Program for Demonstrating Static Method
#StaticMethodEx6.py
class Student:
    def readstuddata(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.marks=float(input("Enter Student Marks:"))
        print("--------------------------------------------------")
        Hyd.dispobjdata(self ,"Student")#call static method of Hyd class from readstuddata() of Student Class

class Employee:
    def readempdata(self):
        self.eno = int(input("Enter Employee Number:"))
        self.ename = input("Enter Employee Name:")
        print("--------------------------------------------------")
        Hyd.dispobjdata(self, "Employee")  # call static method of Hyd class from readempdata() of Employee Class
class Teacher:
    def readteacherdata(self):
        self.tno = int(input("Enter Teacher Number:"))
        self.tname = input("Enter Teacher Name:")
        self.tsub = input("Enter Teacher Subject:")
        self.exp= int(input("Enter Teacher Experience:"))
        print("--------------------------------------------------")
        Hyd.dispobjdata(self, "Teacher")  # call static method of Hyd class from readteacherdata() of Teacher Class
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
