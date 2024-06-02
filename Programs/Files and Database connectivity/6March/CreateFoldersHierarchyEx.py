#Program for Creating Folder Hierarchy
#for Creating Folder Hierarchy--we use function "makedirs()" present in os module
#CreateFoldersHierarchyEx.py
import os
try:
    os.makedirs("C:\\Users\\ragha\\OneDrive\\Desktop\\PythonPracticeFolderCreate\\Hai\\Hello\\HRU")
    print("Folders Hierarchy Created--verify")
except FileExistsError:
    print("Folder Hierarchy already created")