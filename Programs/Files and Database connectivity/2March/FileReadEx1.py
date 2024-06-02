#Program for Demonstrating How to read the data from files
#Choose the file name and open it into read mode
#FileReadEx1.py
try:
    with open("sci.data","r") as fp:
        filedata=fp.read()
        print("----------------------------")
        print(filedata)
        print("----------------------------")
except FileNotFoundError:
    print("File does not exist")

