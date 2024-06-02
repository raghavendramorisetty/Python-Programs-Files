#Program for Demonstrating How to read the data from files
#Choose the file name and open it into read mode
#FileReadEx2.py
try:
    with open("students.data","rt") as fp:
        lines=fp.readlines()
        print("-------------------------------------")
        print(lines)
        for line in lines:
            print(line,end="")
        print()
        print("-------------------------------------")

except FileNotFoundError:
    print("File does not exist")