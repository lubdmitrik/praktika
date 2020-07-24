import math
x = 4
p = (math.exp(-3*x)+math.tan(3*x - 3))/(math.fabs(math.sin(x))+(math.cos(x)+math.cos(2*x))**(1/4))
print(p)
