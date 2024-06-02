#program for deciding whether the Number is Prime or Not
#BreakEx3.py
n=int(input("Enter a Number to decide whether It is Prime Or Not:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    res="Prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not Prime"
            break

    if(res=="Prime"):
        print("{} is Prime number".format(n))
    else:
        print("{} is Not a Prime Number".format(n))