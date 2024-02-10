#merging dictionaries

name1 = {"kelly":23, "vamshi":30}
name2 = {"manoj": 24, 'sk':34}

print("merge with |")

print(name1 | name2)

print('merge with **')

print({**name1,**name2})

"""two dictionaries that you want to combine, you can 
do so using two easy methods. You can use the merge ( | ) 
operator or the (**) operator.
e merge ( ** ) operator. With this operator, you need to 
put the dictionaries inside the curly brackets.
"""
