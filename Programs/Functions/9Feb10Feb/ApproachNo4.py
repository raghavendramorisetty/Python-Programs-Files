#Write a Program for finding Sum of Two Numbers by using Functions
#ApproachNo4.py
def  sumop():
    # Take Input inside Function Body
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    # Do the Process in Function Body
    c = a + b
    #return the result back to Function call
    return a,b,c # here return kwd can return not only one value It can also return One or More Number of Values

#Main program
x,y,z=sumop() # Function call with Multi Line Assigment
print("Sum({},{})={}".format(x,y,z))
print("=========OR==============")
res=sumop() # Function call with single line assigment
#here res is an object of type <class, tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("-----------------OR-----------------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))