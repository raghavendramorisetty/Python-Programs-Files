# program for Demonstrating Class Level method
# ClassLevelMethodEx3.py
class Student:
    @classmethod
    def getcrs(cls):  # Class Level Method
        cls.crs = "PYTHON"
        # cls.getcity() # Calling Class Level Method w.r.t cls

    @classmethod
    def getcity(cls):
        Student.city = "HYD"

    def readstuddata(self, objinfo):  # Instance Method
        self.sno = int(input("Enter {} Student Number:".format(objinfo)))
        self.name = input("Enter {} Student Name:".format(objinfo))
        self.marks = float(input("Enter {} Student Marks:".format(objinfo)))

    def dispstuddata(self, objinfo):  # Instance Method
        print("{} Student Number:{}".format(objinfo, self.sno))
        print("{} Student Name:{}".format(objinfo, self.name))
        print("{} Student Marks:{}".format(objinfo, self.marks))
        self.getcrs()  # Calling Class Level Method w.r.t self
        self.getcity()  # Calling Class Level Method w.r.t self
        print("{} STUDENT COURSE:{}".format(objinfo, self.crs))
        print("{} STUDENT CITY:{}".format(objinfo, self.city))


# Main Program
s1 = Student()
s2 = Student()
s1.readstuddata("First")
print("-------------------------------")
s2.readstuddata("second")
print("-------------------------------")
s1.dispstuddata("First")
print("-------------------------------")
s2.dispstuddata("Second")
