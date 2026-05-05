#Consumes less memory (lazy evaluation)
#Better for working with large data
a = reversed('hello')#Creates an iterator that produces characters in reverse
print(a) #reversed object (An iterator object type)
#It does not reverse the string directly but returns an iterator
#which means it is only ready to reverse the elements one by one, not to generate the entire output
#0x000001A21E8F9540 is a memory address (address in RAM) that indicates where in memory this object was created
print(list(a))
print(''.join(reversed('hello')))
#In fact, it works without creating a list because reversed() returns an iterator.
#join() also has an important condition:
#👉 It only takes something that is iterable Not necessarily a list
#🔥Iterators are disposable

#tuple
a = (1,2,3)
b =  ('a', 1, 'python', (1,2))
print(b[2])
#b[2] = 'something else' TypeError: 'tuple' object does not support item assignment
#tupel -> Supports indexing; immutable; hashable if all its members are hashable

#list
a = [1,2,3]
b = ['a', 1, 'python', (1,2), [1,2]]
print(b)
b[2] = 'something else'
print(b)
#Not hashable; mutable.

#set
a = {1,2,'a'}
print(a)
#a[2] = 'something else' #TypeError: 'set' object does not support item assignment
# An unordered collection of unique values. Items must be hashable

#dict
a = {1:'one', 2: 'two'}
b = {'a': [1,2,3], 'b': 'a string'}
a[1] = {2: 'zro'}
print(a,b)
#An unordered collection of unique key-value pairs; keys must be hashable.


#An object is hashable if it has a hash value which never changes during its lifetime

a = 'hello'
list(a)
print(list(a))
set(a)
print(set(a))
tuple(a)
print(tuple(a))