#Program for Reading the Values from KBD and place them list
#Non-CompehenEx1.py
n=int(input("Enter How Many Values u want to enter:"))
if(n<=0):
	print("{} is Invalid Input".format(n))
else:
	lst=[] # Empty List
	for i in range(1,n+1):
		value=float(input("Enter {} Value:".format(i)))
		lst.append(value)
	else:
		print("Content of List=",lst)