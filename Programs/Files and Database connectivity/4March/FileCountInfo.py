# program for Counting Number of Lines, words and Chars from any file
# FileCountInfo.py
try:
    filename = input("Enter any Text file name for counting number of lines, words and letters:")
    with open(filename, "r") as fp:
        lines = fp.readlines()  # here lines is an object of list type
        nl = 0
        nw = 0
        nc = 0
        for line in lines:
            nl = nl + 1
            nw = nw + len(line.split())
            nc = nc + len(line)
except FileNotFoundError:
    print("File does not exist")
else:
    print("-------------------------------------------")
    print("Number of lines=",nl)
    print("Number of words=",nw)
    print("Number of chars=",nc)
    print("-------------------------------------------")

