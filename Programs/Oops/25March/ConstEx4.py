#Program with Constructors
#ConstEx4.py
class Test:
    def __init__(self,x,y): # Parameterized constructor
        print("I am from Parameterized constructor")
        self.a=x
        self.b=y
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
        print("----------------------------")
#Main program
t1=Test(10,20)
t2=Test(100,200)
t3=Test(1000,2000)