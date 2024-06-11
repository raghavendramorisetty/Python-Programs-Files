#Program with Constructors
#ConstEx1.py
class Employee:
    def __init__(self): # Default Constructor
        print("I am from Defualt Constructor")
        self.eno=100
        self.ename="RS"
        self.sal=2.3
        print("Emp Number={}".format(self.eno))
        print("Employee Name:{}".format(self.ename))
        print("Employee Salary:{}".format(self.sal))
        print("------------------------------------")

#Main Program
eo1=Employee() # Object Creation--Makes the PVM call Default Constructor
eo2=Employee() # Object Creation--Makes the PVM call Default Constructor
eo3=Employee() # Object Creation--Makes the PVM call Default Constructor