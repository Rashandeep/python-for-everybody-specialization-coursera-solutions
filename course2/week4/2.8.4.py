fname=input("enter the file name")
try:
    fh=open(fname)
except:
    print("file doesnot exsist")
    quit()

stuff=list()

for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        if word in stuff:
            continue
        stuff.append(word)

stuff.sort()
print(stuff)
