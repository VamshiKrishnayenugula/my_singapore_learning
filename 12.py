list1 = ['lemon','Orange', 'apple', 'apricot','cot']

list_a =   [ i for i in list1 if i.startswith('a')]
print(list_a)

list_c = [ i for i in list1 if i.endswith('t')]
print(list_c)

"""The startswith() and endswith() are string methods that return 
True if a specified string starts with or ends with a specified 
value.
"""