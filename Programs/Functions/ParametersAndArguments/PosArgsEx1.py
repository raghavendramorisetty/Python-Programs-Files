#Program for Deomstrating Possitional Arguments
#PosArgsEx1.py
def  dispstudvals(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS")
print("*"*50)
dispstudvals(10,"RS",45.67) # Function Call with Possitional Args
dispstudvals(20,"TR",55.67) # Function Call with Possitional Args
dispstudvals(30,"JH",57.68) # Function Call with Possitional Args
dispstudvals(40,"MC",85.69) # Function Call with Possitional Args
print("*"*50)