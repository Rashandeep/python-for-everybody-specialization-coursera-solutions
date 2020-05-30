import urllib.request, urllib.parse, urllib.error
import json

url=input("Enter location: ")
fhand = urllib.request.urlopen(url)
print("Retrieving:",url)

data=fhand.read()
print("Retrieved",len(data),"characters")

info = json.loads(data)
com=info["comments"]
print("Count:",len(com))

lst=list()

for a in com:
    val=a["count"]
    fval=int(val)
    lst.append(fval)

print("Sum:",sum(lst))
