"""If you have two lists and you want to find the difference 
between the lists, that is, elements that are in list a but not 
in list b, use the set().difference(set()) method."""

a = [9,3,6,7,8,4]
b = [9,3,7,5,2,1]

diff = set(a).difference(set(b))

print(list(diff))

#by for loop

dffer =[]
for i in a:
    if i not in b:
        dffer.append(i)

print('by for is ', dffer)

#by list comprehension

differ = [number for number in  a if number not in b ]

print('by list comprehension ',differ)