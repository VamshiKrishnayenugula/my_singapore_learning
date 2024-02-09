"""python provides a way to give hints on what type of argument is expected in a function or what data type a function should return.
these are called 'type hints' """

def translate(s:str) -> bool:
    if s:
        return True
    

print(translate('vamshi'))



"""Here we have a simple function. Notice that the function has 
one parameter, s. The "str" after the s parameter is a typing hint. 
It simply means that the function expects (or hints) that the 
argument that should be passed for parameter "s" must be a 
string. Notice the "-> bool" at the end? This is another typing 
hint. It hints that it expects the return value of the function to 
be a Boolean value. Now, hints are not enforced at runtime by 
Python; that means that if a non-string argument is passed and 
a non-Boolean value is returned by the function, the code will 
run just fine.
Why type hints? Type hints simply help to make the code more 
readable and more descriptive. By just looking at the hint 
annotations, a developer will know what is expected of the 
function"""