#This Program demonstrates Inner Loops---for loop in for loop
#InnerLoopsEx1.py
for i in range(1,6):
    print("Value of i={}".format(i))
    print("-"*50)
    for j in range(1,4):
        print("\t\tValue of j={}".format(j))
    else:
        print("\ti am out-off inner loop")
        print("-" * 50)
else:
    print("\ti am out-off outer loop")
    print("*" * 50)