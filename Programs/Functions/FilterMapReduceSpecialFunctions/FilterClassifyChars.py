# FilterClassifyChars.py
"""
vowel=[]
consonant=[]
digits=[]
specialsymb=[]
spaces=[]

decide = lambda val:vowel.append(val) if (val in ['a', 'e', 'i', 'o', 'u']) else \
         consonant.append(val) if (val.isalpha() and val not in ['a', 'e', 'i', 'o', 'u']) else \
         digits.append(val) if (val.isdigit()) else \
         specialsymb.append(val) if (not val.isalnum() and not val.isalpha() and not val.isdigit() and not val.isspace()) else \
         spaces.append(val)

LOT=input("Enter line of text Separated by spaces:")
chars=list(LOT)
for val in chars:
    decide(val)
print(vowel, consonant, digits, specialsymb, spaces) """

# OR

LOT=input("Enter line of text:")
charlist=list(LOT)
vowels=list(filter(lambda val:val in ['a', 'e', 'i', 'o', 'u'],charlist))
consonants=list(filter(lambda val:val.isalpha() and val not in ['a', 'e', 'i', 'o', 'u'],charlist))
digits=list(filter(lambda val:val.isdigit(),charlist))
specialsymb=list(filter(lambda val:not val.isalnum() and not val.isalpha() and not val.isdigit() and not val.isspace(),charlist))
spaces=list(filter(lambda val:val.isspace(),charlist))
print(vowels, consonants, digits, specialsymb, spaces)