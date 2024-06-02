#Program for saving Dict Data into the JSON File
#DictObjectToJsonFile.py
import json
d={"BID":1000,"NAME":"PYTHON","PRICE":456.67,"PUB":"TATA-MCGH"}
with open("book.json","a") as fp:
    json.dump(d,fp)
    print("Dict Data Saved in JSON FIle--Verify")