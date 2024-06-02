#ListReverseWords.py
n=int(input("Enter How Many Words u want: "))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        num=input("Enter {} Value:".format(i))
        lst.append(num)
    else:
        print("Given List of Values:{}".format(lst)) # ['Apple', 'Mango', 'Kiwi', 'Sberry', 'Guava']
        print("-------------------------------")
        for i in range(0,len(lst)):
            lst[i]=lst[i][::-1]
        else:
            print("reversed Values of list are:{}".format(lst))
