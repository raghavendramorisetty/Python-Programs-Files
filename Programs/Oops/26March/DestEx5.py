#Program for Demonstrating Garbage Collector by calling Destructor
#DestEx5.py
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
        print("GC calls __del__ for Removing the memory of current object id:",id(self))
#Main program
print("Program Execution Started")
eo1=Employee(100,"RS")
print("No Longer Interested to maintain memory space of eo1 object")
time.sleep(5)
del eo1 # Makes GC to call destructor Forcefully

eo2=Employee(200,"TR")
print("No Longer Interested to maintain memory space of eo2 object")
time.sleep(5)
del eo2 # Makes GC to call destructor Forcefully

eo3=Employee(300,"MC")
print("No Longer Interested to maintain memory space of eo3 object")
time.sleep(5)
del eo3 # Makes GC to call destructor Forcefully

print("Program Execution Ended")