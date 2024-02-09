
"""in python we can easily convert a string to a list of strings. 
we can combine the list() functino with the map() function. 
The map functino returns a map object which is an iterator.
the map() functjin takes two argumnets a function and an iterable .
Below, the list is an iterable , and str() is  the function .
we then use the list() function to return a list .
the split() method divides or splits a string at whitespaces.

"""
s= 'hi my name is vamshi'

str1 = list(map(str,s.split()))

print(str1)

""" you can convert a list of strings back to a string using the map() function 
in conjuction with the join() method .
lets convert the out of the above code back to a string using the map() and join() methods"""

lsit1 = ["I ",'am','vamshi']

now = " ".join(map(str,lsit1))
print(now)