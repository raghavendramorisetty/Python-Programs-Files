#AnonymousFunEx7.py

decide=lambda val:"'{}' is Alphabetical Word".format(val) if(val.isalpha()) else "'{}' is Numrical Value".format(val) if(val.isdigit()) \
    else "'{}' is Alpha-numerical Number".format(val) if(val.isalnum() and not val.isalpha() and not val.isdigit()) \
    else "{}' is Special Symbols".format(val) if(not val.isalnum() and not val.isalpha() and not val.isdigit() and not val.isspace() ) \
    else " '{}' is Space Char".format(val)
val=input("Enter Any Value:")
res=decide(val)
print(res)


# For Above Reference of the Code --Use following HINT
"""val=input("Enter Any Value:")
if(val.isalpha()):
    print("'{}' is Alphabetical Word".format(val))
if(val.isdigit()):
    print("'{}' is Numrical Value".format(val))
if(val.isspace()):
    print("'{}' is Space Char".format(val))
if(val.isalnum() and not val.isalpha() and not val.isdigit()):
    print("'{}' is Alpha-numerical Number".format(val))
if(not val.isalnum() and not val.isalpha() and not val.isdigit() and not val.isspace() ):
    print("{}' is Special Symbols".format(val)) """
