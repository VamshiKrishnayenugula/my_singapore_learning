l1 = [input('enter three number').split(sep= ',')]

print(l1)
print(type(l1))


"""What if you want to get multiple inputs from a user? How do you 
do it in Python? Python uses the input() function to get input 
from the user. The input() function takes one input at a time; 
that’s the default setting. How can we modify the input function 
so it can accept multiple inputs at a time? We can use the input()
function together with the string method, split(). Here is the 
syntax below:
input().split()
With the help of the split() function, the input() function can 
take multiple inputs at the same time. The split() method 
separates the inputs. By default, the split method separates
inputs right at the whitespace. However, you can also specify a 
separator. Below, we ask a user to input three (3) numbers. We 
use the split() method to specify the separator. In this case, we 
separate the inputs with a comma (,). Then we calculate the 
average of the three numbers. If the inputs are 12, 13, and 14, 
we get the output below"""


a, b, c = input("Please input 3 numbers: ").split(sep=',')
average = (int(a) + int(b) + int(c))/3
print(average)
