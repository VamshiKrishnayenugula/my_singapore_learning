"""if you have a list of dictionaries and your want tot sort them by their vlaues you can use the itemgetter class from the operator module and the sorted fujnction here ais an a
example to demontrate
"""

from operator import itemgetter
d = [{"school":"yale", "city": "Beijing"},{"school":"cat", "city": "Cairo"}]

sorted_list = sorted(d, key = itemgetter('school'))

print(sorted_list)

"""The above example sorts a list in ascending order. If you 
wanted to sort the list in descending order, you would have 
to set the reverse parameter in the sorted function to True. You 
can see below that the list has been sorted in descending order."""


sorted_list_rev = sorted(d, key = itemgetter('school'),reverse=True)

print(sorted_list_rev)