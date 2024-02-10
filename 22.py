#iterable or not - to confirm an object is iterable or not

"""this is how you can use code to check if an item is iterable or not. We are using the iter() function .
When you pass an item that is  not iterable as an an argument to the iter() functuon ,
it returns a TypeErrro. Below, we write a short script that checks if agiven object is an iterable ."""

arr = ['i','love', 'working','with','python']

try:
    iter_check = iter(arr)

except TypeError:
    print('object a not iterable')

else:
    print('object a is iterable')

b = 34.5

try:
    iter_check = iter(b)

except TypeError:
    print('Object b is not iterable')

else:
    print('object b is iterable')
