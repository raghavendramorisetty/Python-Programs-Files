#Program for Creating a Folder
#To create a Folder, we use a function "mkdir()"  present in os module
#CreateFolderEx.py
import os
try:
    os.mkdir("C:\\Users\\ragha\\OneDrive\\Desktop\\PythonPracticeFolderCreate")
    print("Folder Created successfully--verify")
except FileExistsError:
    print("Folder already exist")
except FileNotFoundError:
    print("Folder Does not Exist")