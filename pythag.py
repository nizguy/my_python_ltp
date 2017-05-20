import math
a = input("The length of side A: ")
b = input("The length of side B: ")
c = (a * a) + (b * b)
c = math.sqrt(c)


print "{}*{} + {}*{} = {} " .format(a, a, b, b, (a * a) + (b * b))
print "the length of side c is {}" .format(c)


