#InhProg1.py
class C1: # Here C1 is Base Class
    def disp1(self):
        print("C1--disp1--instance method")
class C2(C1): # Single Inheritance--here C2 is called Derived Class
    def disp2(self):
        print("C2--disp2--instance method")

#Main Program
o2=C2()
o2.disp1()
o2.disp2()