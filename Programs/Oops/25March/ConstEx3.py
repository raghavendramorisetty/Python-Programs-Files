#Program with Constructors
#ConstEx3.py
class Test:
    def __init__(self): # Default constructor
        print("I am from Default constructor")
        self.a=10
        self.b=20
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
        print("----------------------------")
#Main program
t1=Test()
t2=Test()
t3=Test()