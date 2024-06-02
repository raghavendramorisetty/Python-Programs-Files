#Program for Removing a Folders Hierarhcy by using a function "removedirs()" present in os module
#RemoveFolderHierarchyEx.py
import os
try:
    os.removedirs("C:\\sampleFolder\\sampleFolder2\\sampleFolder3")
    print("Folder Hierarchy Removed----verify")
except FileNotFoundError:
    print("Folder does not exist")
except OSError:
    print("Specified folder hierarchy is not empty--make sure that it must be empty")

