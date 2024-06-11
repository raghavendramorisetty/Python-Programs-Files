#InhProg3.py
class C1:
    def geta(self):
        self.a=100
class C2(C1):
    def getb(self):
        self.b=200
    def operation(self):
        self.geta()
        self.getb()
        self.c=self.a+self.b
        print("sum({},{})={}".format(self.a,self.b,self.c))
#Main program
o2=C2()
o2.operation()