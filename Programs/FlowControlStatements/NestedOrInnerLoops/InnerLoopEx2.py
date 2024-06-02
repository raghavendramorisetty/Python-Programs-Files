#This Program demonstrates Inner Loops---while loop in while loop
#InnerLoopsEx2.py
i=1
while(i<=5):
    print("Value of i={}".format(i))
    print("-" * 50)
    j=1
    while(j<=3):
        print("\t\tValue of j={}".format(j))
        j=j+1
    else:
        i = i + 1
        print("\ti am out-off inner loop")
        print("-" * 50)
else:
    print("\ti am out-off outer loop")
    print("*" * 50)