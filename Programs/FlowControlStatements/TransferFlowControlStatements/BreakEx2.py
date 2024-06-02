#program for Demonstrating Break Statement by using while loop
#BreakEx2.py
s="PYTHON"
print("----------------------------------")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("----------------------------------")
#My Requirement is to Print Only PYT without using Indexing and slicing
i=0
while(i<len(s)):
    if(s[i]=="H"):
        break
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("*"*50) #This line will not execute
print("----------------------------------")
print("Program execution completed")