# Searching for  One or More  of Specified Value
#RegExpr22.py
import re
mattab=re.finditer("K+","KVKKVKKKVKV")
print("--------------------------------------------")
for mat in mattab:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("--------------------------------------------")


"""
--------------------------------------------
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr22.py
--------------------------------------------
Start Index:0  End Index:1  Value:K
Start Index:2  End Index:4  Value:KK
Start Index:5  End Index:8  Value:KKK
Start Index:9  End Index:10  Value:K
--------------------------------------------
"""