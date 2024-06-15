# Searching for all Alpha-Numerics Only (Except Special Symbols)
#RegExpr14.py
import re
mattab=re.finditer("[A-Za-z0-9]","aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr14.py
--------------------------------------------
Start Index:0  End Index:1  Value:a
Start Index:1  End Index:2  Value:H
Start Index:2  End Index:3  Value:b
Start Index:3  End Index:4  Value:3
Start Index:4  End Index:5  Value:t
Start Index:5  End Index:6  Value:K
Start Index:7  End Index:8  Value:Y
Start Index:8  End Index:9  Value:p
Start Index:9  End Index:10  Value:6
Start Index:10  End Index:11  Value:c
Start Index:11  End Index:12  Value:Q
Start Index:12  End Index:13  Value:L
Start Index:13  End Index:14  Value:d
Start Index:14  End Index:15  Value:5
Start Index:16  End Index:17  Value:Z
Start Index:17  End Index:18  Value:s
Start Index:18  End Index:19  Value:v
Start Index:19  End Index:20  Value:O
Start Index:20  End Index:21  Value:2
Start Index:21  End Index:22  Value:R
--------------------------------------------
"""