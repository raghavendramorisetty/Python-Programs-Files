#Program for Reading the Values from KBD and place them list
#Non-CompehenEx2.py
print("Enter Number of Values and Press @ to stop:")
lst=[]
while(True):
	value=input("Enter the values of list: ")
	if(value=="@"):
		break
	else:
		lst.append(float(value))
print("Content of List={}".format(lst))