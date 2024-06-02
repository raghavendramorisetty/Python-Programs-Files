#Program for Demonstrating how to open the file in write mode
#FileOpenEx6.py
try:
    with open("Ragh2.data","x+") as fp:
        print("-------------------------------------------")
        print("File Created in x+ mode ")
        print("Type of fp=",type(fp))
        print("-------------------------------------------")
        print("File Name=",fp.name)
        print("File Mode=",fp.mode)
        print("Is File Readable?=",fp.readable())
        print("Is File Writeable?=", fp.writable())
        print("Is File Closed?=", fp.closed)
        print("-------------------------------------------")
    print("\nIs File Closed?=", fp.closed)
except FileExistsError:
    print("File already exist")