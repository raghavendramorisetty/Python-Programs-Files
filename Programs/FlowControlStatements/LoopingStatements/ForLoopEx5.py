#Program for Reading N Values and Display Those Values
#ForLoopEx5.py
n=int(input("Enter How Many Values u want to enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=list()  # Creating empty list for Holding Dynamic Reading Values
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of Values={}".format(lst))