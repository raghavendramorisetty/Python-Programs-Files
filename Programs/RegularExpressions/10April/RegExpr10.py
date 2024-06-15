# Searching for all  Digits
#RegExpr10.py
import re
mattab=re.finditer("[0-9]","aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr10.py
--------------------------------------------
Start Index:3  End Index:4  Value:3
Start Index:9  End Index:10  Value:6
Start Index:14  End Index:15  Value:5
Start Index:20  End Index:21  Value:2
--------------------------------------------
"""