import re

fname=input("enter file name")
try:
    fh=open(fname)
except:
    print("file doenot exist")
    exit()

lst=list()

for line in fh:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    for num in y:
        fnum=int(num)
        lst.append(fnum)
print(len(lst),sum(lst))
