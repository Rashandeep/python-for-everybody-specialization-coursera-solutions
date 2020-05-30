fname=input("enter file name")
try:
    fh=open(fname)
except:
    print("file not found")
    quit()

stuff=dict()

for line in fh:
    if not line.startswith("From:"):
        continue
    words=line.split()
    res=words[1]
    stuff[res]=stuff.get(res,0)+1

bigcount=None
bigword=None
for a,b in stuff.items():
    if bigcount is None or b>bigcount:
        bigcount=b
        bigword=a

print(bigword,bigcount)
