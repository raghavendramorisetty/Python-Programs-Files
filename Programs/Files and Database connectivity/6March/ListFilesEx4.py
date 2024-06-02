#Program for Listing the Python Files and Database connectivity only  in a Folder(Another Folder)
#ListFilesEx4.py
import os
try:
    FileNames=os.listdir("C:\\sample2")
    print("-------------------------------------------------")
    for filename in FileNames:
        if(filename[-3:]==".py"):
            print("\t{}".format(filename))
    print("-------------------------------------------------")
except FileNotFoundError:
    print("Folder does not exist")

