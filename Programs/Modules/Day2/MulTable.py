#Program for generaing Mul table for given Number
#MulTable.py---File Name and Acts as Module Name
def  table(n):
	if(n<=0):
		print("{} is Invalid Input".format(n))
	else:
		print("-"*50)
		print("Mul Table for {}".format(n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		print("-"*50)