#Program adding of two Numbers by using Instance Methods
#InstanceMethodEx4.py
class Sum:
    def  getvals(self):
        self.a=float(input("Enter Value of a:"))
        self.b = float(input("Enter Value of b:"))
    def  addvalues(self):
        self.c=self.a+self.b
    def dispvals(self):
        self.getvals()
        self.addvalues()
        print("sum({},{})={}".format(self.a,self.b,self.c))

#Main Program
s=Sum()
s.dispvals()
