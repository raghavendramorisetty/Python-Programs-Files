#To print positive number elements and negative elements seperately
#ContinueExMe.py
lst = [10, -20, -30, 40, 50, -67, 89, 0, -10, -23, 0]
poslist=[]
neglist=list()
for val in lst:
   if(val<0):
       neglist.append(val)
   if(val>0):
       poslist.append(val)
else:
    print("Given List ={}".format(lst))
    print("Positive Elements={}".format(poslist))
    print("Negative Elements={}".format(neglist))