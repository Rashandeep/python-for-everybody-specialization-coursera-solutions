fname=input("enter file name")
try:
    fh=open(fname)
except:
    print("file dose not exsist")
    quit()

stuff=dict()
lst=list()

for line in fh:
    line=line.rstrip()
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    words=line.split()
    word=words[5].split(':')
    res=word[0]
    lst.append(res)

lst.sort()

for result in lst:
        stuff[result]=stuff.get(result,0)+1

for k,v in stuff.items():
    print(k,v)
