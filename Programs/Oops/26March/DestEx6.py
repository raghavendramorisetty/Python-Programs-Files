#Program for Demonstrating Garbage Collector by calling Destructor
#DestEx6.py
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
print("Program Execution Ended")
#Automatic Garbage Collection