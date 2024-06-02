#Program for Renaming a File by using "rename()" present in os module
#RenameFileEx.py
import os
try:
    os.rename("C:\\sample2\\CHECKING.txt","C:\\sample2\\CHECKING22.txt")
    print("File Renamed--verify")
except FileNotFoundError:
    print("File name Does Not Exist")

