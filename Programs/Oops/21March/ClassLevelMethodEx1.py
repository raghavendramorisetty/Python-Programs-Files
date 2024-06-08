# program for Demonstrating Class Level method
# ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrs(cls):  # Class Level Method
        cls.crs = "PYTHON"


# Main Program
Student.getcrs()  # calling Class Level Method w.r.t Class Name
print(Student.crs)
