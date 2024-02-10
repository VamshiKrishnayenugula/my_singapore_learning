"""What if you have a number of dictionaries and you want to 
wrap them into one unit? What do you use? Python has a class 
called chainMap that wraps different dictionaries into a single 
unit. It groups multiple dictionaries together to create one 
unit. ChainMap is from the collections module. Here is how it 
works:"""

from collections import ChainMap


x = {'name': 'Jon','sex': 'male'}
y = {'name': 'sasha', 'sex': 'female'}

full_dict = ChainMap(x,y)

print(full_dict)

print(type(full_dict))

"""We can also access the keys and values of the dictionaries 
wrapped in a ChainMap. Below, we print out the keys and 
values of the dictionaries.

"""

from collections import ChainMap
x = {'name': 'Jon','sex': 'male'}
y = {'car': 'bmw', 'make': 'x6'}
dict1 = ChainMap(x, y)

print(list(dict1.keys()))
print(list(dict1.values()))