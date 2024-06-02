#Program for Finding Sum of N Natural Numbers
#NatNumsSumEx1.py
n=int(input("Enter How Many Natural Numbers sum u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Natural Numbers within:{}".format(n))
    print("=" * 50)
    s=0
    i=1
    while(i<=n):
        print("\t\t{}".format(i))
        s = s + i  # Accumutaing Nat Number sum
        i=i+1
    else:
        print("=" * 50)
        print("Sum={}".format(s))
        print("=" * 50)