#Program for demonstrating  Variable Length Arguments OR Parameters
#This Program will  execute as it is
#VarLenArgsEx2.py
def  disp(a,b,c,d,e): #Function Def-1 with 5 Possitional Params
	print(a,b,c,d,e)
disp(10,20,30,40,50) # Function call-1 with 5 Possitional Args
#-----------------------------------------------------------------------------------------
def  disp(a,b,c,d): #Function Def-2 with 4 Possitional Params
	print(a,b,c,d)
disp(10,20,30,40)#  Function call-2 with 4 Possitional Args
#-----------------------------------------------------------------------------------------
def  disp(a,b,c): #Function Def-3 with 3 Possitional Params
	print(a,b,c)
disp(10,20,30) #  Function call-3 with 3 Possitional Args
#-----------------------------------------------------------------------------------------
def  disp(a,b): #Function Def-4 with 2 Possitional Params
	print(a,b)
disp(10,20) #  Function call-4 with 2 Possitional Args
#-----------------------------------------------------------------------------------------
def  disp(a): #Function Def-5 with 1 Possitional Params
	print(a)
disp(10) #  Function call-5 with 1 Possitional Args


#The Limitation of the Above Process is that, If we have 100 Fun Calls then we must define 100 Definitions--Time Consuming Process
#To Eliminate the above problem---- we use var leng args---1000 Similar Fun Calls with Var args---Define Only 1 Fun Def.