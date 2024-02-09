l1 = [ 1,2,34,5]
l2 = [34,67,89]

l3 = l1 + l2
print(l3)

#flatten the nested list

l4 = [[1,2,3],[34,56,6]]

l5 = sum(l4,[])

print(l5)

#another way to flatten the nested list

from functools import reduce
new_list = reduce(lambda x,y : x+y,l4)
print('new list is',new_list)