#Program for copying the content of One File to another File
#FileCopy.py
srcfile=input("Enter source File Name:")
try:
    with open(srcfile,"rt") as rp:
        dstfile=input("Enter Destination File:")
        with open(dstfile,"at") as wp:
            srcfiledata=rp.read() #Read the data from srcfile
            wp.write("\n")
            wp.write(srcfiledata) # write src file data to the destination file
            print("File Copied--verify")
except FileNotFoundError:
    print("Source File does not Exist so cannot do copying process")