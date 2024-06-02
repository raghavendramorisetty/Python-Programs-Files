# Program for Removing a File by using "remove()" present in os module
# RemoveFileEx.py
import os
try:
    os.remove("C:\\sample2\\CHECKING22.txt")
    print("File Removed--verify")
except FileNotFoundError:
    print("File name does not exist")
