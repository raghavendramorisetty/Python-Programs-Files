#Program for Reading JSON File Data into Dict Object
#JSONFileToDict.py
import json
try:
    with open("book.json","r") as fp:
        d=json.load(fp)
        print("-"*40)
        for key,value in d.items():
            print("{}----{}".format(key,value))
        print("-"*40)
except FileNotFoundError:
    print("JSON File does not exist")
    