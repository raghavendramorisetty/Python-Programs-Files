#FindMaxLengthWord.py
line=input("Enter a Line of Text:") # Line=Python is an Object Oriented Programming Lang
if(len(line)==0):
    print("U must Enter a Line of Text:")
else:
    words=line.split()
    dobj=dict() # Create an Empty Dict for Storing word and Its Length
    for word in words:
        dobj[word]=len(word)
    else:
        maxlenwords=[]
        print(dobj) # {'Python': 6, 'is': 2, 'an': 2, 'Object': 6, 'Oriented': 8, 'Programming': 11, 'Lang': 4}
        maxlen=max(dobj.values()) # Maxlen=11
        print(type(dobj.values())) # <class 'dict_values'>
        print(dobj.values()) # dict_values([values of lengths of words in dict])
        for key,value in dobj.items():
            if(value==maxlen):
                maxlenwords.append(key)
        else:
            print("------------------------------")
            print("Max Length Words")
            print("------------------------------")
            for word in maxlenwords:
                print("\t{}".format(word))
            else:
                print("------------------------------")