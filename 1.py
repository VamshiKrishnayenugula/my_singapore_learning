#printing horizontally

list1 = [2,345,3,5]
print("verticle print")
for i in list1:
    print(i)
print("horizontal print")
for i in list1:
    print(i, end= " ")


print("horizontal  print with a separator ,")
for i in list1:
    print(i, end= " , ")


print("horizontal  print with a separator /")
for i in list1:
    print(i, end= "  / ")

"""When looping over an iterable, the print function prints each 
item on a new line. This is because the print function has a 
parameter called end. By default, the end parameter has an 
escape character (end = "\n"). Now, to print horizontally, we
need to remove the escape character and replace it with an 
empty string (end = "")."""