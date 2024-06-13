#PolyEx3.py
class C1:
    def __init__(self): # Original Constructor
        print("C1--default constructor")
class C2(C1):
    def __init__(self): # Overridden Constructor
        print("C2--default constructor")
        super().__init__()

class C3(C2):
    def __init__(self): # Overridden Constructor
        print("C3--default constructor")
        super().__init__()

#Main Program
o3=C3() # Object Creation