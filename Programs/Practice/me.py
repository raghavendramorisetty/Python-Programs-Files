sum=[]
countlist=[]
count=1
q=0
N=int(input())
lst=[int(val) for val in input().split()]
for i in range(N):
    for j in range(i+1,N):
            sum.append(lst[i]+lst[j])
for i in range(len(sum)):
    for j in range(i+1,len(sum)):
        if(sum[i]==sum[j]):
            count=count+1
    countlist.append(count)
    count=1
print(max(countlist))

