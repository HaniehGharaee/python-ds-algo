import operator
a,b = 1,2
a + b
a += b
c = operator.add(a,b)
print(c)
d = operator.iadd(a, b)
print(d)
str = "first string" + " second string"
print(str)
sum = [1,2,3] + [4,5,6]
print(sum)
a, b = 2,3
print(a**b)
print(pow(a,b))
import math, operator
print(math.pow(a,b))
print(operator.pow(a,b))
