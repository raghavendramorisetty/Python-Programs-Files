import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here


maxteams = 0
N = int(input())
lst = [int(val) for val in input().split()]
for i in range(N):
    for j in range(i + 1, N):
        teamweight = lst[i] + lst[j]
        count = 0
        for p in range(N):
            for q in range(p + 1, N):
                if p != i and p != j and q != i and q != j and lst[p] + lst[q] == teamweight:
                    count = count + 1
        maxteams = max(maxteams, count)
print(maxteams)
