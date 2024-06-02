#Write a Program for finding Sum of Two Numbers by using Functions
#ApproachEx1.py
def  sumop(a,b): # Here 'a' and 'b' are called Formal Parameters
    c=a+b  # Here 'c' is called Local variable
    return c
#main program
print("I am from Main program")
result=sumop(10,20) # Function call
print("sum=",result)
print("-----------------------------------------------")
result=sumop(100,200) # Function call
print("sum=",result)