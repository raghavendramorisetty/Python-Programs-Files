#Program for Demonstrating Instance Methods
#InstanceMethodEx2.py
class Student:
    def readstuddata(self,objinfo):  # Instance Method
        self.sno=int(input("Enter {} Student Number:".format(objinfo)))
        self.name=input("Enter {} Student Name:".format(objinfo))
        self.marks=float(input("Enter {} Student Marks:".format(objinfo)))
        print("---------------------------------------")
        self.dispstuddata(objinfo) # Calling instance Method from another instance Method of same class

    def dispstuddata(self,objinfo): # Instance Method
        print("{} Student Number:{}".format(objinfo,self.sno))
        print("{} Student Name:{}".format(objinfo, self.name))
        print("{} Student Marks:{}".format(objinfo, self.marks))

#Main program
s1=Student()
s2=Student()
#read the Data for s1 Object
s1.readstuddata("First")
print("-----------------------------------")
s2.readstuddata("Second")