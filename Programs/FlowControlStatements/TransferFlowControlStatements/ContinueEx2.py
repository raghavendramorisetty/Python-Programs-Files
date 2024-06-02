#program for Demonstrating Continue Statement  by using while loop
#ContinueEx2.py
s="PYTHON"
print("-"*50)
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-"*50)
#My requirment is to Print PYHN
i=0
while(i<len(s)):
    if(s[i]=="T") or (s[i]=="O") :
        i=i+1
        continue
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-" * 50)