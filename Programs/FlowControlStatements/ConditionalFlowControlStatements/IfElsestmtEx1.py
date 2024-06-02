#Program for accepting a number and decide whether It is +ve or -ve or zero by using if..else statement
#IfElseStmtEx1.py
n=int(input("Enter a Number:"))
if(n>0):
    print("\t{} is +VE".format(n))
else:
    if(n==0):
        print("{} is ZERO".format(n))
    else:
        print("{} is -VE".format(n))
print("Program execution completed")