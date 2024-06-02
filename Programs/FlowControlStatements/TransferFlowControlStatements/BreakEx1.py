#program for Demonstrating Break Statement by using for loop
#BreakEx1.py
s="PYTHON"
print("----------------------------------")
for ch in s:
    print("\t{}".format(ch))
else:
    print("----------------------------------")
#My Requirement is to Print Only PYT without using Indexing and slicing
for ch in s:
    if(ch=="H"):
        break
    print("\t{}".format(ch))
else:
    print("----------------------------------") #This line will not execute
print("----------------------------------")
print("Program execution completed")