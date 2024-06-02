#This Program add the record to the existing book1.csv file
#CSVFileRecordEx1.py
import csv
with open("book1.csv","a") as fp:
    record=[104,"os",400] #single record
    # create an object of csv.writer class
    csvwr=csv.writer(fp)
    csvwr.writerow(record)
    print("Record added to book.csv--verify")
