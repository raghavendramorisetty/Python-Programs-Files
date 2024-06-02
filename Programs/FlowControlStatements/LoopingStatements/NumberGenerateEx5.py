#Program for generating odd Numbers within n  where n is +ve
#NumberGenerateEx5.py
n=int(input("Enter How Many Even Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("*"*50)
    print("odd Numbers within {}".format(n))
    print("*"*50)
    i=1
    while(i<=n):
        print("\t{}".format(i))
        i=i+2
    else:
        print("*" * 50)
