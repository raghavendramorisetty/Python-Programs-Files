#Program for accepting Two Values and decide Big
#IfElseStmtEx2.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
else:
    print("Big({},{})={}".format(a,b,b))
print("Program execution completed")
