# Searching for all Lower  Case Alphabets
# RegExpr8.py
import re

mattab = re.finditer("[a-z]", "aHb3tK$Yp6cQLd5@ZsvO2R&")
print("--------------------------------------------")
for mat in mattab:
    print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(), mat.end(), mat.group()))
print("--------------------------------------------")

"""
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr8.py
--------------------------------------------
Start Index:0  End Index:1  Value:a
Start Index:2  End Index:3  Value:b
Start Index:4  End Index:5  Value:t
Start Index:8  End Index:9  Value:p
Start Index:10  End Index:11  Value:c
Start Index:13  End Index:14  Value:d
Start Index:17  End Index:18  Value:s
Start Index:18  End Index:19  Value:v
--------------------------------------------
"""
