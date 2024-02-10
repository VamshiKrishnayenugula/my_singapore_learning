#accessing dictionarary keys

#using set comprehension

#set comprehension is similar to list comprehension. the difference is that it returns a set 

dict1 = {'name':'vamshi','name':'vamshi','age': 29, 'student':False, "country":"india"}

keys =  {key for key in dict1.keys()}
print(keys)
print(type(keys))

values = {value for value in dict1.values()}
print(f'values of dict  are {values}')

"""Your output shows that the keys in the dictionary are 
'name', 'country', 'student', and 'age', while the values are 'vamshi', 'india', False, and 29. The sets only contain unique elements,
 so if there are any duplicate values, they will appear only once in the set."""

#using set() function
print("***************************")
print(set(dict1))

print(sorted(dict1))