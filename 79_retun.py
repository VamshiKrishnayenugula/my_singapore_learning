"""By default, a function returns one value, and it stops. Below, we 
have 3 values in the return statement. When we call the 
function, it returns a tuple of all three items. """

def values():
    return 1,2,3

print(values())

"""What if we want to return three separate values? How do we do 
it in Python? We create a variable for each value we want to 
return. This makes it possible to access each value separately.
See the code below:"""
print('with varaible name')

x,y,z= values()

print(x)