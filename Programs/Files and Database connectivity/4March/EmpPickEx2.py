# programfor Reading emp details and save them as a Record in a File
# EmpPickEx2.py
import pickle

def savempdata():
    with open("emp.data", "ab") as fp:
        while (True):
            print("------------------------------------------")
            eno = int(input("Enter Employee Number: "))
            ename = input("enter employee name: ")
            sal = float(input("Enter Employee Salary:"))
            dsg = input("Enter Employee Designation:")
            print("----------------------------------------------")
            # add emp values to list object
            emplist = list()
            emplist.append(eno)
            emplist.append(ename)
            emplist.append(sal)
            emplist.append(dsg)
            # Save emplist object to the file
            pickle.dump(emplist, fp)
            print("Employee Data Saved in File")
            print("----------------------------------------------")
            ch = input("Do u want to enter another employee record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for using this program")
                break


# Main program
savempdata()  # Function call
