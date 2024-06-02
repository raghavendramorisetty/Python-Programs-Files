# ValidteName.py<--File Name and Module Name
from NameException import InValidNameError, SpaceError
def validation(name):  # name=Mahesh Kumar
    words = name.split()  # words=[Mahesh, kumar]
    if (len(words) == 0):
        raise SpaceError
    else:
        x = "Valid"
        for word in words:
            if (not word.isalpha()):
                x = "Invalid"
                break
        if (x == "Invalid"):
            raise InValidNameError
        else:
            return ("'{}' is Valid Name".format(name))
