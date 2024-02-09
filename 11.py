a = [122334454,445564324,334532345565,2345]
new_list = ['{:,}'.format(i) for i in a]

print(new_list)

"""If you are working with large figures and you want to add a 
separator to make them more readable, you can use the format()
function."""


a = [10989767, 9876780, 9908763]
new_list =[f"{num:_}" for num in a]
print(new_list)