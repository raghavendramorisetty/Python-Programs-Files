#Program for demonstrating  Variable Length Arguments OR Parameters
#This Program will not execute as it is bcoz PVM Remembers Only Latest Function Definition due to its Interpretation Process.
#VarLenArgsEx1.py
def  disp(a,b,c,d,e): #Function Def-1 with 5 Possitional Params
	print(a,b,c,d,e)
def  disp(a,b,c,d): #Function Def-2 with 4 Possitional Params
	print(a,b,c,d)
def  disp(a,b,c): #Function Def-3 with 3 Possitional Params
	print(a,b,c)
def  disp(a,b): #Function Def-4 with 2 Possitional Params
	print(a,b)
def  disp(a): #Function Def-5 with 1 Possitional Params
	print(a)

#Main Program
disp(10,20,30,40,50) # Function call-1 with 5 Possitional Args
disp(10,20,30,40)#  Function call-2 with 4 Possitional Args
disp(10,20,30) #  Function call-3 with 3 Possitional Args
disp(10,20) #  Function call-4 with 2 Possitional Args
disp(10) #  Function call-5 with 1 Possitional Args