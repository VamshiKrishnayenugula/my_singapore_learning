"""a high order function is a function that takes another function as an argument or returns another function

 The code below 
demonstrates how we can create a function and use it inside a 
high-order function. We create a function called sort_names, 
and we use it as a key inside the sorted() function. By using 
index[0], we are basically telling the sorted function to sort 
names by their first name. If we use [1], then the names would 
be sorted by the last name.

"""

def sort_names(x):
    return x[0]

names = [('john','kelly'), ('chris','rock'), ('will','smith')]

sorted_names = sorted(names, key=sort_names)

print(sorted_names)