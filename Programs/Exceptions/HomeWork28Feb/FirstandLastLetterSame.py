print("Enter the list of words separated by space: ")
lst = [word for word in input().split()]
output = []
for word in lst:
    if (word[0] == word[::-1][0]):
        output.append(word)
print("list of words having 1st and last letters same are: ")
print(output)
