# Read input
N = int(input())
weights = list(map(int, input().split()))

max_teams = 0
x=[]

for i in range(N):
    for j in range(i + 1, N):
        team_weight = weights[i] + weights[j]
        count = 0
        for k in range(N):
            for l in range(k + 1, N):
                if k != i and l != j and weights[k] + weights[l] == team_weight:
                    x.append(team_weight)
                    count += 1
        max_teams = max(max_teams, count)
print(x)

print(max_teams)
