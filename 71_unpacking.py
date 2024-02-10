"""Unpacking a List 
Sometimes you want to unpack a list and assign the elements to 
different variables. Python has a method that you can use to 
make your life easier. We can use the Python unpacking 
operator, asterisk (*). Below is a list of names. We want to get 
the boy’s name and assign it to the variable "boy_name." The 
rest of the names will be assigned to the variable "girls_name." 
So, we assign (unpack from the list) the first item on the list to 
the boy variable. We then add "*" to the girls_name variable. 
By adding * to the girl’s name, we are basically telling Python 
that once it unpacks the male name, all the other remaining 
names must be assigned to the girls_name variable. See the 
output below:"""

name= ['vaishu','vamshi','kharthika']

daughter, *parents = name

print(daughter)
print(parents)


names = [ 'Rose', 'Mary', 'Lisa', 'John']
*girls, boy = names
print(boy)
print(girls)