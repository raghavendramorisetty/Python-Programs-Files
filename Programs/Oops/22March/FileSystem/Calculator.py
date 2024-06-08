# Calculator.py<----File Name and Module Name
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