#Program for Mul Table for +Ve Number
#ForLoopEx3.py
n=int(input("Enter Any Number:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("*"*40)
    print("Mul Table for {} ".format(n))
    print("*" * 40)
    for i in range(1,11):
        print("\t{} x {} = {}".format(n,i,n*i))
    else:
        print("*" * 40)
