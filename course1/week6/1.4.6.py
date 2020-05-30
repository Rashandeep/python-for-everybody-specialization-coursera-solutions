hour=input("enter hours")
rate=input("enter rate per hour")
try:
    h=float(hour)
    r=float(rate)
except:
    print("enter numeric values")
    quit()

def computepay(h,r):
    if h<=40:
        pay=h*r
    else:
        one=h*r
        two=(h-40)*(0.5*r)
        pay=one+two
    return pay

pay=computepay(h,r)
print("Pay",pay)
