#Program for Deomstrating Defualt Arguments
#DefualtArgsEx3.py
def  dispstudvals(sno,sname,marks,crs="PYTHON",cnt="INDIA"): # here crs=PYTHON cnt="INDIA" are called Default Arguments
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*50)
dispstudvals(10,"RS",45.67) # Function Call with Possitional Args
dispstudvals(20,"TR",55.67) # Function Call with Possitional Args
dispstudvals(30,"JH",57.68) # Function Call with Possitional Args
dispstudvals(40,"MC",85.69) # Function Call with Possitional Args
dispstudvals(50,"DT",85.69,"JAVA","USA") # Function Call with Possitional Args
dispstudvals(60,"PT",25.69,"RSA") # Function Call with Possitional Args
dispstudvals(70,"JB",65.69,"HTML","USA") # Function Call with Possitional Args
dispstudvals(80,"MD",95.69,"DSC") # Function Call with Possitional Args
dispstudvals(90,"CV",45.69,cnt="AUS",crs="Django") # Function Call with Possitional Args
print("*"*50)