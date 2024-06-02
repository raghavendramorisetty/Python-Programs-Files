#Program accepting a Line of Text and Generate every Char
#CharGenerateEx1.py
line=input("Enter Line of Text:")
print("="*50)
print("Given Line:{}".format(line))
print("="*50)
i=0
print("-"*40)
while(i<len(line)):
    print("Index:{} Value:{}".format(i,line[i]))
    i=i+1
else:
    print("-"*40)