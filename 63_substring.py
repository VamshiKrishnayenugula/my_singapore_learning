"""If you want to check if a string is a substring of another string, 
you can use the in and not in operators. Let’s say we want to 
test if "like" is a substring of string s. Here is how we do it using 
the in operator: The in operator will evaluate to True if "like” 
is a substring of s and False if it is not."""

s = 'hi this is vamshi from karimnagar'

if 'vamshi' in s:
    print(f'vamshi is a substring of string s which is {s}')

else:
    print('vamshi is not a substirng'
    )


"""We can also use the "not in" operator. The "not in" operator is 
the opposite of the in operator.
"""

if "karimnagar" not in s:
    print("knr is not part")

else:
    print('knr is there')

    """Python advises only using the find() method to know the 
position of a substring. If we wanted to find the position of 
"something" in a string, here is how we would use the find()
method: The find method returns the index where the substring 
starts"""


print(s.find('karimnagar'))