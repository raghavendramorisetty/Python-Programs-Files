# Searching for either "a" or "b" or "c" Only
# RegExpr4.py
import re

# gd="aHb3tK$Yp6cQLd5@ZsvO2R&"
# sp="[abc]"   #  OR    sp=re.compile(r"[abc]")
# mattab=re.finditer(sp,gd)
#	OR
mattab = re.finditer("[abc]", "aHb3tK$Yp6cQLd5@ZsvO2R&a")
print("--------------------------------------------")
for mat in mattab:
    print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(), mat.end(), mat.group()))
print("--------------------------------------------")

"""
--------------------------------------------
E:\KVR-PYTHON-6PM\REG EXPR>py RegExpr4.py
--------------------------------------------
Start Index:0  End Index:1  Value:a
Start Index:2  End Index:3  Value:b
Start Index:10  End Index:11  Value:c
Start Index:23  End Index:24  Value:a
--------------------------------------------
"""
