"""a return statement  return one element and ends the functin 
the yield statement retruns a package of elements called a generaor 
you have to unpack the package to  get the elements 
you can use a for loop or the next() function to unpack the generator"""

# using return statement 

def num (n:int) ->int:
    for i in range(n):
        return i
    

print(num(5))

"""out put

PS D:\My_learning> & C:/Users/Vamshi/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/My_learning/Data_Camp/Functions/hundred/44_ruturn_yield.py
0

You can see from the output that once the function returns 0, it 
stops. It does not return all the numbers in the range.
"""

#using yield

def num(n:int)->int:
    for i in range(n):
        yield i 


#creating a generator 
        
gen = num(6)

for i in gen:
    print(i,end=" ")


    """The yield function returns a "package" of all the numbers in the 
range. We use a for loop to access the items in the range


PS D:\My_learning> & C:/Users/Vamshi/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/My_learning/Data_Camp/Functions/hundred/44_ruturn_yield.py
0
0 1 2 3 4 5
PS D:\My_learning>


"""