#Program for Reading N Values and Find sum and average of  Those Values
#ForLoopEx6.py
n=int(input("Enter How Many Values u want to enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=list()  # Creating empty list for Holding Dynamic Reading Values
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("----------------------------------------")
        print("List of Values={}".format(lst)) # lst=[10.0, 20.0, 30.0, 40.0, 50.0]
        print("----------------------------------------")
        #Code for finding sum and avg
        s=0
        for val in lst:
            print("\t{}".format(val))
            s=s+val
        else:
            print("----------------------------------------")
            print("Sum={}".format(s))
            print("Avg={}".format(s/len(lst)))
            print("----------------------------------------")