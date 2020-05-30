num=0
tot=0
while True:
    val=input("enter a number")
    if val=='done':
        break
    try:
        fval=float(val)
    except:
        print("invalid input")
        continue
    num=num+1
    tot=tot+fval
print(tot,num,tot/num)
