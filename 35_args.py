def add(*args):
    addtion = sum(args)
    print(f'addition of given number is ', addtion)


add(1,2,3)

add(10,20,30)
"""when you are not sure how many arguments you will need for your function, you can pass *args (non keyword arguments)"""


def myFunc(**kwargs):
    for key , value in kwargs.items():
        print(f'{key} and the value is {value}')



myFunc(Name ="ben",age = 40,location ='hyd' )