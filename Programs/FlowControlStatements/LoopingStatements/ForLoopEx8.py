#Program for Reading N Values and sort  Those Values
#ForLoopEx8.py
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
        print("List of Values in ASCENDING ORDER")
        lst.sort()
        for val in lst:
            print("\t\t{}".format(val))
        print("Max Value=",lst[-1])
        print("Min Value=", lst[0])
        print("List of Values in DECENDING ORDER")
        lst.sort(reverse=True)
        for val in lst:
            print("\t\t{}".format(val))
