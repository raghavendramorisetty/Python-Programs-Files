#Program for generating 1 to n numbers where n is +ve
#NumberGenerateEx1.py
# Input : n=5
# Output:  1 2 3 4 5
n=int(input("How Many numbers u want to generate:"))
i=1 # InitLization Part
while(i<=n): # Test Cond Part
    print("\t{}".format(i))
    i=i+1 # Updation Part
print("Program execution Completed")