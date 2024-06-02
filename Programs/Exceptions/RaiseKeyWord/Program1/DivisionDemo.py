#DivisionDemo.py<------Main Program--Phase-3
from Division import division
from Infinity import InfinityError
try:
	a=int(input("Enter First Value:"))
	b=int(input("Enter Second Value:"))
	try:
		res=division(a,b) # Function Call-----gives Result or Exception
	except InfinityError:
		print("\tDON'T ENTER ZERO DEN...")
	else:
		print("Div({},{})={}".format(a,b,res))
	finally:
		print("I am from finally block")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")