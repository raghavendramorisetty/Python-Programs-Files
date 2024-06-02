

x=1
N=int(input())
lst=[int(val) for val in input().split()]
for i in range(N):
    if lst[x] != lst[i]:
        for j in range(i+1,N):
            sum.append(lst[i]+lst[j])
        x = i
print(sum)
for i in range(len(sum)):
    for j in range(i+1,len(sum)):
        if(sum[i]==sum[j]):
            count=count+1
    countlist.append(count)
    count=1
print(max(countlist))