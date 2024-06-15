# Searching for Digits
#RegExpr18.py
import re
mattab=re.finditer(r"\d","a HK$Y p6Ld5@Z2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr18.py
--------------------------------------------
Start Index:8  End Index:9  Value:6
Start Index:11  End Index:12  Value:5
Start Index:14  End Index:15  Value:2
--------------------------------------------
"""