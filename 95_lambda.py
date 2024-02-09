from functools import reduce

num =5

f = reduce(lambda a,b: a*b,range(1,num+1))
print(f)