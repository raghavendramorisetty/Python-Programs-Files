#This Program demonstrates Inner Loops---for loop in while loop
#InnerLoopsEx4.py
i=1
while(i<=5): # outer loop
    print("Value of i={}".format(i))
    print("-" * 50)
    for j in range(3,0,-1): # Inner Loop
        print("\t\tValue of j={}".format(j))
    else:
        i = i + 1
        print("\ti am out-off inner loop")
        print("-" * 50)
else:
    print("\ti am out-off outer loop")
    print("*" * 50)