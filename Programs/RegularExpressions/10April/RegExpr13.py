# searching for all  except Alphabets
#RegExpr13.py
import re
mattab=re.finditer("[^A-Za-z]","aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
--------------------------------------------

E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr13.py
--------------------------------------------
Start Index:3  End Index:4  Value:3
Start Index:6  End Index:7  Value:$
Start Index:9  End Index:10  Value:6
Start Index:14  End Index:15  Value:5
Start Index:15  End Index:16  Value:@
Start Index:20  End Index:21  Value:2
Start Index:22  End Index:23  Value:&
--------------------------------------------
"""