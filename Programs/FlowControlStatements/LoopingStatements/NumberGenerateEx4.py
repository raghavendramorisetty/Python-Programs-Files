#Program for generating Even Numbers within n  where n is +ve
#NumberGenerateEx4.py
n=int(input("Enter How Many Even Numbers u want to generate:"))
if(n<0):
    print("{} is Invalid input".format(n))
else:
    print("*"*50)
    print("Even Numbers within {}".format(n))
    print("*"*50)
    i=0
    while(i<=n):
        print("\t{}".format(i))
        i=i+2
    else:
        print("*" * 50)
