#Program with Constructors
#ConstEx2.py
class Employee:
    def __init__(self,eno,name,sal): # Parameterized Constructor
        print("------------------------------------")
        print("I am from Parameterized Constructor")
        self.eno=eno
        self.ename=name
        self.sal=sal
        print("Emp Number={}".format(self.eno))
        print("Employee Name:{}".format(self.ename))
        print("Employee Salary:{}".format(self.sal))
        print("------------------------------------")


#Main program
eo1=Employee(100,"RS",3.4) # Object Creation--makes the PVM to call Parametrized Constructor
eo2=Employee(200,"TR",4.5)# Object Creation--makes the PVM to call Parametrized Constructor
