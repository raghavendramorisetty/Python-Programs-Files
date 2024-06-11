#Non-DestEx1.py
class Employee:
    def __init__(self,eno,ename):
        print("--------------------------------")
        print("I am from Parameterized constructor")
        self.eno=eno
        self.name=ename
        print("\tEmp Number:{}".format(self.eno))
        print("\tEmp Name:{}".format(self.name))
        print("--------------------------------")
#Main program
print("Program Execution Started")
eo1=Employee(100,"RS")
eo2=Employee(200,"TR")
eo3=Employee(300,"MC")
print("Program Execution Ended")