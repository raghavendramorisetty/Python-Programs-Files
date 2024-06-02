#Division.py<-----File Name and Module Name
from Infinity import InfinityError
def  division(a,b):
	if(b==0):
		raise InfinityError # raise kwd is used for Hitting or generating the exception by the PVM when cond satisfied
	else:
		return (a/b)
#Development of common Function where It can Raises the exception by using raise--Phase-II