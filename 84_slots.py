"""slots are used in classes
they are basically attributes that an instance object will have 

example

class cars:
__slots__= ['make','brand']

we expect every object in the cars class to have these attributes 
make and brand

so why to use slots 
we use slots because they help us save memory sparce
class objects take up less space when we use slots
see the difference in object size in the following exampls
"""

import sys
class cars:
    def __init__(self,make, brand):
        self.make = make
        self.brand = brand

print(f'the memoy size is {sys.getsizeof(cars)}')


class cars2:
    __slots__ = ['make', 'brand']

    def __init__(self,make,brand):
        self.make = make
        self.brand = brand

print(f'now the size if {sys.getsizeof(cars2)}')