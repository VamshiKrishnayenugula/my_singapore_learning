"""If you want to get the indices of items in a sequence, such as a 
list, we can use the len() and range() functions if you don’t want 
to use the enumerate() function. Let’s say we have a list of 
names and we want to return the indices of all the names in the 
list. Here is how we can use the len() and range() functions:
"""
names = ['John', 'Art', 'Messi']

for i in range(len(names)):
    print(i, names[i])

    """ if we want to return just the index of one of the names in the list , 
    we can combine the len() and range() functino with a conditiojnal statement 
    """

"""    for j in range(len(names)):
        if names[j] == '':
            print('hi bro')
            break"""

