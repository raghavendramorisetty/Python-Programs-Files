# Searching for all except Digits
#RegExpr19.py
import re
mattab=re.finditer(r"\D","a HK$Y p6Ld5@Z2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr19.py
--------------------------------------------
Start Index:0  End Index:1  Value:a
Start Index:1  End Index:2  Value:
Start Index:2  End Index:3  Value:H
Start Index:3  End Index:4  Value:K
Start Index:4  End Index:5  Value:$
Start Index:5  End Index:6  Value:Y
Start Index:6  End Index:7  Value:
Start Index:7  End Index:8  Value:p
Start Index:9  End Index:10  Value:L
Start Index:10  End Index:11  Value:d
Start Index:12  End Index:13  Value:@
Start Index:13  End Index:14  Value:Z
Start Index:15  End Index:16  Value:R
Start Index:16  End Index:17  Value:&
--------------------------------------------
"""