"""
we can use the assert statemnet to check or debug your code.
the assert statement will catch errors early on in the code.
The assert statement takes two arguments: a condition and and an optional error message.
here is the syntax beelow:

assert <condition >, [error message]

the condition returns a boolean value of either True or False.
the error message is teh message we want to be displayed if the condition is False
"""
print('helo')
name =  ["Jon","kelly", "kess", "PETR", 4]

lower_names = []

for item in name:
    assert type(item) == str,'non string items in list'

    if item.islower():
        lower_names.append(item)

print(lower_names)


print('vamshi')