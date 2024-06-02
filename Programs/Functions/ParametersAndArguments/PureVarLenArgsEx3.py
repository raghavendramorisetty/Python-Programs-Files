# Program for demonstrating Variable Length Arguments OR Parameters
# This Program will execute bcoz we are using Variable Length Arguments OR Parameters
# PureVarLenArgsEx3.py
def disp(sno, sname, *a):  # Here *a  is called Variable Length Parameter whose type is <class,tuple>
    print("----------------------------------")
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    s = 0
    for val in a:
        print("\t{}".format(val))
        s = s + val
    print("----------------------------------")
    print("sum({})={}".format(a, s))
    print("----------------------------------")


# Main Program
disp(100, "Rossum", 10, 20, 30, 40, 50)  # Function call-1 with 7 Possitional Args
disp(200, "Travis", 10, 20, 30, 40)  # Function call-2 with 6 Possitional Args
disp(300, "JHunter",10, 20, 30)  # Function call-3 with 5 Possitional Args
disp(400, "Ritche", 10, 20)  # Function call-4 with 4 Possitional Args
disp(500, "Dennis", 10)  # Function call-5 with 3 Possitional Args
disp(600, "Strup")  # Function call-6 with 2 Possitional Args