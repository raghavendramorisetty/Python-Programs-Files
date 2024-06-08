#Program for String sno,sname and marks of a Student
#InstanceDataMembersEx1.py
class student:pass

# Main Program
s1=student() #Here s1 is called object of student
s2=student() # here s2 is called object of student
print("ID of s1 object=",id(s1))
print("ID of s2 object=",id(s2))
print("--------------------------------------------")
#Add the Instance Data--sno, sname and marks to s1 object
s1.sno=100
s1.name="Rossum"
s1.marks=34.56
#Add the Instance Data---sno,name and marks --to s2 object
s2.sno=200
s2.name="Travis"
s2.marks=14.56
print("First Student Data")
print("----------------------------------------------")
print("Student Number=",s1.sno)
print("Student Name=",s1.name)
print("Student Marks=",s1.marks)
print("----------------------------------------------")
print("Second Student Data")
print("----------------------------------------------")
print("Student Number=",s2.sno)
print("Student Name=",s2.name)
print("Student Marks=",s2.marks)
print("----------------------------------------------")