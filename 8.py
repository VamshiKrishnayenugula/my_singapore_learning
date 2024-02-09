#flatten a nested list


"""I will share with you three (3) ways you can flatten a list. The 
first method employs a for loop, the second employs the 
itertools module, and the third employs list comprehension."""
list1 = [[1,2,3], [4,5,6]]

newlist= []

print('by for loop')
for i in list1:
    for j in i:
     newlist.append(j)

print(newlist)

print()
print( 'by itertools')

import itertools

flat_list = list(itertools.chain.from_iterable(list1))

print(flat_list)

print()
print('by list compreshesiion')

fl= [ i for j in list1 for i in j]
print(fl)