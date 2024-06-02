#Program for Demonstrating how to open the file in write mode
#FileOpenEx5.py
with open("Ragh1.data","a+") as fp:
    print("-------------------------------------------")
    print("File Created in a+ mode ")
    print("Type of fp=",type(fp))
    print("-------------------------------------------")
    print("File Name=",fp.name)
    print("File Mode=",fp.mode)
    print("Is File Readable?=",fp.readable())
    print("Is File Writeable?=", fp.writable())
    print("Is File Closed?=", fp.closed)
    print("-------------------------------------------")
print("\nIs File Closed?=", fp.closed)