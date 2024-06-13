# Program for cal area of Different figures by using polymorphism
# PolyEx13.py
class Circle:  # Base Class
    def __init__(self, r):  # Original Parameterized Constructor
        self.ac = 3.14 * r ** 2
        print("Area of Circle:{}".format(self.ac))


class Square:  # Base Class
    def __init__(self, s):  # Original Parameterized Constructor
        self.sa = s ** 2
        print("Area of Square={}".format(self.sa))
        print("=" * 50)


class Rect(Circle, Square):
    # def __init__(self):        # can be used if Default constructor is called in main program (me)
    #     super().__init__(float(input("Enter Radius:")))
    #     print("*" * 50)

    # def __init__(self,r=10):   # can be used if Default constructor or parameterised constructor(any one is okay) is called in main program (me)
    #     super().__init__(r)
    #     print("*" * 50)

    def __init__(self, r=0):pass      # Sir used this
    def area(self, l, b):  # Overridden Constructor
        self.ar = l * b
        print("Area of Rect={}".format(self.ar))
        print("*" * 50)
        super().__init__(float(input("Enter Radius:"))) # no need to use this if line above 17 or 21 is used
        print("*" * 50)
        Square.__init__(self, float(input("Enter Side:")))


# Main Program
# r=Rect(float(input("Enter Radius of Circle:"))) # Object Creation to call parameterized constructor
r = Rect() # Object Creation to call Default constructor
l = float(input("Enter Length:"))
b = float(input("Enter Breadth:"))
r.area(l, b)
