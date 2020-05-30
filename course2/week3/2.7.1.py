fname=input("enter file name")
try:
    fh=open(fname)
except:
    print("file doesnot exsist")
    quit()

for line in fh:
    line=line.strip()
    cline=line.upper()
    print(cline)
