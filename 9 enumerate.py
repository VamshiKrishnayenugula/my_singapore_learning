"""In Python, the enumerate() function is used to iterate over a sequence (such as a list, tuple, or string)
 along with the index of the current item. It returns pairs of index and value."""

names = [ 'vamshi', 'krishna','yenugula','yadav']

for i,j in enumerate(names):
    print(f'postion is {i} and the name is {j}')

    """you can also sepcify a start value for the index using the start parameter"""


for i,j in enumerate(names, start = 1):
    print(i,j)