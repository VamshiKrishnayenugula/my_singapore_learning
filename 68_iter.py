"""if you want to create an iteratro for an objet 
use the iter() functijon .
once the iterator object is crearted , teh elements dcan be acccessed one at a time.
to access the elements in the iterator, you will have to use the next() function 

"""

names = ['vamshi','krishna','yadadv']

#creating an iterator

iter_obj = iter(names)

#accessing the items using the next function 

name1 = next(iter_obj)
print(name1)

name2 = next(iter_obj)
print(name2)

name3 = next(iter_obj)
print(name3)

"""name3 = next(iter_obj)
print(name3)

Traceback (most recent call last):
  File "d:\My_learning\Data_Camp\Functions\hundred\68_iter.py", line 25, in <module>
    name3 = next(iter_obj)
StopIteration

"""

#can also use the loop

while True:
    #accessing the elements in object using nexxt func

    try:
        print(next(iter_obj))

    except:
        break

    

    """"Why use iterators? Iterators have better memory efficienc"""