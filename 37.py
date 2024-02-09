"""dictionary compreshension is a one line code that transforms a dictionary into another dictionary
witih modified values.it takes your code intuitive and concise 
it is similar to list comprehension

"""

dict1 = {'Grade': 70, 'Weight': 45, 'Width': 89}

dict2 = { k:float(v) for k,v in dict1.items()}

print(dict2)