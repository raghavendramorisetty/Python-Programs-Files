#Program for Demonstrating How to write the data to the file
#FileWriteEx2.py
sno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
marks=float(input("Enter Student Marks:"))
#Choose File Name and Open in write Mode
with open("students.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Student Data written to the file")

