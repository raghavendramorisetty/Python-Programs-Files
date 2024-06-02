#Program for Demonstrating how to open the file in write mode
#FileOpenEx4.py

# with open("C:\\Users\\ragha\\My Drive (raghavendramorisetty@gmail.com)\\Sem3 mtech\\NARESHIT\\Python_kvrsir\\python program files\\Programs\\Files and Database connectivity\\Ragh.data","w") as fp:
# OR we can do as below for creating file in CURRENT FOLDER

with open("Ragh.data","w") as fp:
    print("------------------------------------------")
    print("File created in write mode ")
    print("Type of fp=",type(fp))
    print("------------------------------------------")
    print("File Name=",fp.name)
    print("File Mode=",fp.mode)
    print("Is File Readable?=",fp.readable())
    print("Is File Writable?=",fp.writable())
    print("I am in 'with open() as' indentation block--Is File Closed?=",fp.closed)
    print("------------------------------------------")
print("\nI am Out-off 'with open() as' indentation block--Is File Closed?=",fp.closed)

