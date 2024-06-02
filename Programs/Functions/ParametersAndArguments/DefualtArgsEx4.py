#Program for Deomstrating Defualt Arguments
#DefualtArgsEx4.py
def  dispstudvals1(sno,sname,marks,crs="PYTHON",cnt="INDIA"): # here crs=PYTHON cnt="INDIA" are called Default Arguments
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

def  dispstudvals2(sno,sname,marks,crs="JAVA",cnt="INDIA"): # here crs=PYTHON cnt="INDIA" are called Default Arguments
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))


#Main Program
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*50)
dispstudvals1(10,"RS",45.67) # Function Call with Possitional Args
dispstudvals1(20,"TR",55.67) # Function Call with Possitional Args
dispstudvals1(30,"JH",57.68) # Function Call with Possitional Args
dispstudvals1(40,"MC",85.69) # Function Call with Possitional Args
dispstudvals1(25,"RT",15.69,cnt="USA") # Function Call with Possitional Args and Default Arguments
dispstudvals1(15,"SP",35.69,cnt="GER") 
print("*"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("*"*50)
dispstudvals2(50,"DT",85.69) # Function Call with Possitional Args
dispstudvals2(60,"PT",25.69) # Function Call with Possitional Args
dispstudvals2(70,"JB",65.69) # Function Call with Possitional Args
dispstudvals2(80,"MD",95.69) # Function Call with Possitional Args
dispstudvals2(90,"CV",45.69) # Function Call with Possitional Args
dispstudvals2(75,"DR",35.69,cnt="AUS") # Function Call with Possitional Args and Default Arguments
print("*"*50)