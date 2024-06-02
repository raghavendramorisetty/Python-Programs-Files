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
#print(sumscopy)
for val1 in sumscopy:
    count=0
    lstcopy=list(sorted(lst))
    #print(lstcopy)
    #print("oouuuttt",val1)
    lenlstcopy=len(lstcopy)
    for x in range(N):
        for y in range(x+1,N):
           # for val2 in lstcopy[x:]:
                #print("outside",val2)
                #lstcopy.remove(val2)
                #print("inval2loop",lstcopy)
              #  for val3 in lstcopy[y:]:
                    #print("inval3loop",lstcopy)
                #    pairweight2 = val2+val3
                    pairweight2=lstcopy[x]+lstcopy[y]
                    #print("innninside", val3)
                    if (pairweight2 == val1):
                        count=count+1
                        break
                        #print("count",count)
                        #print("innninside",val3)
                        #lstcopy.remove(val3)
    countlist.append(count)
print(max(countlist))










#    j=0
#   k=1
#     while j<(lenlstcopy):
#         while k<(lenlstcopy):
#             pairweight2 = lstcopy[j] + lstcopy[k]
#             # print("beformatch",pairweight2)
#             # print(i, j, k)
#             if(pairweight2==i):
#                 # print("aftermatch",pairweight2)
#                 count=count+1
#                 # print(count)
#                # print(count)
#                 print(lstcopy)
#                 print(j,k)
#                 print(lstcopy[j],lstcopy[k])
#                 lstcopy.pop(j)
#                 #print(i)
#                 #print(j)
#                 lstcopy.pop(k-1)
#                 # print("after pop",lstcopy)
#                 lenlstcopy=lenlstcopy-2
#                 j=0
#                 k=1
#                 continue
#             k=k+1
#         j=j+1
#         # if(len(lstcopy)==0):
#         #     break
#     countlist.append(count)
# print(max(countlist))

