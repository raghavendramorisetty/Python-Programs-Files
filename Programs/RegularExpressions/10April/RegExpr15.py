# Searching for all Special Symbols
#RegExpr15.py
import re
mattab=re.finditer("[^A-Za-z0-9]","aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
--------------------------------------------
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr15.py
--------------------------------------------
Start Index:6  End Index:7  Value:$
Start Index:15  End Index:16  Value:@
Start Index:22  End Index:23  Value:&
--------------------------------------------
"""