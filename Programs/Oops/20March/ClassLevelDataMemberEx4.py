#Program for String sno,sname, marks and Course and city for all students
#ClassLevelDataMemberEx4.py
class Student:
    city="HYD" # Here city is called Class Level Data Member

#Main Program
Student.crs="PYTHON" # Specifying Class Level Data Member
s1=Student()
s2=Student()
#Add the Instance Data--sno,name and marks  to s1 Object
s1.sno=int(input("Enter First Student Number:"))
s1.name=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:"))
#Add the Instance Data ---sno,name and marks --to s2 Object
s2.sno=int(input("Enter Second Student Number:"))
s2.name=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:"))
print("----------------------------------------------")
print("First Student Data")
print("----------------------------------------------")
print("Student Number=",s1.sno)
print("Student Name=",s1.name)
print("Student Marks=",s1.marks)
print("Student COURSE NAME=",Student.crs) # Accessing Class Level Data Members  w.r.t Class Name
print("Student CITY NAME=",Student.city) # Accessing Class Level Data Members  w.r.t Class Name
print("----------------------------------------------")
print("Second Student Data")
print("----------------------------------------------")
print("Student Number=",s2.sno)
print("Student Name=",s2.name)
print("Student Marks=",s2.marks)
print("Student COURSE NAME=",Student.crs) # Accessing Class Level Data Members  w.r.t Class  Name
print("Student CITY NAME=",Student.city) # Accessing Class Level Data Members  w.r.t Class Name
print("----------------------------------------------")