#Program for generating Random multiplication tables based on Programmert Choice
#InnerLoopsEx6.py
n=int(input("Enter How Many Random Mul Tables u want: "))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        num=int(input("Enter {} Value:".format(i)))
        lst.append(num)
    else:
        print("Given List of Values:{}".format(lst))
        for num in lst: # Outer Loop
            if(num<=0):
                print("{} Invalid Input".format(num))
            else:
                print("*" * 50)
                print("\tMul Table for {}".format(num))
                print("*" * 50)
                for i in range(1, 11):  # Inner Loop--generates Mul table for number supplied by outer loop
                    print("\t{} x {}={}".format(num, i, num * i))
                else:
                    print("*" * 50)