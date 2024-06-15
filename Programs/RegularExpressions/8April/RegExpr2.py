#RegExpr2.py
import re
gd="Python is an oop lang.Python is also fun lang"
sp="Python"
result=re.search(sp,gd) # here result is an object of NoneType or Match Class object
print(result)
if(result!=None):
	print("Start Index:{}".format(result.start()))
	print("End Index:{}".format(result.end()))
	print("Value:{}".format(result.group()))
	print("Search is Successful")
else:
	print("Search is Un-Successful")