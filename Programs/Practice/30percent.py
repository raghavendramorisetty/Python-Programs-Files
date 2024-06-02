import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

sums=[]
countlist=[]
q=0

N=int(input())
lst=[int(val) for val in input().split()]
for i in range(N):
    for j in range(i+1,N):
        pairweight=lst[i]+lst[j]
        if pairweight not in sums:
            sums.append(pairweight)
sumscopy=list(sorted(sums))
for val1 in sumscopy:
    print("**************************************************************************************")
    count=0
    lstcopy=list(sorted(lst))
    print("inloop1 lstcopy", lstcopy)
    print("inloop1 val1",val1)
    lenlstcopy=len(lstcopy)
    for val2 in lstcopy:
        print("===========================================================================")
        print("inloop2 lstcopy", lstcopy)
        print("inloop2 val2",val2)
        #lstcopy=[val for val in lstcopy if val!=val2]
        lstcopy.remove(val2)
        print("inloop2 lstcopy after remove", lstcopy)
        for val3 in lstcopy:
            print("------------------------------------------------------------------")
            pairweight2 = val2+val3
            print("inloop3 lstcopy", lstcopy)
            print("inloop3 val2 val3",val2,val3)
            if (pairweight2 == val1):
                print("pairweight2",pairweight2)
                count=count+1
                print("count",count)
                print("inmatch val3",val3)
                #val4=val3
                #lstcopy=[val for val in lstcopy if val!=val3]
                lstcopy.remove(val3)
                break
                print("inloop3 lstcopy after remove if matched", lstcopy)
        print("------------------------------------------------------------------")
    print("==================================================================================")
    countlist.append(count)
print("**************************************************************************************")
        #lstcopy.append(val4)
print(max(countlist))





