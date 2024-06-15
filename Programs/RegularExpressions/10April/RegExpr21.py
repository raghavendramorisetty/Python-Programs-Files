# Searching for  all special symbols
#RegExpr21.py
import re
mattab=re.finditer(r"\W","a HK$Y p6Ld5@Z2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")


"""
--------------------------------------------
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr21.py
--------------------------------------------
Start Index:1  End Index:2  Value:
Start Index:4  End Index:5  Value:$
Start Index:6  End Index:7  Value:
Start Index:12  End Index:13  Value:@
Start Index:16  End Index:17  Value:&
--------------------------------------------
"""