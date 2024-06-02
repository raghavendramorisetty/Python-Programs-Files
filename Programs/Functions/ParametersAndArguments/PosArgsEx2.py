#Program for Deomstrating Possitional Arguments
#PosArgsEx2.py
def  dispstudvals(sno,sname,marks,crs):
	print("\t{}\t\t{}\t\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCRS")
print("*"*50)
dispstudvals(10,"RS",45.67,"PYTHON") # Function Call with Possitional Args
dispstudvals(20,"TR",55.67,"PYTHON") # Function Call with Possitional Args
dispstudvals(30,"JH",57.68,"PYTHON") # Function Call with Possitional Args
dispstudvals(40,"MC",85.69,"PYTHON") # Function Call with Possitional Args
print("*"*50)