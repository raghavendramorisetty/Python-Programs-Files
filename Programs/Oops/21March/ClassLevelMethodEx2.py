# program for Demonstrating Class Level method
# ClassLevelMethodEx2.py
class Student:
    @classmethod
    def getcrs(cls):  # Class Level Method
        cls.crs = "PYTHON"
        cls.getcity()  # Calling Class Level Method w.r.t cls

    @classmethod
    def getcity(cls):
        Student.city = "HYD"


# Main Program
Student.getcrs()  # calling Class Level Method w.r.t Class Name
print(Student.crs)
print(Student.city)
