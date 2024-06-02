#MapEx4.pu
print("Enter List of Values Separated by Space for First List:")
lst1=[int(val) for val in input().split()] # lst=[11,12,13,14]
print("Enter List of Values Separated by Space for Second List:")
lst2=[int(val) for val in input().split()] # lst=[100,200,300,400]
sumlist=list(map(lambda x, y: x+y, lst1,lst2)) # Takes X from  lst1 and Y from lst2
print("List1\t\tList2\t\tSum List")
print("*"*50)
for n1,n2,sm in zip(lst1,lst2,sumlist):
    print("\t{}\t\t{}\t\t{}".format(n1,n2,sm))
print("*"*50)