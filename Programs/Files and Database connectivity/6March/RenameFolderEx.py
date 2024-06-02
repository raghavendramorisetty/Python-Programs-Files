#Program for Renaming a Folder by using "rename()" present in os module
#RenameFolderEx.py
import os
try:
    os.rename("C:\\sample","C:\\sample2")
    print("Folder Renamed--verify")
except FileNotFoundError:
    print("Folder Does Not Exist")