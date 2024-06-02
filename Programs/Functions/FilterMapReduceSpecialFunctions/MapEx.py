print("Enter List of Values Separated by Space for First List:")
lst1=[int(val) for val in input().split()] # lst1=[11,12,13,14]
print("Enter List of Values Separated by Space for Second List:")
lst2=[int(val) for val in input().split()] # lst2=[100,200]
if(len(lst1)>len(lst2)):  # List1 contains More Elements
        for i in range( len(lst1)-len(lst2)):
            lst2.append(0)
if(len(lst2)>len(lst1)):# List2 contains More Elements
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
#Add the elements lst1 and lst2
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("List1\t\tList2\t\tSum List")
print("*"*50)
for n1,n2,sm in zip(lst1,lst2,lst3):
    print("\t{}\t\t{}\t\t{}".format(n1,n2,sm))
print("*"*50)