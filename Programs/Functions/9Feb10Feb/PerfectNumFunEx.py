#PerfectNumFunEx.py
def perfect(n):
    if(n<=0):
        return ("{} is Invalid Input".format(n))
    else:
        s=0
        for i in range(1,(n//2)+1):
            if(n%i==0):
                s=s+i
        else:
            if(s==n):
                return ("{} is Perfect".format(n))
            else:
                return ("{} is Not Perfect".format(n))
#Main Program
n=int(input("Enter a Number for Deciding perfect or not: "))
res=perfect(n) # Function Call
print("\t{}".format(res))