#Program for generating  List of Primes within the given Range -n
#InnerLoopsEx7.py
n=int(input("Enter Number to get List of Primes within its Range(Including itself):"))
if(n<=1):
    print("{} is Invalid".format(n))
else:
    primeslist=list()
    for num in range(2,n+1): # Outer Loop--supply Number
        res=True
        for i in range(2,num):# Inner Loop---decides the number is prime or not
            if(num%i==0):
                res=False
                break
        if(res):
            primeslist.append(num)
    else:
        print("List of Primes within {}={}".format(n,primeslist))