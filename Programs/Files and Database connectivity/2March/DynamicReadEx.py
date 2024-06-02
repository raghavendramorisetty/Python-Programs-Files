#program for accepting the File Name from KBD and display its content
#DynamicReadEx.py
try:
    filename=input("Enter Any File Name:")
    with open(filename) as fp:
        filedata=fp.read()
        print("-----------------------------------")
        print(filedata)
        print("-----------------------------------")
except FileNotFoundError:
    print("File Does Not Exist")

