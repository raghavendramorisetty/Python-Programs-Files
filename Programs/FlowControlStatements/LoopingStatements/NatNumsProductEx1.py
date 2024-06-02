#Program for Finding product of N Natural Numbers
#NatNumsProductEx1.py
n=int(input("Enter How Many Natural Numebrs Product u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Natural Numbers within:{}".format(n))
    print("=" * 50)
    p=1
    i=1
    while(i<=n):
        print("\t\t{}".format(i))
        p = p * i  # Accumulaing Nat Number Product
        i=i+1
    else:
        print("=" * 50)
        print("Product={}".format(p))
        print("=" * 50)