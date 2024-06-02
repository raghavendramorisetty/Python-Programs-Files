# Program for Demonstrating global Keyword
# GlobalKwdEx1.py
a = 10  # Here 'a' is called Global variable
def incr1():
    global a  # Mandatory to write global Kwd bcoz we are modifying the global var value a
    a = a + 1
def incr2():
    global a  # Mandatory to write global Kwd bcoz we are modifying the global var value a
    a = a * 2
def incr3():
    c = a * 3  # Here we need not to use global keyword bcoz we are not modifying global var value 'a', We are just accessing the global variable(a)
    print("Local c=", c)

# Main program
print("Val of a in Main Program before incr1()=", a)  # 10
incr1()
print("Val of a in Main Program after incr1()=", a)  # 11
incr2()
print("Val of a in Main Program after incr2()=", a)  # 22
incr3()
print("Val of a in Main Program after incr3()=", a)  # 22