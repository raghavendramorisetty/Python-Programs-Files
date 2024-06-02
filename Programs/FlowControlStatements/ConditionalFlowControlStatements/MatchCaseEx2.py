#Program for Implementing all Arithmetic Operations by using Match Case statement
#MatchCaseEx2.py
print("="*50)
print("\tArithmetic Operations")
print("="*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("="*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
	case 1:
		print("Enter Two Values for addition:")
		a,b=float(input()),float(input())
		print("\tSum({},{})={}".format(a,b,a+b))
	case 2:
		print("Enter Two Values for Substraction:")
		a,b=float(input()),float(input())
		print("\tSub({},{})={}".format(a,b,a-b))
	case 3:
		print("Enter Two Values for Multiplication:")
		a,b=float(input()),float(input())
		print("\tMul({},{})={}".format(a,b,a*b))
	case 4:
		print("*"*50)
		print("\t\tSub Menu-Division")
		print("*"*50)
		print("\t\t1.Normal Division")
		print("\t\t2.Floor Division")
		print("\t\t3.Exit")
		print("*"*50)
		ch1=int(input("Enter Ur Choice  Sub menu:"))
		match(ch1):
			case 1:
				print("Enter Two Values for Normal Division:")
				a,b=float(input()),float(input())
				print("\tNormal Div({},{})={}".format(a,b,a/b))
			case 2:
				print("Enter Two Values for Floor Division:")
				a,b=float(input()),float(input())
				print("\tFloor Div({},{})={}".format(a,b,a//b))
			case _:
				print("Ur Selection of Sub Menu is Wrong--Try again")
	case 5:
		print("Enter Two Values for Modulo Div:")
		a,b=float(input()),float(input())
		print("\tMod({},{})={}".format(a,b,a%b))
	case 6:
		a,b=float(input("Enter Base:")),float(input("Enter Power:"))
		print("\tPow({},{})={}".format(a,b,a**b))
	case 7:
		print("Thx for using Program")
	case _:
		print("Ur Selection of Operation is wrong--try again")
print("Program execution completed")