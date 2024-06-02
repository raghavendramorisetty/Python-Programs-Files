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
    count=0
    lstcopy=list(sorted(lst))
    lenlstcopy=len(lstcopy)
    for val2 in lstcopy:
        lstcopy.remove(val2)
        for val3 in lstcopy:
            pairweight2 = val2+val3
            if (pairweight2 == val1):
                count=count+1
                lstcopy.remove(val3)
    countlist.append(count)
print(max(countlist))





