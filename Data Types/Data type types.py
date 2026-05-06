#############String Data Type##########
a_str = 'Hello world'
print(a_str)
print(a_str[0])
print(a_str[0:5])
#############Set Data Types#############
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  #duplicates will b remove
a = set('abracadabra')
print(a)  #unique letters in a
a.add('z')
print(a)
####Frozen Sets
b = frozenset('asdfagsa') # They are immutable and new elements cannot added after its defined. !!!b.add('z')
print(b)
cities = frozenset(["Frankfurt", "Basel", "Freiburg"])
print(cities)
##############Numbers data type##############
int_num = 10
print(type(int_num))
float_num = 10.2
print(type(float_num))
complex_num = 3.14j
print(type(complex_num))
###############List Data Type#############
list = [123,'abcd', 10.2, 'd']
list1 = ['hello', 'world']
print(list)
print(list[0:2])
print(list1 * 2) # will gave list1 two times.
print(list + list1)
###############Dictionary Data Type##########
dic = {'name': 'red', 'age':10}
print(dic)
print(dic['name'])
print(dic.values())
print(dic.keys())
#################Tuple Data Type##############
tuple = (123, 'hello')
tuple1 = ('world',)
print(tuple)
print(tuple[0])
print(tuple + tuple1)
#tuple[1] = 'update' !!TypeError: 'tuple' object does not support item assignment