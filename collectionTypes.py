###########list###########
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1,2,3]]
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0])
print(names[2])
print(names[-1])
print(names[-4])
names[0]= 'Ann'
print(names)
names.append("Sia")
print(names)
names.insert(1, "Nikki")
print(names)
names.remove("Bob")
print(names)
print(names.index("Craig"))
print(len(names))
names.pop()
print(names)
for element in names:
    print(element)
############################################
a = [1,1,1,2,3,4]
print(a.count(1))
a.reverse()
print(a)
#a.reverse() equal a[::-1]
a[::-1]
print(a)

#############Tupels#############
#The values in the tuple cannot be changed nor the values be added to or removed from the tuple. 
ip_address = ('10.20.30.40', 8080)
one_member_tuple = tuple(['Only member'])
print (ip_address, one_member_tuple)

##############Dictionaries#############
#A dictionary in Python is a collection of key-value pairs. 
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}
ca_capital = state_capitals['California'] # To get a value
print(ca_capital)
#get all of the keys in a dic
for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))

#############################Set############################
#Sets are used in situations where it is only important that some things are grouped together, and not what order they were included. 
# For large groups of data, it is much faster to check whether or not an element is in a set than it is to do the same for a list.
first_names = {'Adam', 'Beth', 'Charlie'}
for names in first_names:
    print(names)
# You can build a set using an existing list
my_list = [1,2,3]
my_list = set(my_list)
print(my_list)
