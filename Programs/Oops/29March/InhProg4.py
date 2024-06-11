#InhProg4.py
class Parent:
    def getparentprop(self):
        self.pp=float(input("Enter Parent Property:"))
class Child(Parent):
    def getchildprop(self):
        self.cp=float(input("Enter Child Property:"))
    def gettotprop(self):
        self.getparentprop()
        self.getchildprop()
        self.totprop=self.pp+self.cp
        print("Total property of Child=",self.totprop)

#Main program
co=Child()
co.gettotprop()