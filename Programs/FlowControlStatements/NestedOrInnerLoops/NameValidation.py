#NameValidation.py
while(True):
    name=input("Enter Ur Name:")
    if(len(name)==0):
        print("U Must Enter Ur Name:")
    else:
        res=True
        words=name.split()
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            print("'{}' is Valid Name".format(name))
            break
        else:
            print("'\t{}' is Invalid Valid Name--try again".format(name))