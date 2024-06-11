#PloyEx1.py
class Dog:
    def sound(self): # Original Method
        print("Dog says Bow Bow ")
class Cat(Dog):
    def sound(self): # Overridden Method
        print("Cat Says Meow Meow")
        super().sound()

class Human(Cat):
    def sound(self):# Overridden Method
        print("Human says Python Python")
        super().sound()
#main program
print("w.r.t Human class")
c=Human()
c.sound()