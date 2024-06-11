#SameProgramDataEnacpAbsEx1.py
class Account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=4567
        self.bname="SBI"
    def  showdetails(self):
        print("Account Number:{}".format(self.__acno))
        print("Account Holder Name:{}".format(self.cname))
        print("Account Balance:{}".format(self.__bal))
        print("Account PIN:{}".format(self.__pin))
        print("Account Branch Name:{}".format(self.bname))

#Main program
ac=Account() # Object Creation
ac.showdetails()