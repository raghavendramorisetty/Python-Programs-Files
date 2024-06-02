#Write a Program for finding Sum of Two Numbers by using Functions
#ApproachNo1.py
#INPUT--------------------------->Taking From Function Call
#PROCESS :-------------------->Done in Function Body
#OUTPUT / RESULT :--------->Displayed in Function call
def  sumop(a,b): # Here 'a' and 'b' are called Formal Parameters
    c=a+b  # Here 'c' is called Local variable
    return c
#main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
z=sumop(x,y) # Function Call
print("Sum({},{})={}".format(x,y,z))
print("==================================")
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=sumop(a,b) # Function Call
print("sum({},{})={}".format(a,b,c))
