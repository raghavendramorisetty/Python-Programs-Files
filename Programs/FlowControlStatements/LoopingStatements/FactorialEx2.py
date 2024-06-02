#FactorialEx2.py
n=int(input("Enter a Number for calculating factorial:"))
if(n<0):
    print("{} is Invalid Input and can't cal Factorial".format(n))
else:
    fact=1
    i=n
    while(i>0):
        fact=fact*i
        i=i-1
    else:
        print("=" * 50)
        print("\t{}!={}".format(n,fact))
        print("=" * 50)