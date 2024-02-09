def sort_list(arr:list):
    a = sorted(arr, reverse=True)
    return a[:5]

my_list = [2,4,4556,7,854,4,5,6,7,8,9]

print(sort_list(my_list))

"""There is a 
Python built-in module that you can use that will make your life 
easier. It is called heapq. With this module, we can easily return 
the 5 largest numbers using the nlargest method. The method 
takes two arguments: the iterable object and the number of 
numbers we want to return."""

print('by heapq')

import heapq

print('largest',heapq.nlargest(3,my_list))
print('4 smallest', heapq.nsmallest(4,my_list))