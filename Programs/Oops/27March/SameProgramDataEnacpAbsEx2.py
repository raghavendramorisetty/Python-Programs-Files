#SameProgramDataEnacpAbsEx2.py
class Account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=4567
        self.bname="SBI"
    def __dispaccdet(self):
        print("Account Number:{}".format(self.__acno))
        print("Account Holder Name:{}".format(self.cname))
        print("Account Balance:{}".format(self.__bal))
        print("Account PIN:{}".format(self.__pin))
        print("Account Branch Name:{}".format(self.bname))
    def  accstatus(self):
        self.__dispaccdet()

#Main program
ac=Account() # Object Creation
#ac.dispaccdet()#--Gives error bcoz dispaccdet() is encapsulated
# OR
#ac.__dispaccdet()#--Gives error bcoz dispaccdet() is encapsulated
ac.accstatus()