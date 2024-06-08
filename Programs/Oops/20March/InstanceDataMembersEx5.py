#Program for String sno,sname and marks of a Student
#InstanceDataMembersEx5.py
class Student:pass

#Main Program
s1=Student() # Here s1 is called Object
s2=Student() # Here s2 is called Object
print("ID of s1 Object=",id(s1))
print("ID of s2 Object=",id(s2))
print("Content of s1={} and Number of Values={}".format(s1.__dict__, len(s1.__dict__)))
print("Content of s2={} and Number of Values={}".format(s2.__dict__, len(s2.__dict__)))
print("----------------------------------------------")
#Add the Instance Data--sno,name and marks  to s1 Object
s1.sno=int(input("Enter First Student Number:"))
s1.name=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:"))
#Add the Instance Data ---sno,name and marks --to s2 Object
s2.sno=int(input("Enter Second Student Number:"))
s2.name=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:"))
print("First Student Data")
print("----------------------------------------------")
for dmn,dmv in s1.__dict__.items():
    print("\t{}-->{}".format(dmn,dmv))
print("----------------------------------------------")
print("Second Student Data")
print("----------------------------------------------")
for dmn,dmv in s2.__dict__.items():
    print("\t{}-->{}".format(dmn,dmv))
print("----------------------------------------------")
