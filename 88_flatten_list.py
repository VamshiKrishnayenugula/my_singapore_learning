"""There are many ways to flatten a list. We have covered other 
methods already. There is another way we can flatten a nested 
list. We can use a module called more_itertools. We will use 
the collapse() class from this module. This is a one-line 
solution. First, install the module using:"""

import more_itertools

nested_list = [[12, 14, 34, 56], [23, 56, 78]]

print(nested_list)
print('flatten list is ', list(more_itertools.collapse(nested_list)))

"""Collapse a list of tuples
The power of the collapse() method is that it will flatten any 
list, even a list of tuples. See below:
"""
import more_itertools
list_tuples = [(12, 14, 34, 56),(23, 56, 78),(12, 23, 56)]
print(list(more_itertools.collapse(list_tuples)))