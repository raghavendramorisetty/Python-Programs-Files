# RegExpr3.py
import re

gd = "Python is an oop lang.Python is also fun lang"
sp = "Python"
mattab = re.finditer(sp, gd)
print(mattab)
print("Type of mattab object=", type(mattab))  # <class 'callable_iterator'>
print("--------------------------------------------------------")
for mat in mattab:  # here mat is an obj of <class, re.match>
    print("start Index:{}  End Index:{} Value:{}".format(mat.start(), mat.end(), mat.group()))
print("--------------------------------------------------------")
