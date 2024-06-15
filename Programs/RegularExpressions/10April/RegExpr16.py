# Searching for all Space Characters
#RegExpr16.py
import re
mattab=re.finditer(r"\s","a HK$Y p6Ld5@Z2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")


"""--------------------------------------------

E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr16.py
--------------------------------------------
Start Index:1  End Index:2  Value:
Start Index:6  End Index:7  Value:
--------------------------------------------"""
