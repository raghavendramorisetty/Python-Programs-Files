#Program for Demonstrating Garbage Collector by calling Destructor
#DestEx1.py
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
        print("GC Calls __del__ and Memory Space Removed of object id:",id(self))
#Main program
print("Program Execution Started")
eo1=Employee(100,"RS")
eo2=Employee(200,"TR")
eo3=Employee(300,"MC")
print("Program Execution Ended")
time.sleep(5)