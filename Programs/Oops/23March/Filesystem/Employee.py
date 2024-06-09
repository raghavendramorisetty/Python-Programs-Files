#Employee.py<----File Name and Module Name
class Employee:
    def  getempvals(self,eno,ename,sal,dsg):
        self.eno=eno
        self.name=ename
        self.sal=sal
        self.dsg=dsg
    def  dispempvals(self):
        print("\t{}\t{}\t{}\t{}".format(self.eno,self.name,self.sal,self.dsg))