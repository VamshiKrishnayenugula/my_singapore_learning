"""if you have two sequences and you wnat to loop over them at the same time
how can you go about it in python 
this is when zip() function comes in handy 
the zip() function creaes pairs of iems in the sequences 
the element at index once in sequence is paired with the element at the index one in squence two

this process repeats for all the other indexes
lets demonstrate how we can loop over two sequences at the same time"""

#list one

first_names = ['yenugula','suggu','gampa']

second_name = ['vamshi','gnani','abi']

full = list(zip(first_names,second_name))

print(type(full))

print(full)

#now side by side

for i,j in zip(first_names,second_name):
    print(i,j)