#ReduceEx1.py
import functools
print("Enter List of Values Separated by space for finding sum:")
lst=[int(val) for val in input().split()]
res=functools.reduce(lambda x,y: x+y, lst)
print("sum({})={}".format(lst,res))
#---------------------------------------------------------
def sumop(x,y): # Normal Function Def
    return(x+y)
#Main program
print("Enter List of Values Separated by space for finding:")
lst=[int(val) for val in input().split()]
res=functools.reduce(sumop, lst)
print("sum({})={}".format(lst,res))