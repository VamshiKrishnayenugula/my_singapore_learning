#counter

from collections import Counter

list1 = ['John','Kelly', 'Peter', 'Moses', 'Peter',"Peter"]

count_peter = Counter(list1).get("Peter")

print(count_peter)

"""If you want to know how many times an item appears in an 
iterable, you can use the counter() class from the collection 
module. The counter() class will return a dictionary of how many 
times each item appears in an iterable. Let’s say we want to know 
how many times the name Peter appears in the following list; 
here is how we can use the counter() class of the collections 
module."""

print("another way")
count = 0 
for i in list1:
    if i =="Peter":
        count+=1

print('another couunt is ', count)