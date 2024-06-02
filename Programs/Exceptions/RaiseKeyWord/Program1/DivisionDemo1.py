#DivisionDemo1.py<------Main Program--Phase-3
from Division import division
from Infinity import InfinityError
try:
	a=int(input("Enter First Value:"))
	b=int(input("Enter Second Value:"))
	res=division(a,b) # Function Call-----gives Result or Exception
except InfinityError:
	print("\tDON'T ENTER ZERO DEN...")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except:
	print("OOOPs some thing went wrong...")
else:
	print("Div({},{})={}".format(a,b,res))
finally:
	print("I am from finally block")