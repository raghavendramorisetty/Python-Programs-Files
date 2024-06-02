N = int(input())
weights = list(map(int, input().split()))

# Count the frequency of each weight
weight_freq = {}
for weight in weights:
    weight_freq[weight] = weight_freq.get(weight, 0) + 1

# Iterate through possible values of s
max_teams_count = 0
for s in range(2, 2 * N + 1):
    teams_count = 0
    for weight, freq in weight_freq.items():
        if s - weight in weight_freq:
            # Ensure there are enough participants of each weight to form teams
            teams_count += min(freq, weight_freq[s - weight])
    # Update the maximum number of teams
    max_teams_count = max(max_teams_count, teams_count // 2)

print(max_teams_count)
