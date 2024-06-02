#Program accepting a Line of Text and Generate Word by word
#WordGenerateEx1.py
line=input("Enter Line of Text:")
if(len(line)==0):
    print("U must enter a line of Text ")
else:
    print("="*50)
    print("Given Line:{}".format(line))
    print("="*50)
    #get the words--use split()
    words=line.split()  # words= ['Python', 'is', 'an', 'oop', 'lang']
    i=0
    while(i<len(words)):
        print("\t\t{}".format(words[i]))
        i=i+1
    print("="*50)
    print("Number of Words={}".format(len(words)))
    print("="*50)