#Program for accepting Two Integer and find Big among them
#SimpleIfStmtEx1.py
a=int(input("Enter First Value:")) # a=10
b=int(input("Enter Second Value:")) # b=5
if (a>b):
    print("Big({},{})={}".format(a,b,a))
if (b>a):
    print("Big({},{})={}".format(a,b,b))
if (a==b):
    print("Both the Values are Equal")
print("Program execution Completed")