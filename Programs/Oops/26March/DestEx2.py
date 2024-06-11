#Program for Demonstrating Garbage Collector by calling Destructor
#DestEx2.py
import sys
import time
class Employee:
    def __init__(self,eno,ename):
        print("--------------------------------")
        print("I am from Parameterized constructor")
        self.eno=eno
        self.name=ename
        print("\tEmp Number:{}".format(self.eno))
        print("\tEmp Name:{}".format(self.name))
        print("--------------------------------")
    def __del__(self):
        global tm
        print("GC calls __del__ for Removing the memory of current object id:",id(self))
        tm=tm-sys.getsizeof(self)
        print("Now memory Space of all objects is = ", tm)


#Main program
print("Program Execution Started")
eo1=Employee(100,"RS")
eo2=Employee(200,"TR")
eo3=Employee(300,"MC")
#Find the memory space of all objects
tm=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("Total memory Spaces all objects= ",tm)#144
print("Program Execution Ended")
time.sleep(3)
#Automatic Garbage Collection