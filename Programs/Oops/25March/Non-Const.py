#Program without Constructors
class Employee:
    def readempdata(self):
        self.eno=100
        self.ename="RS"
        self.sal=2.3

#Main program
e=Employee()
print("Initial Content of e=",e.__dict__)
e.readempdata() # Calling Instance Method Explicitly
print("Now Content of e=",e.__dict__)
