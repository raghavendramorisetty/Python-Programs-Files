#Program for Demonstrating  Key Word Variable Length Arguments OR Parameters
#This Program will  execute as it is  bcoz we are using Key Word Variable Length Arguments OR Parameters
#PureKwdVarLenArgsEx3.py
def  findtotals(sno,sname,cls,**submarks):
	print("*"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("*"*50)
	totmarks=0
	print("\tSubName\t\tMarks")
	print("*"*50)
	for subject,marks in submarks.items():
		print("\t{}\t\t{}".format(subject,marks))
		totmarks=totmarks+marks
	print("*"*50)
	print("\tTOTAL MARKS = {}".format(totmarks))
	print("*"*50)

#Main program
findtotals(100,"Shekar","X",Tel=60,Hindi=75,English=80,Maths=67,Science=78,Social=89)
findtotals(200,"Charan","12",Sankrit=75,English=80,Maths=69,Physics=60,Chemestry=60)
findtotals(300,"Rakesh","B.Tech",OS=56,DBMS=50,C=60)
findtotals(400,"Rossum","Research")
