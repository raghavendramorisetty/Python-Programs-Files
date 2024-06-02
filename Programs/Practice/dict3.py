import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

sums = []
countlist = []

N = int(input())
lst = [int(val) for val in input().split()]
dictobj = {i:lst[i] for i in range(N)}

for i in range(N):
    for j in range(i+1,N):
        pairweight=lst[i]+lst[j]
        if pairweight not in sums:
            sums.append(pairweight)

sumscopy=sorted(sums)
for val1 in sumscopy:
    count=0
    dictobj={i:lst[i] for i in range(N)}

    KeysToBeRemoved = set()
    for key2 in list(dictobj.keys()):
        if key2 in KeysToBeRemoved:
            continue
        val2=dictobj[key2]

        for key3 in list(dictobj.keys()):
            if key3 in KeysToBeRemoved or key3==key2:
                continue
            val3=dictobj[key3]

            pairweight2=val2+val3
            if pairweight2==val1:
                count=count+1
                KeysToBeRemoved.add(key2)
                KeysToBeRemoved.add(key3)
                break
    countlist.append(count)
print(max(countlist))