#Program for generating n to 1 numbers where n is +ve
#NumberGenerateEx3.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("=" * 50)
    print("Number from {} to 1".format(n))
    print("=" * 50)
    i=n # Initlization Part
    while(i>=1): # test cond
        print("\t{}".format(i))
        i=i-1 # updation part
    else:
        print("="*50)

