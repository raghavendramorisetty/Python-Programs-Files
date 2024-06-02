#Program for accepting the 3 values and find Biggest and check for equality
#IfElseStmtEx4.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=float(input("Enter Third Value:"))
if(b<=a>c):
    print("big({},{},{})={}".format(a,b,c,a))
else:
    if(a<b>=c):
        print("big({},{},{})={}".format(a, b, c, b))
    else:
        if(b<c>=a):
            print("big({},{},{})={}".format(a, b, c, c))
        else:
            print("All values are equal")

