#Program for performing arithmetic operations by using static method
#StaticMethodEx7.py
class Numbers:
    def readvalues(self):
        self.a = float(input("Enter First Value:"))
        self.b = float(input("Enter Second Value:"))
        self.op = input("Enter Arithmetic Operation Symbols:")
class Calculator:
    @staticmethod
    def operation(obj):
        match(obj.op):
            case "+":
                print("Sum({},{})={}".format(obj.a,obj.b,obj.a+obj.b))
            case "-":
                print("Sub({},{})={}".format(obj.a, obj.b, obj.a - obj.b))
            case "*":
                print("Mul({},{})={}".format(obj.a, obj.b, obj.a * obj.b))
            case "/":
                print("Div({},{})={}".format(obj.a, obj.b, obj.a / obj.b))
            case "//":
                print("FloorDiv({},{})={}".format(obj.a, obj.b, obj.a // obj.b))
            case "%":
                print("Mod({},{})={}".format(obj.a, obj.b, obj.a % obj.b))
            case "**":
                print("pow({},{})={}".format(obj.a, obj.b, obj.a ** obj.b))
            case _:
                print("Ur Selection of Operation is wrong-try again")
#Main program
n=Numbers()
n.readvalues()
#Calling static method and pass object n
Calculator.operation(n)