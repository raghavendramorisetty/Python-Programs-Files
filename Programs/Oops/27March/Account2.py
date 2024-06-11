#Program for Demonstrating Data Encapsulation
#Account2.py<----File Name and Module Name
class Account:
    def getAcDetails(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=4567
        self.bname="SBI"