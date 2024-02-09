

from datetime import datetime
import time

a = 'Hello' 
b = 'Python' 
c = 'world' 
f = 'People' 

# Using concatenation 
start = time.perf_counter()
for _ in range(100000):
    d = a + b + c + f
"""In the code snippet you provided, the underscore (_) is often used as a throwaway variable or a placeholder
 when its value is not going to be used in the loop. 
 In Python, the convention is to use _ when you need a variable name, but you don't actually care about its value."""
end = time.perf_counter()

print(f'Concatenation time is {end - start:.5f} seconds')


#using join method

start1 = time.perf_counter()

for i in range(100000):
    d = " ".join([a,b,c,d])

end1 = time.perf_counter()

print(f'joining time is {end1 - start1:.5f}')

