
from operator import itemgetter

name = [('vamshi','krishna'),('peter','parker'),('mohan','suresh')]

#sort names by first name

first_name = sorted(name,key = itemgetter(0))
print('sorted by firstname',first_name)


last_name = sorted(name,key = itemgetter(1))
print('sorted by last is   ',last_name)


# sort names by first name, then last name
sorted_names = sorted(name,key=itemgetter(0,1))
print('Sorted by last name & first name',sorted_names)


"""Sorting a List of Tuples
You can sort a list of tuples using the itemgetter() class of the 
operator module. The itemgetter() function is passed as a key 
to the sorted() function. If you want to sort by the first name, 
you pass the index (0) to the itemgetter() function. Below are 
different ways you can use itemgetter() to sort the list of tuples."""