import time

def timer(func):
    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()

        print(f'run time is {end - start} secs')

    return inner


@timer
def range_checker():
    lst = []

    for i in range(10000):
        lst.append(i*3)


range_checker()


"""Timer Decorator
Below, I created a timer function that uses the perf_counter class 
of the time module. Notice that the inner() function is inside the 
timer() function; this is because we are creating a decorator. 
Inside the inner() function is where the "decorated" function will 
run. Basically, the "decorated" function is passed as an argument 
to the decorator. The decorator then runs this function inside the 
inner() function.
The @timer right before the range_tracker function means that 
the function is being decorated by another function. To 
"decorate" a function is to improve or add extra 
functionality to that function without changing it. By 
using a decorator, we are able to add a timer to the 
range_tracker function. We are using this timer to check how 
long it takes to create a list from a range."""