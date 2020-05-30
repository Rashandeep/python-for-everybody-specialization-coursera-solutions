score=input("enter the score")
try:
    s=float(score)
except:
    print("enter the numeric value")
    quit()

if s>=1.0:
    print("enter value less than 1.0")
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
elif s<0.0:
    print("enter value larger than 0.0")
elif s<0.6:
    print("F")
