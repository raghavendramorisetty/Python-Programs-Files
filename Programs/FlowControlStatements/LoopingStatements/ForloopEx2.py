#ForLoopEx2.py
s="PYTHON"
print("By using While Loop--backward direction")
i=len(s)-1
while(i>=0):
    print(s[i])
    i=i-1
else:
    print("*****************************")
print("By using for Loop--backward direction--logic-1")
for ch in s[::-1]:
    print(ch)
else:
    print("-"*50)
print("By using for Loop--backward direction--logic-2")
for i in range(5,-1,-1):
    print(s[i])
else:
    print("#"*50)
print("By using for Loop--backward direction--logic-3")
for i in range(-1,-7,-1):
    print(s[i])
else:
    print("#" * 50)
print("By using for Loop--backward direction--logic-4")
for i in range(0,len(s))[::-1]:
    print(s[i])
else:
    print("#" * 50)
print("By using for Loop--backward direction--logic-5")
for i in range(len(s)-1,-1,-1):
    print(s[i])