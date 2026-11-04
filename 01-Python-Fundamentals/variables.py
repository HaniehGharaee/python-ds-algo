a = 2
print(a)
print(type(a))
b = 3.14
print(b)
print(type(b))
name = 'Hanieh Gharaee'
print(name)
print(type(name))
q = True
print(q)
print(type(q))
x = None
print(x)
print(type(x))
a,b,c = 1,2,3
print(a, b, c)
print(a,c)
# a, b = 4,5,6
# print(a, b)  ValueError: too many values to unpack (expected 2)
a, b, _ = 1,2,3
print(a, b)
print(a,b,_)
a = b = c = 1
print(a,b,c)
b = 2
print (a , b , c)
x = y = [7, 8 , 9]
x = [13, 8, 9]
print(y)
x = y = [7, 8 , 9]
x[0] = 13
print(y)
x = [1,2,[3,4,5],6,7] # this is nested list
print (x[2])
print (x[2][1])
print(x[0], x[2][0])