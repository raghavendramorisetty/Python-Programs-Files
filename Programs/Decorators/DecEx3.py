#Program for Defining  for Cal Square Root of Value returned by Normal Function by using Decorator
#DecEx3.py
def squareroot(gv):
    def compute():
        n=gv()
        res=n**0.5
        return n,res
    return compute

@squareroot
def getval(): # Here getval() defined by kvr
    return float(input("Enter Numerical value:"))

#Main program
n,result=getval() #Normal Function call
print("SquareRoot({})={}".format(n,result))

