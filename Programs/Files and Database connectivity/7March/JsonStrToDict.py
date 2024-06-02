#Program representing JSON String Format and Converts to Dict Format
#JsonToDict.py
import json
jsonstr='{"sno":"10","sname":"RS","marks":"45.67"}'
print("JSON Data={}\t Type of jsonstr={}".format(jsonstr,type(jsonstr)))
print("-"*50)

# Convert json str into dict type---use json.loads(jsonstrdata)
x=json.loads(jsonstr)
print("x={}\t Type of x={}".format(x,type(x)))
print("-"*50)
print("\tDict data")
print("-"*50)
for key,val in x.items():
    print("\t{}----->{}".format(key,val))
print("-"*50)

#convert dict object to json-str
d={"eno":100,"ename":"TR","sal":3.4}
print("d={} and type={}".format(d,type(d)))
s=str(d)
print("Json str={} and type jsonstr={}".format(s,type(s)))
