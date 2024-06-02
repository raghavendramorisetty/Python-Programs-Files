#Program for Demonstrating  Key Word Variable Length Arguments OR Parameters
#This Program will  execute as it is  bcoz we are using Key Word Variable Length Arguments OR Parameters
#PureKwdVarLenArgsEx2.py

def   dispvals(**kvr): #  here **kvr is called Keyword Var Length Parameter and **kvr is of type <class,dict>
	for key,val in kvr.items():
		print("\t{}-->{}".format(key,val))
	print("Number of Vals=",len(kvr))
	print("----------------------------------------------")

#main Program
dispvals(sno=10,sname="RS",marks=67.68) # Function Call-1 with 3 key word var leng  args
dispvals(bno=100,bname="PYTHON",price=345,pub="TaTa-Mcgh") # Function Call-2 with 4 key word  var leng  args
dispvals(tno=200,tname="TR",subject1="Django",subject2="HTML",subject3="Java") # Function Call-2 with 5 key word  var leng args
dispvals()