# FilterFunEx5.py
word = input("Enter any word:")  # Apple
vlist = list(filter(lambda ch: ch.lower() in ['a', 'e', 'i', 'o', 'u'], word))
res = "Vowel Word" if len(vlist) != 0 else "Not Vowel Word"
print("{} is {}".format(word, res))
