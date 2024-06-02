#Program for Deomstrating Defualt Arguments
#DefualtArgsEx2.py
def  dispstudvals(sno,sname,marks,crs="PYTHON"): # here crs=PYTHON is called Default Argument
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("*"*50)
dispstudvals(10,"RS",45.67) # Function Call with Possitional Args
dispstudvals(20,"TR",55.67) # Function Call with Possitional Args
dispstudvals(30,"JH",57.68) # Function Call with Possitional Args
dispstudvals(40,"MC",85.69) # Function Call with Possitional Args
dispstudvals(50,"DT",85.69,"JAVA") # Function Call with Possitional Args
dispstudvals(60,"PT",25.69) # Function Call with Possitional Args
dispstudvals(70,"JB",65.69,"HTML") # Function Call with Possitional Args
print("*"*50)