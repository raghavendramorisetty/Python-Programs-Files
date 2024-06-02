# Program for Demonstrating How the open the file in read mode
# FileReadEx3.py
try:
    with open("stud1.data") as fp:  # default read mode is taken
        print("----------------------------------")
        print("File Opened in read mode successfully")
        print("Type of fp=", type(fp))
        print("I am in 'with open() as' indentation block--Is File Closed?=", fp.closed)
        print("----------------------------------")
    print("\\nI am Out-off 'with open() as' indentation block--Is File Closed?=", fp.closed)
except FileNotFoundError:
    print("File does not exist")
