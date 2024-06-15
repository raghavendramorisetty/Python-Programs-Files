# Searching for all except Lower Case Alphabets
#RegExpr9.py
import re
mattab=re.finditer("[^a-z]","aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
--------------------------------------------

E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr9.py
--------------------------------------------
Start Index:1  End Index:2  Value:H
Start Index:3  End Index:4  Value:3
Start Index:5  End Index:6  Value:K
Start Index:6  End Index:7  Value:$
Start Index:7  End Index:8  Value:Y
Start Index:9  End Index:10  Value:6
Start Index:11  End Index:12  Value:Q
Start Index:12  End Index:13  Value:L
Start Index:14  End Index:15  Value:5
Start Index:15  End Index:16  Value:@
Start Index:16  End Index:17  Value:Z
Start Index:19  End Index:20  Value:O
Start Index:20  End Index:21  Value:2
Start Index:21  End Index:22  Value:R
Start Index:22  End Index:23  Value:&
--------------------------------------------
"""