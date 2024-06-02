import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here


T = int(input())
P=[]
N=[]
PTime=[]
NTime=[]

for x in range(T):
    p=[int(i) for i in input().split()]
    P.append(p)
    n=[int(j) for j in input().split()]
    N.append(n)

for y in range(T):
    PTime.append(P[y][0]/P[y][1]+P[y][2])
    NTime.append(N[y][0]/N[y][1]+N[y][2])

for z in range(T):
    if NTime[z]<PTime[z]:
        print("NINA")
        print(int(NTime[z]))
    elif NTime[z]>PTime[z]:
        print("PAUL")
        print(int(PTime[z]))
    else:
        print("BOTH")
        print(int(NTime[z]))


''' code for more efficiency
import sys
import os

def main():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        P1, P2, P3 = int(data[index]), int(data[index+1]), int(data[index+2])
        N1, N2, N3 = int(data[index+3]), int(data[index+4]), int(data[index+5])
        
        PTime = P1 / P2 + P3
        NTime = N1 / N2 + N3
        
        if NTime < PTime:
            results.append(f"NINA\n{int(NTime)}")
        elif NTime > PTime:
            results.append(f"PAUL\n{int(PTime)}")
        else:
            results.append(f"BOTH\n{int(NTime)}")
        
        index += 6
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
'''
