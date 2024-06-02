#Program accepting a Line of Text and Generate length of each Word
#WordLengthGenerateEx1.py
#Program accepting a Line of Text and Generate Word by word
#WordLengthGenerateEx1.py
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
        print("\t\t{}\t\t{}".format(len(words[i]),words[i]))
        i=i+1
    print("="*50)
    print("Number of Words={}".format(len(words)))
    print("="*50)

                                      # OR below program

#Below is code done by me

# line=input("Enter Line of Text:")
# if(len(line)==0):
#     print("U must enter a line of Text ")
# else:
#     words=line.split()
#     lenarr=[]
#     for i in range(len(words)):
#         lenarr.append(len(words[i]))
#         #Note:If lenarr[i]=len(words[i]) is used instead above statement then we will get error
#               becoz lenarr is empty list, we get index error.
#     for i in range(len(words)):
#         print("{} is length of word {}".format(lenarr[i],words[i]))
