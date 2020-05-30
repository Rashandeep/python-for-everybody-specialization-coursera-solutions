text = "X-DSPAM-Confidence:    0.8475"
one=text.find('0')
two=text.find('5')
res=text[one:two+1]

fres=float(res)
print(fres)
