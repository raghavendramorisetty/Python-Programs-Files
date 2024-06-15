# RegExpr1.py
import re

gd = "Python is an oop lang.python is also fun lang"
# gd="Python is an oop lang.Python is also fun lang"
sp = "Python"
lst = re.findall(sp, gd)
print(lst)
for val in lst:
    print(val)
print(" {} times '{}' Found".format(len(lst), sp))
