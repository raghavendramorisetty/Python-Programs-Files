#Program for Reading the Data from CSV File by using Normal Files and Database connectivity
#Non-CSVReaderEx1.py
with open("employee.csv","r") as fp:
    csvdata=fp.read()
    print("------------------------------------")
    print("\tCSV File Data")
    print(csvdata)
    print("------------------------------------")