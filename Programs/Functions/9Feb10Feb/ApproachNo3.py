#Write a Program for finding Sum of Two Numbers by using Functions
#ApproachNo3.py
#INPUT--------------------------->Taking From Function Call
#PROCESS :-------------------->Done in Function Body
#OUTPUT / RESULT :--------->Displayed in Function Body
def  sumop(k,v):
    r=k+v
    print("Sum({},{})={}".format(k,v,r))

#Main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
sumop(x,y) #Function Call