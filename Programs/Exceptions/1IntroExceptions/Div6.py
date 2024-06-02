#Program for Calculating Division of Two Numbers
#Div6.py
""" In 26th Feb 2024  KVR Programmer Defined This Program and Handles all types of specific Exceptions occurs in this program
After 5 Years Mayank is NEW Programmer , he is adding new Code as part of Maintenance activity. Due to that new Code there is
possibility of an exception may occur and that type of exception may not be knowing to mayank then how to handle that Future Exceptions
on 26th feb 2024 by KVR? (Solution: By using Default Block(me)) """
try:
		print("Program Execution Started")
		s1=input("Enter First Value:")
		s2=input("Enter Second Value:")
		#convert s1 and s2 into int type
		a=int(s1)#-----------------------------Exception generated stmt--ValueError
		b=int(s2)#-----------------------------Exception generated stmt--ValueError
		c=a/b #--------------------------------Exception generated stmt---ZeroDivisionError
		s="PYTHON" # Code added by Mayank
		print(s[2])
except ZeroDivisionError:
		print("\tDON'T ENTER ZERO FOR DEN....")
except ValueError:
		print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except IndexError:
		print("\tPlz Check Ur Index")
except:  # Default except
		print("Oooops Some thing went wrong")
else:
		print("*********else block*****")
		print("Val of a={}".format(a))
		print("Val of b={}".format(b))
		print("Div={}".format(c))
finally:
		print("i am from finally block---Program Execution Ended")

