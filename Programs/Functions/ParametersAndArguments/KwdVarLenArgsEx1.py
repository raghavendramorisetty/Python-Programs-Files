#Program for Demonstrating  Key Word Variable Length Arguments OR Parameters
#This Program will not execute as it is bcoz PVM Remembers Only Latest Function Definition due to its Interpretation Process.
#KwdVarLenArgsEx1.py
def  dispvals(sno,sname,marks):
	print(sno,sname,marks)

def  dispvals(bno,bname,price,pub):
	print(bno,bname,price,pub)

def  dispvals(tno,tname,subject1,subject2,subject3):
	print(tno,tname,subject1,subject2,subject3)

#main Program
dispvals(sno=10,sname="RS",marks=67.68) # Function Call-1 with 3 key word args
dispvals(bno=100,bname="PYTHON",price=345,pub="TaTa-Mcgh") # Function Call-2 with 4 key word args
dispvals(tno=200,tname="TR",subject1="Django",subject2="HTML",subject3="Java") # Function Call-2 with 5 key word args