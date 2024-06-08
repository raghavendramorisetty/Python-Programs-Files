#Program for String sno,sname and marks of a Student
#InstanceDataMembersEx2.py
class Student:pass

#Main Program
s1=Student() # Here s1 is called Object
s2=Student() # Here s2 is called  Object
print("ID of s1 Object=",id(s1))
print("ID of s2 Object=",id(s2))
print("Content of s1={} and Number of Values={}".format(s1.__dict__, len(s1.__dict__)))
print("Content of s2={} and Number of Values={}".format(s2.__dict__, len(s2.__dict__)))
print("----------------------------------------------")
#Add the Instance Data--sno,name and marks  to s1 Object
s1.sno=100
s1.name="Rossum"
s1.marks=34.56
#Add the Instance Data ---sno,name and marks --to s2 Object
s2.stno=200
s2.sname="Travis"
s2.marks=14.56
s2.addr="HYD"
print("First Student Data")
print("----------------------------------------------")
print("Content of s1={} and Number of Values={}".format(s1.__dict__, len(s1.__dict__)))
print("----------------------------------------------")
print("Second Student Data")
print("----------------------------------------------")
print("Content of s2={} and Number of Values={}".format(s2.__dict__, len(s2.__dict__)))
print("----------------------------------------------")