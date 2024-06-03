#Program for Defining Non-Decorator Program
#Non-DecEx1.py

def getval(): # here getval() defined by kvr
    return float(input("Enter Numerical value:"))

def squareroot(): # durga is asking me--sir give me square root of 5
    n=getval()
    res=n**0.5
    print("sqrt({})={}".format(n,res))

def square(): # Giridhran is asking --sir give me Square  of 5
    n=getval()
    res=n**2
    print("Square({})={}".format(n,res))

def cube(): # lohit is asking sir give me cube of 5
    n=getval()
    res=n**3
    print("cube({})={}".format(n,res))

#main program
squareroot()
square()
cube()
