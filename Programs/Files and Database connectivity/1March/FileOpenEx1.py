#Program for Demonstrating How the open the file in read mode
#FileReadEx1.py
import sys
try:
    fp=open("stud.data","r")
except FileNotFoundError:
    print("File does not Exist")
    #sys.exit() OR
else:
    print("File opened in read mode successfully")
    print("Type of fp=", type(fp))
    print("I am in else block--Is File Closed?=",fp.closed)
finally:
    print("I am from finally block")
    fp.close()
    print("Is File Closed?=",fp.closed)
    print("File closed")
