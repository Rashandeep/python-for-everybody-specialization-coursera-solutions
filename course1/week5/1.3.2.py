hrs = input("Enter Hours:")
rate=input("enter rate per hour")
try:
    r=float(rate)
    h = float(hrs)
except:
    print("enter numeric values")
    quit()

if h<=40:
    pay=h*r
else:
    one=h*r
    two=(h-40)*(0.5*r)
    pay=one+two
print(pay)
