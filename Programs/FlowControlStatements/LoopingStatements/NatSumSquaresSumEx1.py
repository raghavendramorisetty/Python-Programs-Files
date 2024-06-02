#Program for Finding Sum of Squares and Cubes  N Natural Numbers
#NatNumsSquaresSumEx1.py
n=int(input("Enter How Many Natural Numebrs sum u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s,ss,cs=0,0,0
    print("="*70)
    print("Natural Numbers within:{}".format(n))
    print("=" * 70)
    print("Nat Nums\t\tSquares of Nat Nums\t\tCubes of Nat Naums")
    print("=" * 70)
    i=1
    while(i<=n):
        print("\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("=" * 70)
        print("\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(s,ss,cs))
        print("=" * 70)