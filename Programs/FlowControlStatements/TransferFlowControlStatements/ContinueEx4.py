#To print positive number elements and negative elements seperately
#ContinueEx4.py
n=int(input("Enter How Many Values u want to enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=list()  # Creating empty list for Holding Dynamic Reading Values
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        poslist = [] # For Storing +ve Values
        for val in lst:
            if (val <= 0):
                continue
            poslist.append(val)
        else:
            print("Given List ={}".format(lst))
            print("Possitive Elements={}".format(poslist))
            neglist = list() # For Storing  -ve Values
            for val in lst:
                if (val >= 0):
                    continue
                neglist.append(val)
            else:
                print("Negative Elements={}".format(neglist))