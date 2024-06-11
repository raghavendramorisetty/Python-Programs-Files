#Program for Demonstrating Garbage Collector by calling Destructor
#DestEx7.py
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
eo2=eo1 #Deep Copy
eo3=eo1 # deep Copy
print("No Longer Interested to maintain memory space of eo1 object")
time.sleep(5)
del eo1 #  GC never call destructor Forcefully bcoz eo2 and eo3 points the object

print("No Longer Interested to maintain memory space of eo2 object")
time.sleep(5)
del eo2 # GC never call destructor Forcefully bcoz  eo3 points the object

print("No Longer Interested to maintain memory space of eo3 object")
time.sleep(5)
del eo3# Makes GC to call destructor Forcefully bcoz no more objects points memory space

print("Program Execution Ended")
#Automatic Garbage Collection