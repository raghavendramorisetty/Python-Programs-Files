#KwdArgsEx2.py
def   disp(A,B,C,D,City="HYD"):
	print("\t{}\t{}\t{}\t{}\t{}".format(A,B,C,D,City))


#main program
print("*"*50)
print("\tA\tB\tC\tD\tCity")
print("*"*50)
disp(10,20,30,40)#Function call with Possitional Args
disp(C=30,D=40,B=20,A=10)#Function call with Keywords Args
disp(B=20,D=40,A=10,C=30) #Function call with Keywords Args
disp(10,20,D=40,C=30) #Function call with Possitional Args and Keywords Args
#disp(C=30,10,D=40,B=20)  SyntaxError: positional argument follows keyword argument
disp(C=30,A=10,D=40,B=20) #Function call with Possitional Args and Keywords Args
disp(10,20,City="BANG",D=40,C=30)#Function call with Possitional Args and Keywords Args and Default args
print("*"*50)