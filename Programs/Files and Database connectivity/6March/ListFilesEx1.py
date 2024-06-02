#Program for Listing the Files and Database connectivity in a Folder
#ListFilesEx1.py
import os
try:
    FileNames=os.listdir(".") # here dot (.) refers current working Folder
    print("-----------------------------------------------------")
    for filename in FileNames:
        print(filename)
    print("------------------------------------------------------")
except FileNotFoundError:
    print("Folder does not exist")

