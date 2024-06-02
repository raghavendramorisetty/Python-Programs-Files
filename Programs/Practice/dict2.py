import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

sums = []
countlist = []

N = int(input())
lst = [int(val) for val in input().split()]
dictobj = {i: lst[i] for i in range(N)}
print(dictobj)

# Collect unique pair sums
for i in range(N):
    for j in range(i + 1, N):
        pairweight = lst[i] + lst[j]
        if pairweight not in sums:
            sums.append(pairweight)

sumscopy = sorted(sums)
for val1 in sumscopy:
    print("**************************************************************************************")
    count = 0
    dictobj = {i: lst[i] for i in range(N)}  # Reset dictobj for each sum
    print(dictobj)

    keys_to_remove = set()  # To keep track of keys to remove after iteration
    for key2 in list(dictobj.keys()):
        if key2 in keys_to_remove:
            continue
        val2 = dictobj[key2]

        for key3 in list(dictobj.keys()):
            if key3 in keys_to_remove or key3 == key2:
                continue
            val3 = dictobj[key3]

            pairweight2 = val2 + val3
            if pairweight2 == val1:
                count += 1
                print(dictobj[key2],dictobj[key3])
                print("count",count)
                keys_to_remove.add(key2)
                keys_to_remove.add(key3)
                break

    countlist.append(count)
    print(f"Count for sum {val1}: {count}")
    print("==================================================================================")

print("**************************************************************************************")
print(max(countlist))
