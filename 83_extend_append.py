"""
Extend and append are both list methods. They both add 
elements to an existing list. The append() method adds one (1) 
item to the end of the list, whereas the append()
The extend() method adds multiple items to the end of the 
list. Below, we use the append() method to append numbers2
to numbers1. You can see that the whole list of numbers2 has 
been appended to numbers1 as one (1) item
"""

num1 = [1,3,4,6]
num2 = [56,34,35]

"""numappend = num1.append(num2)
print(numappend)

he append method in Python does not return a new list. 
Instead, it modifies the original list in place and returns None. 
Therefore, when you print numappend, you see None because that's what the append method returns."""

num1.append(num2)

print(num1)
"""[1, 3, 4, 6, [56, 34, 35]]"""

num2.extend(num1)
print(num2)


"""
The output you're seeing, [56, 34, 35, 1, 3, 4, 6, [...]], indicates that there is a circular reference or self-reference in the list. The ellipsis (...) is used to represent a circular reference when the __repr__ method of an object encounters an object that it has already printed during the current representation.

In your case, the circular reference is caused by the fact that num1 contains a reference to num2, and num2 is also extended with num1. This creates a situation where the representation of num2 includes a reference back to num1, forming a circular reference."""