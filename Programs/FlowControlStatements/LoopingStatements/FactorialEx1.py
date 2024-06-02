#FactorialEx1.py
n=int(input("Enter a Number for calculating factorial:"))
if(n<0):
    print("{} is Invalid Input and can't cal Factorial".format(n))
else:
    fact=1
    i=1
    while(i<=n):
        #print("\t\t{}".format(i))
        fact = fact * i
        i=i+1
    else:
        print("=" * 50)
        print("Factorial({})={}".format(n,fact))
        print("=" * 50)