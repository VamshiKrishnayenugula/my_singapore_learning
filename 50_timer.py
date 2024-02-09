import timeit
def timer(code):

    tm = timeit.timeit(code,number=20)
    return f'Execution time is {tm:2f} secs'


if __name__ == "__main__":
    print(timer('sum(num ** 2 for num in range(1000000))'))

    """If you want to know the execution time of a given code, you can 
use the timeit() module. Below, we create a function called timer 
that uses timeit() from the timeit module. We're basically using 
timeit to determine how long it takes to run sum(num**2 for 
num in range(10000)).The first parameter of the timeit 
function in the code below is stmt. This is where we pass the 
Python code that we want to measure. This parameter only takes 
a string as an argument, so we have to ensure that we convert our 
code to a string format. The number parameter is basically the 
number of executions we want to run on this code. 

PS D:\My_learning> & C:/Users/Vamshi/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/My_learning/Data_Camp/Functions/hundred/50_timer.py
Execution time is 3.440752 secs
PS D:\My_learning> """


import timeit

test = "sum(num **2 for num in range(1000008))"

tm = timeit.timeit(test)

print(f'time for this function is {tm:2f}')

"""It’s not necessary to create a function like we did above. You can 
also use timeit without creating a function. Let’s simplify the 
above code by writing it without a function. Remember that the 
stmt parameter only takes a string as an argument; that is why 
the test variable below, which is the code that we pass to the 
timeit() function, is a string"""