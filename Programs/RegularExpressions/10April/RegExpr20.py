# Searching for Word Characters
#RegExpr20.py
import re
mattab=re.finditer(r"\w","a HK$Y p6Ld5@Z2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr20.py
--------------------------------------------
Start Index:0  End Index:1  Value:a
Start Index:2  End Index:3  Value:H
Start Index:3  End Index:4  Value:K
Start Index:5  End Index:6  Value:Y
Start Index:7  End Index:8  Value:p
Start Index:8  End Index:9  Value:6
Start Index:9  End Index:10  Value:L
Start Index:10  End Index:11  Value:d
Start Index:11  End Index:12  Value:5
Start Index:13  End Index:14  Value:Z
Start Index:14  End Index:15  Value:2
Start Index:15  End Index:16  Value:R
--------------------------------------------
"""