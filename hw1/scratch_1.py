4a = float(input ("Input a: "))
b = float(input ("Input b: "))
c = float(input ("Input c: "))
if c == a*b:
    print ("c = a * b\n")
elif c == -b/a:
    print ("c = -b / a\n (is a root of equation ax = b)")
else:
    print ("c != a * b\nc != -b / a")
