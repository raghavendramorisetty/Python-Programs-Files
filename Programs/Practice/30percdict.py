import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

sums=[]
countlist=[]
x=0
keycopy=11111111

N=int(input())
lst=[int(val) for val in input().split()]
dictobj={}
for i in range(N):
    dictobj[i]=lst[i]
print(dictobj)
for i in range(N):
    for j in range(i+1,N):
        pairweight=lst[i]+lst[j]
        if pairweight not in sums:
            sums.append(pairweight)
sumscopy=list(sorted(sums))
for val1 in sumscopy:
    print("**************************************************************************************")
    count=0
    for i in range(N):
        dictobj[i] = lst[i]
    print(dictobj)
    #lstcopy=list(sorted(lst))
    #print("inloop1 lstcopy", lstcopy)
    #print("inloop1 val1",val1)
    #lenlstcopy=len(lstcopy)
    for key2, val2 in dictobj.copy().items():
        val2copy = val2
        print("inloop2 dictobj", dictobj)
        if (len(dictobj)==0):
            break
        if(key2!=keycopy):
            print("key2",key2)
            dictobj.pop(key2)
        #print("===========================================================================")
        #print("inloop2 val2",val2)
        #lstcopy=[val for val in lstcopy if val!=val2]
        #dictobj.pop(key2)
        #print("inloop2 lstcopy after remove", lstcopy)
        for key3, val3 in dictobj.copy().items():
            #print(val2copy, val3)
            #print("------------------------------------------------------------------")
            pairweight2 = val2copy+val3
            print("inloop3 dictobj", dictobj)
            #print("inloop3 lstcopy", lstcopy)
            #print("inloop3 val2 val3",val2,val3)
            if (pairweight2 == val1):
                #print("pairweight2",pairweight2)
                count=count+1
                #print("count",count)
                #print("inmatch val3",val3)
                #val4=val3
                #lstcopy=[val for val in lstcopy if val!=val3]
                keycopy = key3
                #dictobj.pop(key2)
                dictobj.pop(key3)
                break
                #print("inloop3 lstcopy after remove if matched", lstcopy)
        print("------------------------------------------------------------------")
    print("==================================================================================")
    countlist.append(count)
print("**************************************************************************************")
        #lstcopy.append(val4)
print(max(countlist))





