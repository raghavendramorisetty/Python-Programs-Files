#AnonymousFunEx4.py
def  isprime(n):
    if(n<=1):
        return "Invalid Input"
    else:
        res=True
        for i in range(2,n):
            if(n%i==0):
                res=False
                break
        if(res):
            return "PRIME"
        else:
            return "NOT PRIME"
#Anonymous Function
decide=lambda n: isprime(n)

#Main Program
n=int(input("Enter a Number:"))
res=decide(n)
print("{} is {}".format(n,res))