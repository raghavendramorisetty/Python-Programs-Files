#This Program demonstrates Inner Loops---while loop in for loop
#InnerLoopsEx3.py
for i in range(5,0,-1): # outer  loop
    print("Value of i={}".format(i))
    print("-"*50)
    j=3
    while(j>=1): # inner loop
        print("\t\tValue of j={}".format(j))
        j=j-1
    else:
        print("\ti am out-off inner loop")
        print("-" * 50)
else:
    print("\ti am out-off outer loop")
    print("*" * 50)