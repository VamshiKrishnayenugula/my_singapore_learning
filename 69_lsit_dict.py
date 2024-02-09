"""Two Lists into a Dict
Sometimes, while working with lists, you may want to change the 
data type to a dictionary. That is, you may want to combine the lists 
into a dictionary. To do this, you may have to use the zip() function 
and the dict() function. The zip() function takes two iterables and 
pairs the elements. The first element in iterable one is paired with 
the first element in iterable two, and the second element with 
another second element, etc. The zip() function returns an iterator 
of tuples. The dict() function will convert the paired elements into a 
key-value combination, creating a dictionary."""


list1 = ['name', 'age', 'country']
list2 = ['Yoko', 60, 'Angola']


d = dict(zip(list1,list2))

print(d)


"""If an element in the list cannot be paired with another element, 
then it will be left out. Let’s say list1 has four elements and 
list2 has five; the fifth item in list2 will be left out. You can see 
below that "Luanda" has been left out."""


list1 = ['name', 'ageee', 'country']
list2 = ['Yoko', 60, 'Angola', "Luanda"]
dict1 = dict(zip(list1,list2))
print(dict1)
