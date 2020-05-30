fname=input("enter file name")
try:
    fh=open(fname)
except:
    print("file doesnot exist")
    quit()

count=0
sum=0

for line in fh:
    line=line.strip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    num=line.find(':')
    val=line[num+1:]
    fval=float(val)
    sum=sum+fval

print("Average spam confidence:",sum/count)
