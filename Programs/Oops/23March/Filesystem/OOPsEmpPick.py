#OOPsEmpPick.py
from Employee import Employee
import pickle,sys
class EmployeePick:
    def  saveempvalues(self):
        with open("emp.data","ab") as fp:
            while(True):
                try:
                    print("------------------------------------------------------")
                    empno=int(input("Enter Employee Number:"))
                    ename=input("Enter Employee Name:")
                    sal=float(input("Enter Employee Salary::"))
                    dsg=input("Enter Employee Designation")
                    #Create an object of Employee Class
                    eo=Employee()
                    eo.getempvals(empno,ename,sal,dsg)
                    #save eo object data into the file by using dump()
                    pickle.dump(eo,fp)
                    print("Employee Data Saved in File Successfully")
                    print("------------------------------------------------------")
                    ch=input("Do u want to enter another employee record(yes/no):")
                    if(ch.lower()=="no"):
                        print("Thx for using this program")
                        sys.exit()
                except ValueError:
                    print("Don't enter alnums,strs and symbols for eno and sal-try again")

#Main program
ep=EmployeePick()
ep.saveempvalues()