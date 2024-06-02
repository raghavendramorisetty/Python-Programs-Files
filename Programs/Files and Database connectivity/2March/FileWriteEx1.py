#Program for Demonstrating How to write the data to the file
#FileWriteEx1.py
sno=400
sname="Travis"
marks=24.56
#choose File Name and open in write Mode
with open("students.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Student Data written to the file")

