#AnonymousFunEx3.py
converter=lambda line:line.upper()
#Main Program
line=input("Enter a Line of Text:")
res=converter(line) # Function Call
print("Given Line:{}".format(line))
print("Converted Line:{}".format(res))