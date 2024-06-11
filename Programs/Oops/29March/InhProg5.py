#InhProg5.py
class GrandParent:
    def getgrandparentprop(self):
        self.gpp=float(input("Enter Grand Parent Property:"))
class Parent(GrandParent):
    def getparentprop(self):
        self.pp=float(input("Enter Parent Property:"))
class Child(Parent):
    def getchildprop(self):
        self.cp=float(input("Enter Child Property:"))
    def gettotprop(self):
        self.getgrandparentprop()
        self.getparentprop()
        self.getchildprop()
        self.totprop=self.gpp+self.pp+self.cp
        print("------------------------------------")
        print("Grand Parent Property:",self.gpp)
        print("Parent Property:", self.pp)
        print("Child  Property:", self.cp)
        print("Total property of Child=",self.totprop)
        print("------------------------------------")

#Main program
co=Child()
co.gettotprop()