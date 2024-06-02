def find_max_pairs(arr):
    # Create a dictionary to store the count of each element
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    max_pairs = 0
    pairs = []

    # Iterate through the dictionary to find pairs
    for num in count_dict:
        # Check if the complement of num exists in the dictionary
        complement = -num
        if complement in count_dict:
            # Calculate the number of pairs possible with num and complement
            num_pairs = min(count_dict[num], count_dict[complement])
            # Add these pairs to the result
            for _ in range(num_pairs):
                pairs.append((num, complement))
            # Update the maximum pairs
            max_pairs += num_pairs
            # Remove num and complement from the dictionary to avoid using them again
            del count_dict[num]
            del count_dict[complement]

    return max_pairs, pairs

# Test the function
arr = [1,1,2,2,3,4]
max_pairs, pairs = find_max_pairs(arr)
print("Maximum number of pairs:", max_pairs)
print("Pairs formed:", pairs)
