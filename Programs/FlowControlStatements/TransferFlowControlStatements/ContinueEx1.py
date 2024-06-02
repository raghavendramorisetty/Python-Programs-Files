#program for Demonstrating Continue Statement  by using for loop
#ContinueEx1.py
s="PYTHON"
print("-"*50)
for ch in s:
    print("\t{}".format(ch))
else:
    print("-"*50)
#My requirment is to Print PYHN
for ch in s:
    if ch in ["T","O"]:
        continue
    print("\t{}".format(ch))
else:
    print("-" * 50)
