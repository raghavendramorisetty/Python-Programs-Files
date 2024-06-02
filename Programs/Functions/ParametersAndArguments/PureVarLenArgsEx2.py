# Program for demonstrating  Variable Length Arguments OR Parameters
# This Program will execute bcoz we are using Variable Length Arguments OR Parameters
# PureVarLenArgsEx2.py
def disp(*a):  # Here *a  is called Variable Length Parameter whose type is <class,tuple>
    for val in a:
        print("\t{}".format(val))
    print("Number of Values=", len(a))
    print("----------------------------------")


# Main Program
disp(10, 20, 30, 40, 50)  # Function call-1 with 5 Possitional Args
disp(10, 20, 30, 40)  # Function call-2 with 4 Possitional Args
disp(10, 20, 30)  # Function call-3 with 3 Possitional Args
disp(10, 20)  # Function call-4 with 2 Possitional Args
disp(10)  # Function call-5 with 1 Possitional Args
disp()  # #  Function call-6 with 0 Possitional Args