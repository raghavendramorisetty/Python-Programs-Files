#MultipleIndFoldersEx1.py
import os,time
try:
    lst=["kiran","python","student"]
    for val in lst:
        os.mkdir("C:\\Users\\ragha\\OneDrive\\Desktop\\PythonPracticeFolderCreate\\Hai\\Hello\\HRU\\HELLO"+val)
        #os.mkdir("C:\\Users\\ragha\\OneDrive\\Desktop\\PythonPracticeFolderCreate\\Hai\\Hello\\HRU\\" + val)
        print("'{}' Folder created".format(val))
        time.sleep(2)
except FileExistsError:
    print("Folder Name Already Exists")