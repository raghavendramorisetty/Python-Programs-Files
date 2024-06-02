# program for Demonstrating Access the Data of the File Randomly
# tell()--->Gives Current Index of File Pointer
# seek()--->Will Reset(0 index)/sets(other index) the Index of File Pointer to Given value.
# RandomAccessFiles.py
try:
    with open("hyd.info", "r") as fp:
        print("----------------------------------------------")
        print("Initial Index of fp=", fp.tell())  # 0
        print("-----------------------------------------------")
        fdata = fp.read(6)
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 6
        print("-----------------------------------------------")
        fdata = fp.read(8)
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 15
        print("-----------------------------------------------")
        fdata = fp.read(10)
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 26
        print("-----------------------------------------------")
        fdata = fp.read(6)
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 32
        print("-----------------------------------------------")
        fdata = fp.read()
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 90
        print("-----------------------------------------------")
        fdata = fp.read()
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 90
        print("-----------------------------------------------")
        # Resetting the fp to 0 Index
        fp.seek(0)
        fdata = fp.read()
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())
        print("-----------------------------------------------")
        # Resetting the fp to 32 Index
        fp.seek(32)
        fdata = fp.read()
        print("Random File Data=", fdata)
        print("Now Index of fp=", fp.tell())  # 90
        print("-----------------------------------------------")

except FileNotFoundError:
    print("File Does not Exist")
