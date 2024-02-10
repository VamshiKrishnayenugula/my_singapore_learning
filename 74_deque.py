"""If you want to add and pop elements from both sides of a list, 
you can use deque (double-ended queue). Unlike a normal list 
that lets you add and remove elements from one end, deque 
allows you to add and remove elements from both the left and 
right sides of the list. This makes it quite handy if one has a big 
stack. Deque is found in the collections module. In the example 
below, see how we are able to append elements at both ends of 
the list.
"""

from collections import deque

arr = deque([1,3])

arr.appendleft(55) #append to left side of list

print(arr)

arr.append(535) #append to right

print(arr)

"""deque also makes it easy to pop (remove ) elements on both ends of the list"""

arn = deque([1,2,3,5,5,467,34])
print()

print(arn)

arn.pop() #as ususual last element will be removed

print(arn)

arn.popleft()#with this left side element will be removed

print(arn)