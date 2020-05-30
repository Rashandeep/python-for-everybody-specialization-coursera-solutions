import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input("Enter location: ")
fhand = urllib.request.urlopen(url)
print("Retrieving:",url)
# for line in fhand:
#     print(line.decode().strip())

data=fhand.read()
print("Retrieved",len(data),"characters")
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment') #it returns a list
print('Count:', len(lst))

lval=list()
for item in lst:
    val=item.find('count').text
    fval=int(val)
    lval.append(fval)

print("Sum:",sum(lval))
