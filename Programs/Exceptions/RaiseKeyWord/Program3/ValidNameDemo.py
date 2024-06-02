#ValidNameDemo.py
from ValidteName import validation
from NameException import InValidNameError,SpaceError
try:
    name=input("Enter Ur Name:")
    res=validation(name)
except InValidNameError:
    print("'{}' is Invalid Name".format(name))
except SpaceError:
    print("Don't enter Space for Name")
else:
    print(res)