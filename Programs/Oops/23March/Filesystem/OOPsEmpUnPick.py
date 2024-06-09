# OOPsEmpUnPick.py
import pickle


class EmployeeUnPick:
    def readrecords(self):
        try:
            with open("emp.data", "rb") as fp:
                print("*" * 50)
                while (True):
                    try:
                        record = pickle.load(fp)
                        record.dispempvals()
                    except EOFError:
                        print("*" * 50)
                        break

        except FileNotFoundError:
            print("File does not Exist")


# Main program
epu = EmployeeUnPick()
epu.readrecords()
