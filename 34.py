"""set comparision is sismilar to list comprehesion 
ths only dirrerence is that it returns a set and not a list .
instead of square brackets , set compreshension uses curly brackets
this is because sets are enclosed in curly brckets.
yuo can use set comprehension on an iterble lets say we have a list of uppercase strings and we want to convert them into lowercase sring s and remove duplicates 
we can use set comprehension since sets are not ordered  the order of teh items int the iterable will be change sets to not allow duplicates, so only on e peadsce will be in th out put
set
"""
list = ['love','hate','war','vamshi', 'vamshi']

set1 = { word.lower() for word in list}
print(set1)