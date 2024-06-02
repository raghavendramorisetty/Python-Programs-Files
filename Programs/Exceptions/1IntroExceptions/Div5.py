#Program for Calculating Division of Two Numbers ---
#Div5.py---It is a Not recommended program
while(True):
	try:
		print("Program Execution Started")
		s1=input("Enter First Value:")
		s2=input("Enter Second Value:")
		#convert s1 and s2 into int type
		a=int(s1)#-----------------------------Exception generated stmt--ValueError
		b=int(s2)#-----------------------------Exception generated stmt--ValueError
		c=a/b #--------------------------------Exception generated stmt---ZeroDivisionError
	except :  # Default Except Block
		print("\t{}".format("Oooooops Some thing went wrong!!!--try again"))
	else:
		print("*********else block*****")
		print("Val of a={}".format(a))
		print("Val of b={}".format(b))
		print("Div={}".format(c))
		break
	finally:
		print("i am from finally block---Program Execution Ended")

