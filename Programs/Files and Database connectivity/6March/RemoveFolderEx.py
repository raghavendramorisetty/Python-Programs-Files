#Program for Removing a Folder by using a function "rmdir()" present in os module
#RemoveFolderEx.py
import os
try:
    os.rmdir("C:\\sampleFolder")
    print("Folder removed--verify")
except FileNotFoundError:
    print("Folder does not Exist")
except OSError:
    print("Specified Folder is not empty--make sure that It must be empty")
