list1 = [2, 5, 6, 8, 1, 8, 9, 11]
print('original list',list1)
print()

list1.sort(reverse=False)
print("list in ascending orderlist1",list1)


print()

list1.sort(reverse=True)
print("list in descending orderlist1",list1)

"""The sort() method will sort a list in ascending order (by default). 
For the sort method to work, the list should have the same type 
of objects. You cannot sort a list mixed with different data types, 
such as integers and strings. The sort() method has a parameter 
called reverse; to sort a list in descending order, set reverse to 
True

"""

"""The sort() method does not return a new list; it sorts an existing 
list. If you try to create a new object using the sort() method, it 
will return None"""

list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list2 = list1.sort(reverse=True)
print(list2)