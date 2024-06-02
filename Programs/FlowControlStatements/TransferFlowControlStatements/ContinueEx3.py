#To print positive number elements and negative elements seperately
#ContinueEx3.py
lst = [10, -20, -30, 40, 50, -67, 89, 0, -10, -23, 0]
poslist=[]
for val in lst:
   if(val<=0):
       continue
   poslist.append(val)
else:
    print("Given List ={}".format(lst))
    print("Positive Elements={}".format(poslist))
    neglist=list()
    for val in lst:
        if(val>=0):
            continue
        neglist.append(val)
    else:
        print("Negative Elements={}".format(neglist))