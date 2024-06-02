#ImportStmtSyntax4.py---import module name1 as alias name,module name2 as alias name,....module name-n as alias name
import icici as k ,MathsInfo as v, Aop as r
print("Bank Name:",k.bname)
print("bank Addr:",k.addr)
k.simpleint()  # Function call
print("-------------------------------------")
print("Val of PI=",v.PI)
print("Val of E=",v.E)
print("-------------------------------------")
r.addop(10,20)
r.subop(100,200)