#FromImportSyntax2.py----from module name import global vars as alias name,function names as alias name,class names as alias name
from icici import bname as ib ,addr as a,simpleint as si
from MathsInfo import PI,E,bname as hb
from Aop import mulop as mp
print("Bank Name:",ib)
print("bank Addr:",a)
si()  # Function call
print("-------------------------------------")
print("Val of PI=",PI)
print("Val of E=",E)
print("Bank name=",hb)
print("-------------------------------------")
mp(10,20)