#Program for generating 1 to n numbers where n is +ve
#NumberGenerateEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("*"*50)
    print("Numbers within:{}".format(n))
    print("*" * 50)
    i=1 # Initlization Part
    while(i<=n): # test cond
        print("\t{}".format(i))
        i=i+1 # Updation Part
    else:
        print("-"*50)