###############Set##############
# Intersection
a = {1,2,3,4,5}.intersection({3,4,5,6})
print(a)
# Union
b = {1,2,3,4,5}.union({3,4,5,6})
c = {1,2,3,4,5}|{3,4,5,6}
print(b)
print(c)
#Difference
d = {1, 2, 3, 4}.difference({2,3,5})
e = {1, 2, 3, 4} - {2,3,5}
print(d)
print(e)
# Symmetric difference with
f = {1,2,3,4}.symmetric_difference({2,3,5})
g = {1,2,3,4} ^ {2,3,5}
print(f)
print(g)
# Superset check
h = {1,2}.issuperset({1,2,3})
i = {1,2} >= {1,2,3}
j = {1,2,3,4}.issuperset({1,2})
print(h, i, j)
# Subset check
k = {1,2}.issubset({1,2,3})
l = {1,2} <= {1,2,3}
print(k , l)
# Disjoint check
m = {1,2}.isdisjoint({3,4})
n = {1,2}.isdisjoint({1,4})
print(m , n)
###################################
#Existence check
o = 2 in {1,2,3}
p = 4 in {1,2,3}
q = 4 not in {1,2,3}
print(o, p, q)
##################################
#Add and Remove 
s = {1,2,3}
s.add(4)
print(s)
s.discard(3)
print(s)
s.remove(2)
print(s)
#s.remove(2) # KeyError!