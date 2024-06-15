# Searching for all Upper Case Alphabets
#RegExpr6.py
import re
mattab=re.finditer("[A-Z]","aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr6.py
--------------------------------------------
Start Index:1  End Index:2  Value:H
Start Index:5  End Index:6  Value:K
Start Index:7  End Index:8  Value:Y
Start Index:11  End Index:12  Value:Q
Start Index:12  End Index:13  Value:L
Start Index:16  End Index:17  Value:Z
Start Index:19  End Index:20  Value:O
Start Index:21  End Index:22  Value:R
--------------------------------------------
"""