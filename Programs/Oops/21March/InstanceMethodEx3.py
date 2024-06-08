#Program adding of two Numbers by using Instance Methods
#InstanceMethodEx3.py
class Sum:
    def  getvals(self):
        self.a=float(input("Enter Value of a:"))
        self.b = float(input("Enter Value of b:"))
    def  addvalues(self):
        self.c=self.a+self.b
    def dispvals(self):
        print("sum({},{})={}".format(self.a,self.b,self.c))

#Main Program
s=Sum()
s.getvals()
s.addvalues()
s.dispvals()