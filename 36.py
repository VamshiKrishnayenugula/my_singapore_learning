#python filter function

#normal by using for

names = ['Derick', 'John', 'moses', 'linda']
lower_case =[]
for i in names:
    if i.islower():
        lower_case.append(i)

print(lower_case)

# now by using filter 

lower_case_new = list(filter(lambda x:x.islower() , names))
print('another lower is ', lower_case_new)