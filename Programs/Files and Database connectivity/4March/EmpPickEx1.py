# program for Reading emp details and save them as a Record in a File
# EmpPickEx1.py
import pickle

with open("emp.data", "ab") as fp:
    print("------------------------------------------------")
    eno = int(input("Enter Employee Number:"))
    ename = input("Enter Employee Name:")
    sal = float(input("Enter Employee salary:"))
    dsg = input("enter employee designation:")
    print("------------------------------------------------")
    # add emp values to list object
    emplist = list()
    emplist.append(eno)
    emplist.append(ename)
    emplist.append(sal)
    emplist.append(dsg)
    # save emp list object to the file
    pickle.dump(emplist,fp)
    print("Employee data saved in file")
    print("------------------------------------------------")
