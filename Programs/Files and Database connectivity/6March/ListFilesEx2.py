#Program for Listing the Files and Database connectivity in a Folder
#ListFilesEx2.py
import os
try:
    foldername=input("Enter Folder Name:")
    FileNames=os.listdir(foldername)
    print(FileNames)
    print("-----------------------------------------------")
    for filename in FileNames:
        print(filename)
    print("-----------------------------------------------")
except FileNotFoundError:
    print("Folder does not exist")
