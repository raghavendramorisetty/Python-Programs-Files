#Program for cal area of Different figures by using polymorphism
#PolyEx5.py
class Circle:  # Base Class
    def area(self): # Original Method
        self.r=float(input("Enter radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle:{}".format(self.ac))
        #super().area() This Gives AttributeError bcoz highest level object class does not contain area()
class Square(Circle):
    def area(self): # Overridden Method
        self.s=float(input("Enter Side:"))
        self.sa=self.s**2
        print("Area of Square={}".format(self.sa))
        print("=" * 50)
        super().area()
class Rect(Square):
    def area(self):  # Overridden Method
        self.l = float(input("Enter Length:"))
        self.b=float(input("Enter Breadth:"))
        self.ar=self.l*self.b
        print("Area of Rect={}".format(self.ar))
        print("="*50)
        super().area()

#Main Program
r=Rect()
r.area()