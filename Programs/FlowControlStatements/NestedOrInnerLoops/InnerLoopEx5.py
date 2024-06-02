#Program for generating 1 to n multiplication tables
#InnerLoopsEx5.py
n=int(input("Enter How Many Mul tables u want:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    for num in range(1,n+1): # Outer Loop--Supply Number
        print("*"*50)
        print("\tMul Table for {}".format(num))
        print("*" * 50)
        for i in range(1,11):#Inner Loop--generates Mul table for number supplied by outer loop
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("*" * 50)