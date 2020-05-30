fname=input("enter the file name")
try:
    fh=open(fname)
except:
    print("file doesnot exsist")
    quit()

count=0

for line in fh:
    line=line.rstrip()
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    count=count+1
    words=line.split()
    res=words[1]
    print(res)

print('There were',count,'lines in the file with From as the first word')
