#program for deciding whether the Number is Prime or Not
#BreakEx4.py
n=int(input("Enter a Number to decide whether It is Prime Or Not:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    if(res):
        print("{} is Prime number".format(n))
    else:
        print("{} is Not a Prime Number".format(n))