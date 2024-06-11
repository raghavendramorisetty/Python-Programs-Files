#Program with Constructors
#ConstEx5.py
class Test:
    def __init__(self,x=1,y=2): # Default / Parameterized constructor
        print("I am from Default / Parameterized constructor")
        self.a=x
        self.b=y
        print("Val of a={}".format(self.a))
        print("Val of b={}".format(self.b))
        print("----------------------------")
#Main program
t1=Test()
t2=Test(10,20)
t3=Test(100)
t4=Test(y=200)
t5=Test(y=2000,x=1000)
print(t5.__dict__)
