x=0
N=int(input())
lst=[int(val) for val in input().split()]
dictobj={}
for i in range(N):
    dictobj[i]=lst[i]
print(dictobj)
dictobj2=list(sorted(dictobj))
print(dictobj2)
for key2,val2 in dictobj.copy().items():
    val2copy=val2
    dictobj.pop(key2)
    for key3, val3 in dictobj.copy().items():
        print(val2copy,val3)
        #dictobj.pop(key3)

# N = int(input())
# weights = list(map(int, input().split()))
#
# weight_freq = {}
# for weight in weights:
#     weight_freq[weight] = weight_freq.get(weight, 0) + 1
# print(weight_freq)
