#MapEx3.py
print("Enter List of Old Salaries Values Separated by Space:")
sallst=[int(val) for val in input().split() if int(val)>0]
newsallist=list(map(lambda sal: sal*1.50,sallst))
print("*"*50)
print("Given Elements\t\tSquares")
print("*"*50)
for osal,nsal in zip(sallst,newsallist):
    print("\t\t\t{}\t\t\t\t{}".format(osal,nsal))
print("*"*50)