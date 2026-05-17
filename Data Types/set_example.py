###############Set##############
# Intersection
a = {1,2,3,4,5}.intersection({3,4,5,6})
print(a)
#a.intersection(b)
# Union
b = {1,2,3,4,5}.union({3,4,5,6})
c = {1,2,3,4,5}|{3,4,5,6}
print(b)
print(c)
#a.union(b)
#Difference
d = {1, 2, 3, 4}.difference({2,3,5})
e = {1, 2, 3, 4} - {2,3,5}
print(d)
print(e)
# a.difference(b)
# Symmetric difference with
f = {1,2,3,4}.symmetric_difference({2,3,5})
g = {1,2,3,4} ^ {2,3,5}
print(f)
print(g)
#a.symmetric_difference(b)
# Superset check
h = {1,2}.issuperset({1,2,3})
i = {1,2} >= {1,2,3}
j = {1,2,3,4}.issuperset({1,2})
print(h, i, j)
#a.issuperset(c)
# Subset check
k = {1,2}.issubset({1,2,3})
l = {1,2} <= {1,2,3}
print(k , l)
#c.issubset(a)
# Disjoint check
m = {1,2}.isdisjoint({3,4})
n = {1,2}.isdisjoint({1,4})
print(m , n)
#a.isdisjoint(b)
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
s.update({5, 6})
print(s)
#s.remove(2) # KeyError!
##########################################################################
# The way to get the unique elements from a list is to turn it into a set  
restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
#Same list as the original but without duplicates
print(list(unique_restaurants))
###########################################################################
#Set of set
#r = {{1,2}, {3,4}}
#print(r) #TypeError: unhashable type: 'set'
r = {frozenset({1,2}), frozenset({3,4})}
print(r)
###########################################################################
print(len(s))
t = {1,2,2,3,4}
u = {3,3,4,4,5}
v = {5,6}
print(len(t&u))
print(len(t&u) == 0)
print(t&v == set()) # {1,2,3,4} & {5,6} => set() == set()
print(u&v == set()) # {3,4,5} & {5,6} => {5} == set()
[] == [] # True
print(1 in t)
print(6 in t)
from collections import Counter
counterA = Counter(['a', 'b', 'b', 'c'])
print(counterA) 