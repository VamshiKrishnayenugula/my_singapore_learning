"""we write a code that calculates the factorial of a given 
number. A factorial of a number is the product of all integers 
from 1 to that number. The factorial of 3 is calculated as (1 * 2 * 
3), which is 6. The for loop in the function below executes this 
calculation. Below, we calculate the factorial of the integer 8.
"""



def fact(n:int)->int:
    f = 1
    if n <0:
        print('negative numbers have no factorial')

    else:
        for i in range(1,n+1):
            f = f*i
        return f'factorial of n is  {f}'
        


print(fact(8))