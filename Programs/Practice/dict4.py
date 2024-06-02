def find_max_pair_count(lst):
    from collections import defaultdict

    N = len(lst)
    sum_counts = defaultdict(int)
    pair_counts = []

    # Collect all pair sums and their counts
    for i in range(N):
        for j in range(i + 1, N):
            pair_sum = lst[i] + lst[j]
            sum_counts[pair_sum] += 1

    # Iterate over unique sums and calculate maximum pair counts
    for target_sum in sum_counts:
        count = 0
        used = [False] * N

        # Find pairs for the current target sum
        for i in range(N):
            if used[i]:
                continue
            for j in range(i + 1, N):
                if used[j]:
                    continue
                if lst[i] + lst[j] == target_sum:
                    count += 1
                    used[i] = True
                    used[j] = True
                    break

        pair_counts.append(count)

    return max(pair_counts)

# Main execution
if __name__ == "__main__":
    N = int(input())
    lst = [int(val) for val in input().split()]

    # Find and print the maximum count of pairs with unique sums
    result = find_max_pair_count(lst)
    print(result)
