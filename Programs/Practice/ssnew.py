sums=[]
countlist=[]
q=0
dictobj={}

N=int(input())
lst=[int(val) for val in input().split()]
lstsort=list(sorted(lst))
for i in range(N):
    for j in range(i+1,N):
        dictobj[[i,j]]=lstsort[i]+lstsort[j]
# for key1, value1 in dictobj.items():
#         for key2, value2 in dictobj.items():
#             if(value1==value2 and key1)





